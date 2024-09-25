# management/commands/assemble_chunks.py
from django.core.files.storage import default_storage
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Сборка частей файла в один целый файл'

    def add_arguments(self, parser):
        parser.add_argument('upload_id', type=str, help="ID загрузки для сборки")

    def handle(self, *args, **kwargs):
        upload_id = kwargs['upload_id']
        chunk_index = 0
        assembled_file_path = f"/path/to/assembled_files/{upload_id}.vdi"

        with open(assembled_file_path, 'wb') as assembled_file:
            while True:
                chunk_filename = f"uploaded_chunks/{upload_id}_chunk_{chunk_index}"
                if not default_storage.exists(chunk_filename):
                    break
                with default_storage.open(chunk_filename, 'rb') as chunk_file:
                    assembled_file.write(chunk_file.read())
                chunk_index += 1

        self.stdout.write(self.style.SUCCESS(f"Файл {assembled_file_path} успешно собран"))
