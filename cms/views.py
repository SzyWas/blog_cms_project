from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, RedirectView, UpdateView, DeleteView, ListView


class ContentManagementView(LoginRequiredMixin, TemplateView):
    template_name = 'cms/cms.html'


class LogoutView(RedirectView):
    url = '/login/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class ObjectDeleteView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('cms')
    template_name = 'cms/object/object_delete.html'


class ObjectCreateView(LoginRequiredMixin, CreateView):
    fields = [
        'name',
        'description',
    ]
    success_url = reverse_lazy('cms')
    template_name = 'cms/object/object_create.html'


class ObjectEditView(ObjectCreateView, UpdateView):
    template_name = 'cms/object/object_edit.html'


















