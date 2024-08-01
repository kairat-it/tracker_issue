from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse
from .models import Issue, Project
from .forms import IssueForm


class IssueListView(ListView):
    model = Issue
    template_name = 'tracker/issue_list.html'
    context_object_name = 'issues'
    paginate_by = 3


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-created_at')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(summary__icontains=query)
        return queryset




class IssueDetailView(DetailView):
    model = Issue
    template_name = 'tracker/issue_detail.html'
    context_object_name = 'issue'


class IssueCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    form_class = IssueForm
    template_name = 'tracker/issues/issue_form.html'
    fields = ['summary', 'description', 'status', 'types']

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        form.instance.project = project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.kwargs['pk']})


class IssueUpdateView(LoginRequiredMixin, UpdateView):
    model = Issue
    form_class = IssueForm
    template_name = 'tracker/issue_form.html'
    success_url = reverse_lazy('issue_list')


class IssueDeleteView(LoginRequiredMixin, DeleteView):
    model = Issue
    template_name = 'tracker/issue_confirm_delete.html'
    success_url = reverse_lazy('issue_list')


class ProjectListView(ListView):
    model = Project
    template_name = 'tracker/projects/project_list.html'
    context_object_name = 'projects'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(name__icontains=query) | queryset.filter(description__icontains=query)
        return queryset

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'tracker/projects/project_detail.html'
    context_object_name = 'project'

class ProjectCreateView(CreateView):
    model = Project
    template_name = 'tracker/projects/project_form.html'
    fields = ['start_date', 'end_date', 'name', 'description']
    success_url = reverse_lazy('project_list')

class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'tracker/projects/project_form.html'
    fields = ['start_date', 'end_date', 'name', 'description']
    success_url = reverse_lazy('project_list')

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'tracker/projects/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')
