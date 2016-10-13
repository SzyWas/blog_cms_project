import datetime

from category.models import Category
from django.db import models
from django.template.defaultfilters import slugify


class PostAuthor(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=True)
    email = models.EmailField()
    description = models.TextField()
    slug = models.SlugField(unique=True, editable=False)

    class Meta:
        verbose_name_plural = 'Post Authors'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name.replace(" ", "-"))
        super(PostAuthor, self).save(*args, **kwargs)

    def get_class_name(self):
        return self.__class__.__name__

class PostEntry(models.Model):

    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(PostAuthor)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=256)
    content = models.TextField()
    height = models.IntegerField(default=400, null=True)
    width = models.IntegerField(default=750, null=True)
    image = models.ImageField(
        upload_to='post_entry/', null=True, blank=True,
        width_field="width", height_field="height",
    )
    views = models.IntegerField(default=0)
    draft = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, editable=False)
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True, null=True)
    last_update_date = models.DateTimeField(auto_now_add=False, null=True)

    class Meta:
        verbose_name_plural = 'Post Entries'

    def __str__(self):
        return "%s - %s" % (self.title, self.author)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title.replace(" ", "-"))
        if self.draft:
            self.published_date = datetime.datetime.now()
        elif self.draft and self.save():
            self.last_update_date = datetime.datetime.now()

        super(PostEntry, self).save(*args, **kwargs)

