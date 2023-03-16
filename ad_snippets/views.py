from django.http import Http404
from django.utils import timezone

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,viewsets

from ad_snippets.models import Snippet,Tag
from ad_snippets.serializers import SnippetSerializer,TagListSerializer,TagDetailSerializer

class SnippetOverview(APIView):
    """
    List all snippets, or create a new snippet, or delete selected snippets
    """
    serializer_class = SnippetSerializer
    model = Snippet

    def get_queryset(self):
        return self.model.objects.all()

    def get_context(self):
        return {
            'request' : self.request
        }

    def get(self, request, format=None):
        snippets = self.get_queryset()
        serializer = self.serializer_class(snippets, many=True,context=self.get_context())
        response_data = {
            'snippets' : serializer.data,
            'total_snippets' : len(serializer.data)
        }
        return Response(response_data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data,context=self.get_context())
        if serializer.is_valid():
            serializer.save(created_by=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,format=None):
        snippets = self.get_queryset()
        snippets.filter(pk__in=request.data['snippet_ids']).delete()
        serializer = self.serializer_class(snippets, many=True,context=self.get_context())
        return Response(serializer.data)

class SnippetDetailView(APIView):
    """
    Detail, Update, Delete Snippets API endpoint. Takes "pk" in kwargs to identify the snippet.
    """
    serializer_class = SnippetSerializer
    model = Snippet

    def get_context(self):
        return {
            'request' : self.request
        }

    def get_queryset(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snip = self.get_queryset(pk)
        serializer = self.serializer_class(snip,context=self.get_context())
        data = serializer.data
        response_data = {
            'title' : data['title'],
            'content' : data['short_text'],
            'created_at' : data['created_at']
        }
        return Response(response_data)

    def put(self, request, pk, format=None):
        snip = self.get_queryset(pk)
        serializer = self.serializer_class(snip, data=request.data,context=self.get_context())
        if serializer.is_valid():
            serializer.save(updated_at=timezone.now())
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TagListViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Tag Viewset. API to list tags and API to return snippets linked to the selected tag.
    """
    serializer_class = TagListSerializer
    serializer_action_classes = {
        'list': TagListSerializer,
        'retrieve': TagDetailSerializer,
    }

    def get_queryset(self):
        return Tag.objects.all()

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super(TagListViewSet, self).get_serializer_class()