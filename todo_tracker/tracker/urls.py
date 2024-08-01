from django.urls import path
from .views import IssueListView, IssueDetailView, IssueCreateView, IssueUpdateView, IssueDeleteView, ProjectListView, \
    ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project/add/', ProjectCreateView.as_view(), name='project_add'),
    path('project/<int:pk>/edit/', ProjectUpdateView.as_view(), name='project_edit'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('project/<int:pk>/issue/add/', IssueCreateView.as_view(), name='issue_add'),
    path('issues', IssueListView.as_view(), name='issue_list'),
    path('issue/<int:pk>/', IssueDetailView.as_view(), name='issue_detail'),
    path('issue/add/', IssueCreateView.as_view(), name='issue_add'),
    path('issue/<int:pk>/edit/', IssueUpdateView.as_view(), name='issue_edit'),
    path('issue/<int:pk>/delete/', IssueDeleteView.as_view(), name='issue_delete'),
]

