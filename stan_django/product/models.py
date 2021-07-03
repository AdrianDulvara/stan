from io import BytesIO
from PIL import Image

from django.db import models
from django.core.files import File


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}'


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    detail_image = models.ImageField(upload_to='uploads/',
                                     blank=True,
                                     null=True)
    menu_image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added', )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url

        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def get_detail_image(self):
        if self.detail_image:
            return 'http://127.0.0.1:8000' + self.detail_image.url
        else:
            if self.image:
                self.detail_image = self.make_detail_image(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.detail_image.url
            else:
                return ''

    def get_menu_image(self):
        if self.menu_image:
            return 'http://127.0.0.1:8000' + self.menu_image.url
        else:
            if self.image:
                self.menu_image = self.make_menu_image(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.menu_image.url
            else:
                return ''

    def make_thumbnail(self, image, size=(200, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

    def make_detail_image(self, image, size=(70, 70)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        detail_image = File(thumb_io, name=image.name)

        return detail_image

    def make_menu_image(self, image, size=(100, 100)):
        img = Image.open(image)
        img.convert('RGB')
        img.menu_image(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        menu_image = File(thumb_io, name=image.name)

        return menu_image