import random
from idlelib.configdialog import changes

from django.core.management import BaseCommand
from faker import Faker
from radioVirgen.models import MetodoPago, Usuario


class Command(BaseCommand):
    help = 'Añadir métodos de pago'

    def handle(self, *args, **kwargs):
        faker = Faker()
        tipos = ['Tarjeta', 'PayPal', 'Transferencia']

        try:
            nombreUsuario = Usuario.objects.filter(PrimaryKey=1).first()

            if not MetodoPago.objects.exists():
                MetodoPago.objects.create(
                    usuario=nombreUsuario,
                    tipo= random.choice(tipos),
                    nombreCompleto=nombreUsuario,
                    email=faker.email(),
                    numeroCuenta=random.randint(1111, 9999)
                )
                self.stdout.write(self.style.SUCCESS('Método añadido con éxito'))
            else:
                self.stdout.write(self.style.WARNING('El método ya paga de esta forma'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))


