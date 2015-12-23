from django.conf.urls import url
from contact.views import contact, resume


urlpatterns = [
    url(r'^$', contact, name="contact"),
    url(r'^resume/$', resume, name="resume"),
]
