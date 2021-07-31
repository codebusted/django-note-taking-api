from rest_framework import serializers

from .models import Notes

class NotesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notes
        fields = ('id','title', 'content', 'created_at', 'modified_at')