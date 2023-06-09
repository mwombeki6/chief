from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from custom.models import User
from innovation.models import Innovation
from research.models import Research
from publication.models import Publication

@registry.register_document
class UserDocument(Document):
    class Index: 
        name = 'user'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username'
        ]          