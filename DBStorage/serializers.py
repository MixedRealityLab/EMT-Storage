from rest_framework import serializers
from .models import Participant, CollectionAnswer, GiftAnswers, GiftParticipant, StorageSettings

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'

class CollectionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionAnswer
        fields = '__all__'

class GiftParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = GiftParticipant
        fields = '__all__'

class GiftAnswersSerializer(serializers.ModelSerializer):

    class Meta:
        model = GiftAnswers
        fields = ('modID', 'parID', 'giftWord', 'giftFree', 'giftArou', 'giftVael')
        #('modID', 'parID', 'giftWord', 'giftFree', 'giftArou', 'giftVael')

class StorageSettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = StorageSettings
        fields = '__all__'