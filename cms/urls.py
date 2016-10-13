from django.conf.urls import url
from blog.models import PostAuthor, PostEntry
from category.models import Category

from blog.views import PostEntryContentManagementView, PostContentManagementView, \
    PostEntryCreateView, PostEntryEditView, PostAuthorContentManagementView
from cms.views import  ObjectCreateView, ObjectEditView, ContentManagementView, ObjectDeleteView
from category.views import CategoryContentManagementView

urlpatterns = [

    url(r'^$', ContentManagementView.as_view(), name='cms'),
    url(r'^post-list/', PostContentManagementView.as_view(), name='post-list'),
    url(r'^post/(?P<slug>[\w-]+)/(?P<pk>[0-9]+)/', PostEntryContentManagementView.as_view(), name='post-cms'),
    url(r'^post-create/', PostEntryCreateView.as_view(), name='post-create'),
    url(r'^post-edit/(?P<slug>[\w-]+)/(?P<pk>[0-9]+)/', PostEntryEditView.as_view(), name='post-edit'),
    url(r'^post-delete/(?P<pk>[0-9]+)/', ObjectDeleteView.as_view(model=PostEntry), name='post-delete'),

    url(r'^category-list/', CategoryContentManagementView.as_view(model=Category, context_object_name='category'), name='category-list'),
    url(r'^category-create/', ObjectCreateView.as_view(model=Category), name='category-create'),
    url(r'^category-edit/(?P<slug>[\w-]+)/(?P<pk>[0-9]+)/', ObjectEditView.as_view(model=Category), name='category-edit'),
    url(r'^category-delete/(?P<pk>[0-9]+)/', ObjectDeleteView.as_view(model=Category), name='category-delete'),

    url(r'^authors-list/', PostAuthorContentManagementView.as_view(model=PostAuthor, context_object_name='category'), name='authors-list'),
    url(r'^author-create/', ObjectCreateView.as_view(model=PostAuthor), name='author-create'),
    url(r'^author-edit/(?P<slug>[\w-]+)/(?P<pk>[0-9]+)/', ObjectEditView.as_view(model=PostAuthor), name='author-edit'),
    url(r'^author-delete/(?P<pk>[0-9]+)/', ObjectDeleteView.as_view(model=PostAuthor), name='author-delete'),

]
