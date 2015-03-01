from models import Dialogue, Information
from rest_framework import serializers

from django.contrib.auth.models import User


class DialogueSerializer(serializers.HyperlinkedModelSerializer):

    Creator_id = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Dialogue.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.Established = validated_data.get('Established', instance.Established)
        instance.CountMess = validated_data.get('CountMess', instance.CountMess)
        #instance.Creator_id = validated_data.get('Creator_id', instance.Creator_id)
        #instance.Receiver_id = validated_data.get('Receiver_id', instance.Receiver_id)
        instance.save()

        return instance

    class Meta:
        model = Dialogue
        fields = (
            #'url',
            'id',
            'Established',
            'CountMess',
            'Creator_id',
            #'Receiver_id',
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):

    #dialogs = serializers.PrimaryKeyRelatedField(many=True, queryset=Dialogue.objects.all())


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        return instance


    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'email',)


class InformationSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        return Information.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.CountDialog = validated_data.get('CountDialog', instance.CountDialog)
        instance.save()

        return instance


    class Meta:
        model = Information
        fields = ('id',
                  'CountDialog',)