from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from ad_snippets.views import SnippetOverview,SnippetDetailView,TagListViewSet

router = DefaultRouter()
router.register('tags', TagListViewSet, basename='tag')

urlpatterns = [
    path('snippets/', SnippetOverview.as_view(),name='snippet_overview'),
    path('snippet/<int:pk>/', SnippetDetailView.as_view(),name='snippet_details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += router.urls