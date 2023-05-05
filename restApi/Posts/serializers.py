from rest_framework.serializers import ModelSerializer
from .models import Post, Person


class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = ['id','first_name', 'last_name']


class PostSerializer(ModelSerializer):
    person_that_make_it = PersonSerializer()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'draft', 'read_time', 'person_that_make_it', 'updated', 'created']
