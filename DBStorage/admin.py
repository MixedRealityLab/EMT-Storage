from django.contrib import admin
from .models import Participant, CollectionAnswer, GiftAnswers, GiftParticipant, StorageSettings

admin.site.register(Participant)
admin.site.register(CollectionAnswer)
admin.site.register(GiftAnswers)
admin.site.register(GiftParticipant)
admin.site.register(StorageSettings)