
from django.conf.urls import url
from django.contrib import admin
from info.views import IndexView, ResumeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^resume/$', ResumeView.as_view(), name='resume_view')
]
