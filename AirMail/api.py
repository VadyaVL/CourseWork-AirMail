from models import Dialogue
from serializers import DialogueSerializer

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

class DialogueList(APIView):
    def get(self, request, format=None):
        dialogue = Dialogue.objects.all()
        serialized_dialogue = DialogueSerializer(dialogue, many=True)
        return Response(serialized_dialogue.data)

class DialogueDetail(APIView):

    def get_object(selfself, pk):
        try:
            return Dialogue.objects.get(pk=pk)
        except Dialogue.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dialogue = self.get_object(pk)
        serialized_dialogue = DialogueSerializer(dialogue)
        return Response(serialized_dialogue.data)

