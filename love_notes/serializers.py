from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    note_url = serializers.ModelSerializer.serializer_url_field(view_name='note_detail')

    class Meta:
       model = Note
       fields = ('id', 'body', 'time_stamp', 'note_url')