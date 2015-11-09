from datetime import datetime
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from github import GitHub
from gmi.django.scooper.models import Treasure
from hashlib import sha256
import sys


class Command(BaseCommand):
    help = 'fetch new data from the specified scooping source'

    def add_arguments(self, parser):
        parser.add_argument(
            'source', help='source as configured in settings.py')

    def handle(self, *args, **options):
        try:
            raw_source = settings.SCOOPER[options['source']]
            source = dict(
                [(name.lower(), val) for name, val in raw_source.items()])
        except KeyError as err:
            raise CommandError(
                'scooping source \'{}\' not defined in settings.py'.format(
                    err.args[0]))

        scooper = Scooper.create(**source)
        treasures = scooper.scoop()
        for treasure in treasures:
            t = Treasure(**treasure)
            t.save()


class Scooper(object):

    def create(**kwargs):
        type = kwargs['type']
        handler = getattr(sys.modules[__name__], '{}Scooper'.format(type))
        return handler(**kwargs)

    create = staticmethod(create)


class GitHubScooper(object):

    def __init__(self, type='GitHub', user=None, token=None):
        self.user = user
        self.gh = GitHub(access_token=token)

    def scoop(self):
        result = []
        events = self.gh.users(self.user).events.public.get()
        for event in events:
            hash = sha256()
            hash.update(event['id'].encode())

            result.append(dict(
                checksum=hash.hexdigest(),
                headline='{} event to repo {}'.format(
                    event['type'],
                    event['repo']['name']),
                content='contentfoo',
                pub_date=datetime.strptime(
                    event['created_at'], '%Y-%m-%dT%H:%M:%SZ')))

        return result
