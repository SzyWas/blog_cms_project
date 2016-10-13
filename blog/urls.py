from blog.views import PostEntriesListView, PostEntryDetailView
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from cms.views import LogoutView

urlpatterns = [
    url(r'^$', PostEntriesListView.as_view(), name='blog'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^page/(?P<page>[0-9]+)/$', PostEntriesListView.as_view(), name='blog-page'),
    url(r'^(?P<slug>[\w-]+)/(?P<pk>[0-9]+)/$', PostEntryDetailView.as_view(), name='post-detail'),
]
