from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.welcome,name='Index'),
    url(r'^profile/(\d+)',views.profile,name = 'profile'),
    url(r'^updateProfile',views.updateProfile,name = 'updateProfile'),
    url(r'^new/project$',views.new_project, name='new-project'),
    url(r'^directory/',views.directory, name='directory'),
    url(r'^site/(\d+)',views.site,name='site'),
    url(r'^search',views.search_results,name = 'search'),
    url(r'^api/profile/$', views.ProfileList.as_view(),name='profileApi'),
    url(r'^api/project/$', views.ProjectList.as_view(),name='projectApi')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)