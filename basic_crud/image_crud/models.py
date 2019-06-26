from django.db import models
from django.contrib.auth.models import User
from PIL import Image



class Image_CRUD(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to="image_crud")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
