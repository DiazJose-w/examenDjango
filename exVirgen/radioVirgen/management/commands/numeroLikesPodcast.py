from django.core.management import BaseCommand

from radioVirgen.models import Podcast, LikePodcast


class Command(BaseCommand):
    help = 'Número de likes que tiene el podcast'

    def add_arguments(self, parser):
        parser.add_argument(
            '--nombre',
            type=str,
            help='Dime el nombre del podcast',
            required=False
        )

    def handle(self, *args, **kwargs):
        nombrePodcast = kwargs.get('nombre')
        try:
            idP = Podcast.objects.filter(nombre=nombrePodcast).first().id
            if not idP.exists():
                self.stdout.write(self.style.SUCCESS(f'El podcast {idP} no existe'))
            else:
                numLikes = LikePodcast.objects.filter(podcast=idP)
                self.stdout.write(self.style.SUCCESS(f'El podcast {nombrePodcast} tiene'))
                self.stdout.write(self.style.SUCCESS(f'un total de {numLikes.count()} likes'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))

