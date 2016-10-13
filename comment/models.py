from blog.models import PostEntry
from django.db import models


class Comment(models.Model):
    post_id = models.ForeignKey(PostEntry)
    id = models.AutoField(primary_key=True)
    content = models.TextField(max_length=1000)
    author = models.CharField(max_length=64)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Comments'
        ordering = ['-date']

    def __str__(self):
        return u'%s' % self.content
