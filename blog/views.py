from blog.models import PostEntry, PostAuthor
from comment.forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView
from django.views.generic.edit import FormMixin


class PostEntriesListView(ListView):
    model = PostEntry
    object_list = PostEntry.objects.all()
    context_object_name = 'post_entries'
    paginate_by = 5
    template_name = 'blog/blog.html'
    ordering = '-published_date'


class RecentPostEntriesView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(RecentPostEntriesView, self).get_context_data(**kwargs)
        context['recent_posts'] = PostEntry.objects.all().order_by('-published_date')[:5]
        return context


class LatestPostEntryView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(LatestPostEntryView, self).get_context_data(**kwargs)
        context['latest_post'] = PostEntry.objects.all().filter(draft=True).latest('published_date')
        return context


class PostEntryDetailView(FormMixin, DetailView):
    model = PostEntry
    form_class = CommentForm
    template_name = 'blog/post_entry.html'
    context_object_name = 'post'

    def get_success_url(self):
        return reverse('post-detail', kwargs={'slug': self.object.slug, 'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(PostEntryDetailView, self).get_context_data(**kwargs)
        context['comment_form'] = self.get_form()
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        post_entry = get_object_or_404(PostEntry, id=self.object.pk)
        post_entry.views += 1
        post_entry.save()
        return super(PostEntryDetailView, self).get(post_entry)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        comment_form = self.get_form()
        if comment_form.is_valid():
            return self.form_valid(comment_form)
        else:
            return self.form_invalid(comment_form)

    def form_valid(self, form):
        post_entry = get_object_or_404(PostEntry, id=self.object.pk)
        comment_form = form.save(commit=False)
        comment_form.post_id_id = post_entry.pk
        comment_form.save()
        return super(PostEntryDetailView, self).form_valid(comment_form)


class PostContentManagementView(LoginRequiredMixin, PostEntriesListView):
    template_name = 'cms/post/post_cms.html'
    paginate_by = 0


class PostEntryContentManagementView(LoginRequiredMixin, PostEntryDetailView):
    template_name = 'cms/post/post_entry_cms.html'


class PostEntryCreateView(LoginRequiredMixin, CreateView):
    model = PostEntry
    fields = [
        'author',
        'category',
        'title',
        'content',
        'image',
        'width',
        'height',
        'draft',
    ]
    success_url = '/administration/'
    template_name = 'cms/post/post_entry_create.html'


class PostEntryEditView(PostEntryCreateView, UpdateView):
    template_name = 'cms/post/post_entry_edit.html'


class PostAuthorContentManagementView(LoginRequiredMixin, ListView):
    model = PostAuthor
    template_name = 'cms/author/author_cms.html'