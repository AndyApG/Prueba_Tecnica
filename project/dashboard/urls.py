from django.urls import path
from dashboard.views import LoadView, ContratoView, LogoutView, LoginEmailView, RegistroView

urlpatterns = [
    path('', LoginEmailView.as_view(), name='main'),
    path('login/', LoginEmailView.as_view(), name='login'),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('load/', LoadView.as_view(),name='load'),
    path('datos/',ContratoView.as_view(),name='datos'),
    path('logout/', LogoutView.as_view(), name='logout')
]

