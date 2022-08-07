import os
import csv
import slugify

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # путь для отладки в VSCode
        #filename = os.getcwd() + '\\work_with_database\\' + 'phones.csv' 
        filename = 'phones.csv'
        with open(filename, 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            aslug = slugify.slugify(phone.get('name'))
            new_phone = Phone(
                name = phone.get('name'), 
                image = phone.get('image'),
                price = phone.get('price'),
                release_date = phone.get('release_date'),
                lte_exists = phone.get('lte_exists'),
                slug = aslug
            )
            new_phone.save()

