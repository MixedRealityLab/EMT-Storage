from django.urls import path
from DBCalls.views import CollectionView, ExhibitView, ModuleView, QuestionView

urlpatterns = [
    path('Questions/<str:qID>', QuestionView.as_view(), name='questionview'),
    path('Questions/', QuestionView.as_view(), name='questionview'),
    path('Modules/<str:mID>', ModuleView.as_view(), name='moduleview'),
    path('Modules/', ModuleView.as_view(), name='moduleview'),
    path('Exhibits/<str:eID>', ExhibitView.as_view(), name='exhibitview'),
    path('Exhibits/', ExhibitView.as_view(), name='exhibitview'),
    path('<str:cID>/', CollectionView.as_view(), name='collectionview'),
    path('', CollectionView.as_view(), name='collectionview')
]