from comment.models import Comment
from django import template

register = template.Library()


@register.inclusion_tag('cms/template_tags/comments.html')
def comments_tag(pk):
    comments = Comment.objects.filter(post_id=pk)
    return {
        'comments': comments,
    }
