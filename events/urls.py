from django.urls import path

from . import views

app_name = 'events'

urlpatterns = [
    path('create/', views.EventCreate.as_view(), name='create'),
    path('<int:pk>/edit/', views.EventUpdate.as_view(), name='update'),
    path('<int:pk>/signup/', views.sign_up, name='sign-up'),
    path('<int:pk>/withdraw/', views.withdraw, name='withdraw'),
    path('<int:pk>/', views.EventDetail.as_view(), name='detail'),
    path('', views.EventList.as_view(), name='list'),
]
