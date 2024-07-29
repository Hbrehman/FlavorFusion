"""
URL mappings for the user API
"""

from django.urls import path
from user import views

# this name will be used in reverse mapping to get the URL like this reverse('user:create')
app_name = 'user'


urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name="create"),
    path('token/', views.CreateTokenView.as_view(), name="token"),
    path('me/', views.ManageUserView.as_view(), name='me'),
]
