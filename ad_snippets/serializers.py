from django.utils.encoding import smart_str
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from ad_snippets.models import Snippet,Tag

class CreatableSlugRelatedField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        queryset = self.get_queryset()
        try:
            return queryset.get_or_create(**{self.slug_field: data})[0]
        except ObjectDoesNotExist:
            self.fail('does_not_exist', slug_name=self.slug_field, value=smart_str(data))
        except (TypeError, ValueError):
            self.fail('invalid')

class SnippetSerializer(serializers.ModelSerializer):
    tag = CreatableSlugRelatedField(slug_field='title',queryset=Tag.objects.all())
    created_by = serializers.ReadOnlyField(source='created_by.username')
    hyperlink = serializers.SerializerMethodField()

    class Meta:
        model = Snippet
        fields = ['title','short_text','created_at','updated_at','created_by','tag','hyperlink']

    def get_hyperlink(self,obj):
        # Generating hyper link here
        return '1'
 