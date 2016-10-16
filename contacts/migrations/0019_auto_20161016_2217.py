# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-16 22:17
from __future__ import unicode_literals

from django.db import migrations


def set_book_owner(apps, schema_editor):
    Book = apps.get_model("contacts", "Book")
    BookOwner = apps.get_model("contacts", "BookOwner")
    for book in Book.objects.all():
        if not book.owner:
            owners = BookOwner.objects.filter(book=book)
            if owners:
                book.owner = BookOwner.objects.filter(book=book)[0].user
                book.save()


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0018_auto_20161016_2214'),
    ]

    operations = [
        migrations.RunPython(set_book_owner)
    ]
