from functools import partial
from zipfile import ZipFile

from PIL import Image
from album.models import Album
from concurrent.futures import ThreadPoolExecutor
import environ
import io
from pathlib import Path
import pyqrcode
import requests


env = environ.Env()


DATA_DIR = Path("/tmp")
QR_SCALE = 4
MAX_THREADS = env.int('MAX_THREADS', default=1)


def generate_zip(album):
    accessible_interviews_images = generate_accessible_interviews(album)

    zip_buffer = io.BytesIO()

    with ZipFile(zip_buffer, 'w') as zip_file:

        for index, image in enumerate(accessible_interviews_images, 1):
            image_content = get_image_content(image)
            image_filename = f"{index}.{image.format.lower()}"

            zip_file.writestr(image_filename, image_content)

    return zip_buffer.getvalue()


def get_image_content(image):
    image_buffer = io.BytesIO()
    image.save(image_buffer, format=image.format)

    return image_buffer.getvalue()


def generate_accessible_interviews(album):
    interviews = album.interviews.all()
    qr_position = album.qr_position

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        images = list(executor.map(
            partial(generate_accessible_interview, qr_position),
            interviews
        ))

    return images


def generate_accessible_interview(qr_position, interview):
    thubmnail_image = get_thumbnail_image(interview)
    qr_image = generate_qr_code_image(interview)

    corner_position = calculate_corner_position(
        qr_position,
        main_image=thubmnail_image,
        nested_image=qr_image
    )

    thubmnail_image.paste(qr_image, box=corner_position)

    return thubmnail_image


def get_thumbnail_image(interview):
    thumbnail = interview.youtube_video.thumbnail

    response = requests.get(thumbnail)
    image_data = response.content

    return Image.open(io.BytesIO(image_data))


def generate_qr_code_image(interview):
    youtube_url = interview.youtube_video.url

    qr = pyqrcode.create(youtube_url)
    qr_filename = DATA_DIR / f"{interview.name}.png"

    qr.png(qr_filename, scale=QR_SCALE)

    return Image.open(qr_filename)


def calculate_corner_position(album_position, main_image, nested_image):
    top, left = 0, 0
    bottom = main_image.height - nested_image.height
    right = main_image.width - nested_image.width

    POSITIONS = {
        Album.Corner.TOP_LEFT: (left, top),
        Album.Corner.TOP_RIGHT: (right, top),
        Album.Corner.BOTTOM_LEFT: (left, bottom),
        Album.Corner.BOTTOM_RIGHT: (right, bottom),
    }

    return POSITIONS[album_position]
