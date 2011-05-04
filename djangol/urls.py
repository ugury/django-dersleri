from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
   url(r'^admin/', include(admin.site.urls)),
   url(r'^lesson/(\d+)/([-\w]+)/','lessons.views.get_lesson'),
   url(r'^home/','lessons.views.get_lessons'),
)