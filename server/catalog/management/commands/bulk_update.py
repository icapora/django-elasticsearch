from django.core.management.base import BaseCommand

from elasticsearch_dsl import connections
from elasticsearch.helpers import bulk

from catalog.constants import ES_INDEX
from catalog.models import Wine


class Command(BaseCommand):
    help = 'Updates the Elasticsearch index.'

    def _document_generator(self):
        for wine in Wine.objects.iterator():
            yield {
                '_index': ES_INDEX,
                '_id': wine.id,
                'variety': wine.variety,
                'country': wine.country,
                'price': wine.price,
                'winery': wine.winery,
                'description': wine.description,
                'points': wine.points,
            }

    def handle(self, *args, **kwargs):
        self.stdout.write(f'Bulk updating documents on "{ES_INDEX}" index...')
        connection = connections.get_connection()
        succeeded, _ = bulk(connection, actions=self._document_generator(), stats_only=True)
        self.stdout.write(f'Updated {succeeded} documents on "{ES_INDEX}" successfully')
