from apps.api.serializers import news_serializers
from apps.news.models import Articles, Author, Category
from rest_framework import viewsets


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = news_serializers.CategorySerializers

class ArticlesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = news_serializers.ArticlesSerializers

class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = news_serializers.AuthorSerializers