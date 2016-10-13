from blog.models import PostEntry
from comment.models import Comment
from django import template

register = template.Library()


@register.inclusion_tag('template_tags/comments.html')
def comments_tag(pk):
    comments = Comment.objects.filter(post_id=pk)
    return {
        'comments': comments,
    }


@register.inclusion_tag('template_tags/most_viewed_posts.html')
def most_viewed_tag():
    most_viewed_posts = PostEntry.objects.all().order_by('-views')[:5]
    return {
        'most_viewed': most_viewed_posts
    }


@register.inclusion_tag('template_tags/newest_posts.html')
def newest_posts_tag():
    newest_posts = PostEntry.objects.all().order_by('-published_date')[:5]
    return {
        'newest_posts': newest_posts,
    }


@register.filter
def class_name(value):
    return value.__class__.__name__