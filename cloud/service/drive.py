import mimetypes
import io

from googleapiclient.discovery import MediaFileUpload
from googleapiclient.http import MediaIoBaseDownload

from cloud.service import BaseService
import config


class DriveService(BaseService):
    def __init__(self, *args, **kwargs):
        self.service_name = 'drive'
        self.api_version = 'v3'
        super().__init__(*args, **kwargs)

    def create_doc(self, name, folder_id):
        file_metadata = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.document',
            'parents': [folder_id]
        }
        doc = self.service.files().create(body=file_metadata,
                                          fields='id').execute()
        return doc.get('id')

    def upload_file(self, file_path, file_name, folder_id):
        metadata = {'name': file_name, 'parents': [folder_id]}
        mimetype = mimetypes.MimeTypes().guess_type(file_path)[0]
        media = MediaFileUpload(file_path, mimetype=mimetype)
        drive_file = self.service.files().create(body=metadata, media_body=media, fields='id').execute()
        return drive_file.get('id')

    def download_file(self, file_id):
        request = self.service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
        return fh

    def create_folder(self, name, folder_id=config.root_folder):
        metadata = {
            'name': name,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [folder_id]
        }
        folder = self.service.files().create(body=metadata,
                                             fields='id').execute()
        return folder.get('id')
