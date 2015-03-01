from models import Dialogue
from rest_framework import serializers


class DialogueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dialogue
        fields = (
            #'url',
            'id',
            'Established',
            'CountMess',
        )