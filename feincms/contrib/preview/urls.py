from django.conf.urls import patterns, url

from feincms.contrib.preview.views import PreviewHandler


urlpatterns = patterns('',
    url(r'^(.*)/_preview/(\d+)/$', PreviewHandler.as_view(),
        name='feincms_preview'),
)
