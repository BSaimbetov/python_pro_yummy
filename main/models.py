from django.db import models

# Create your models here.


class DishCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    image = models.ImageField(upload_to='events')
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Staff(models.Model):
    name = models.CharField(max_length=255, unique=True)
    position = models.CharField(max_length=255, unique=True)
    biography = models.TextField()
    image = models.ImageField(upload_to='staff')
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    caption = models.TextField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.caption if self.caption else "Gallery Image"
