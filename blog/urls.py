from django.conf.urls import url
from blog.views import post_list, post_detail

urlpatterns = [
    url(r'^$', post_list, name="overview"),
    url(r'^(?P<slug>.*)/$', post_detail, name="detail")
]
