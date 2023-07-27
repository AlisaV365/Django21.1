from django.core.management import BaseCommand, call_command

from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Fill database with new data'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        call_command('loaddata', 'fixture.json')

