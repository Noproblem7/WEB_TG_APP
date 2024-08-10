import uuid


class SaveMediaFiles(object):
    def song_image_save(self, file_name):
        image_path = file_name.split('.')[-1]
        return f' http://localhost:8000/{uuid.uuid4()}.{image_path})'
