from django.urls import path
from .views import ComputersList, ComputersDetail

urlpatterns = [
    path('', ComputersList.as_view(), name='computers_list'),
    path('<int:pk>/', ComputersDetail.as_view(), name='computers_detail'),
]
