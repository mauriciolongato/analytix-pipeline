from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^registroheader/', views.registroheader_list),
    url(r'^registrodetalhe/', views.registrodetalhe_list),
    url(r'^truncatetables/', views.truncate_tables),
]
