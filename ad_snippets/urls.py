from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ad_snippets.views import SnippetOverview

urlpatterns = [
    path('snippets/', SnippetOverview.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)