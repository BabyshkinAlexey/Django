from typing import Any
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Print 'Htllo world! to output."
    
    def handle(self, *args, **options):
        self.stdout.write('Hello world!')