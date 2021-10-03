from django.core.management.base import BaseCommand
from ...bot import run

class Command(BaseCommand):
    def handle(self, *args, **options):
        run()