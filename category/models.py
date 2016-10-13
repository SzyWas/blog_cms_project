from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.TextField()
    slug = models.SlugField(unique=True, editable=False)

    class Meta:
        ordering = ['-name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return u'%s' % self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name.replace(" ", "-"))
        super(Category, self).save(*args, **kwargs)

    def get_class_name(self):
        return self.__class__.__name__
