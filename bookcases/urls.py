
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.bookcase_list, name="bookcase_list"),
    url(r'^(?P<id>\d+)/$', views.bookcase_detail, name="bookcase_detail"),
    url(r'^bookshelf/(?P<id>\d+)/$', views.bookshelf_detail, name="bookshelf_detail"),
>>>>>>> 79363db975d0e3a4d67075b6377f11b39c597667
]