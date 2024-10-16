from django.urls import path
from .views import BanqueListView

urlpatterns = [
    path('', BanqueListView.as_view(), name='banque-list'),
    path('list/', BanqueListView.as_view(), name='banque-list'),
]