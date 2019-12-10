from django.urls import path
from DBStorage.views import ParticipantView, CollectionAnswersView, GiftAnswersView, GiftParticipantView, StorageSettingsView

urlpatterns = [
    path('Storage/', StorageSettingsView.as_view(), name='storagesettingsview'),

    path('Collection/<str:caID>', CollectionAnswersView.as_view(), name='collectionanswersview'),
    path('Collection/', CollectionAnswersView.as_view(), name='collectionanswersview'),

    path('Participants/<str:pID>', ParticipantView.as_view(), name='participantview'),
    path('Participants/', ParticipantView.as_view(), name='participantview'),

    path('Gift/Answers/<str:pfID>', GiftAnswersView.as_view(), name='giftanswersview'),
    path('Gift/Answers/', GiftAnswersView.as_view(), name='giftanswersview'),

    path('Gift/Participants/<str:pfID>', GiftParticipantView.as_view(), name='giftparticipantview'),
    path('Gift/Participants/', GiftParticipantView.as_view(), name='giftparticipantview'),
]