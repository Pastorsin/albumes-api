from rest_framework import renderers


class ZipRenderer(renderers.BaseRenderer):
    media_type = 'application/zip'
    file_format = 'zip'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data
