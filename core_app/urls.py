from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("producten/", views.producten, name="producten"),
    path('submit-footer-vragen/', views.footer_vragen_form_submit, name='footer_vragen_form_submit'),
]