from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Modificar el método de pago'

    def add_arguments(self, parser):
        parser.add_argument(

        )
        parser.add_argument(

        )

    def handle(self, *args, **kwargs):
        car = 6