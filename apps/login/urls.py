# login/urls.py
from django.urls import path
from .views import CreateTokenView

urlpatterns = [
    path('token/', CreateTokenView.as_view(), name='token_obtain_pair'),
    # Agrega más URLs relacionadas con la autenticación si es necesario
]
