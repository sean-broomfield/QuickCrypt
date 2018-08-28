from django.conf.urls import url
from tracker import views

urlpatterns = [
    url(r'^$', views.CryptocoinView.as_view(), name="cryptocoin_list"),
    url(r'^reload/$', views.reloadData, name="reload")
]