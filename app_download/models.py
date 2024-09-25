# models.py
from django.db import models

class FileUpload(models.Model):
    file = models.FileField(upload_to='uploaded_chunks/')
    chunk_index = models.IntegerField()  # Индекс части файла
    upload_id = models.CharField(max_length=255)  # Идентификатор для сборки
    created_at = models.DateTimeField(auto_now_add=True)
