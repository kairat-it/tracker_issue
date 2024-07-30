from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Issue
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
    template_name = 'tracker/issue_form.html'
    success_url = reverse_lazy('issue_list')


class IssueUpdateView(LoginRequiredMixin, UpdateView):
    model = Issue
    form_class = IssueForm
    template_name = 'tracker/issue_form.html'
    success_url = reverse_lazy('issue_list')


class IssueDeleteView(LoginRequiredMixin, DeleteView):
    model = Issue
    template_name = 'tracker/issue_confirm_delete.html'
    success_url = reverse_lazy('issue_list')
