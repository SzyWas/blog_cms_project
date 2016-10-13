from category.models import Category

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView


class CategoryContentManagementView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'cms/category/category_cms.html'
