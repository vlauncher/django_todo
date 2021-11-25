from django.urls import path
from pages.views import HomepageView,LogoutView

urlpatterns = [
    path('',HomepageView.as_view(),name='home'),
    path('logout/',LogoutView.as_view(),name='logout')
]