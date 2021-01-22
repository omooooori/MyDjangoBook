from django.db import models


class Book(models.Model):
    name = models.CharField('Book name', max_length=255)
    publisher = models.CharField('Publisher', max_length=255, blank=True)
    page = models.IntegerField('Page number', blank=True, default=0)

    def __str__(self):
        return self.name


class Impression(models.Model):
    book = models.ForeignKey(Book,
                             verbose_name='Book name',
                             related_name='impressions',
                             on_delete=models.CASCADE
                             )

    comment = models.TextField('Comment', blank=True)

    def __str__(self):
        return self.comment
