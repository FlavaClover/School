from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Reload data base'

    def handle(self, *args, **options):
        print('Hello')