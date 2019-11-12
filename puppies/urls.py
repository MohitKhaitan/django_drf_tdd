from django.conf.urls import url
from .views import Puppy, Puppies

urlpatterns = [
    url(r'^api/v1/puppies/(?P<pk>[0-9]+)$', Puppy.as_view(), name='puppy'),
    url(r'^api/v1/puppies/$', Puppies.as_view(), name='puppies')
]