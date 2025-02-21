from django.core.management import BaseCommand

from radioVirgen.models import MetodoPago


class Command(BaseCommand):
    hel='Listado de los métodos de pago'

    def add_arguments(self, parser):
        parser.add_argument(
            '--idUsuario',
            type=str,
            help='Introduce el método de pago',
            required=False
        )

    def handle(self, *args, **kwargs):
        idUsuario = kwargs.get('idUsuario')

        try:
            mets = MetodoPago.objects.filter(usuario=idUsuario).values('usuario')

            if not mets.exists():
                self.stdout.write(self.style.WARNING('No tenemos usuarios con dicho id'))
            else:
                for i in mets:
                    self.stdout.write(self.style.SUCCESS(f'metodo: {i}'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))





