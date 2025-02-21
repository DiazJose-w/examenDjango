from django.core.management import BaseCommand
from httpx import delete

from radioVirgen.models import Usuario, LikePodcast


class Command(BaseCommand):
    help='Likes de un usuario'

    def add_arguments(self, parser):
        parser.add_argument(
            '--nick',
            type=str,
            help= 'Likes del usuario',
            required=False
        )

    def handle(self, *args, **kwargs):
        nick= kwargs.get('nick')
        try:
            idUsuario = Usuario.objects.filter(nick=nick).first().id
            listaLikes = LikePodcast.objects.filter(usuario=idUsuario)
            self.stdout.write(self.style.SUCCESS(f'Al usuario {nick} le gustan '))
            for i in listaLikes:
                self.stdout.write(self.style.SUCCESS(f': {i.podcast}'))

            self.stdout.write(self.style.SUCCESS(f'Suman una cantidad de {listaLikes.count()} podcast'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))