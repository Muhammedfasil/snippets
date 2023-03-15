from rest_framework import generics
from rest_framework.response import Response

from ad_snippets.models import Snippet
from ad_snippets.serializers import SnippetSerializer

class SnippetOverview(generics.ListCreateAPIView):
    """
    Using generic views to achieve the following,
    1. Return total number of snippet and list all available snippets with a hyperlink to respective detail APIs.
    2. collecting the snippet information and save the data to DB.
    """

    serializer_class = SnippetSerializer

    def get_queryset(self):
        return Snippet.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        response_data = {
            'snippets' : serializer.data,
            'total_snippets' : len(serializer.data)
        }
        return Response(response_data)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)



