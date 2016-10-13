from comment.models import Comment
from blog.models import PostEntry
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


class ApprovedCommentView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = [
        'approved',
    ]
    success_url = reverse_lazy('cms')
    template_name = 'cms/object/object_edit.html'


class CommentEditView(ApprovedCommentView):
    fields = [
        'approved',
        'content',
        'author',
        'email',
    ]
