from django.conf.urls import url,
from laamar.views import home,contact

urlpatterns=[
    url(r'^$',home,name="home"),
    url(r'^contact/$',contact,name="contact")
]