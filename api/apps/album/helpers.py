from zipfile import ZipFile

from PIL import Image
from concurrent.futures import ThreadPoolExecutor
import io
from pathlib import Path
import pyqrcode
import requests


DATA_DIR = Path("/tmp")

QR_SCALE = 4


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

    MAX_THREADS = len(interviews)

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        images = list(executor.map(
            generate_accessible_interview, interviews
        ))

    return images


def generate_accessible_interview(interview):
    thubmnail_image = get_thumbnail_image(interview)
    qr_image = generate_qr_code_image(interview)

    thubmnail_image.paste(qr_image, box=(0, 0))

    return thubmnail_image


def generate_qr_code_image(interview):
    youtube_url = interview.youtube_video.url

    qr = pyqrcode.create(youtube_url)
    qr_filename = DATA_DIR / f"{interview.name}.png"

    qr.png(qr_filename, scale=QR_SCALE)

    return Image.open(qr_filename)


def get_thumbnail_image(interview):
    thumbnail = interview.youtube_video.thumbnail

    response = requests.get(thumbnail)
    image_data = response.content

    return Image.open(io.BytesIO(image_data))
