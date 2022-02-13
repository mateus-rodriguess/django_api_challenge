from unicodedata import category, name
from urllib import response
from apps.api.serializers import news_serializers
from apps.news.models import Category, Articles, Author
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from itertools import groupby

class ArticlesListView(generics.ListAPIView):

    serializer_class = news_serializers.ArticlesListSerializers

    def get_queryset(self):
        """
        get_queryset
        """
        category_name = self.request.query_params.get('category')
        if not category_name:
            queryset = Articles.objects.all()
            return queryset
        try:
            category = Category.objects.get(name=category_name)
            queryset = Articles.objects.filter(category=category)
            return queryset
        except:
            queryset = []
            return queryset


class ArticlesDetailView(generics.RetrieveAPIView):
    serializer_class = news_serializers.ArticlesSerializers
    queryset = Articles.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        summary =  serializer.data["summary"]
        paragraphs = summary.split('.')
        data = serializer.data
        data["firstParagraph"] = f"<p>{paragraphs[0]}</p>"
        data["category"] = serializer.data["category"]["name"]

        if not request.user.is_authenticated:
            return Response(data)
        else:
            text = ""
            for paragraph in paragraphs:
                text += f"<p>{paragraph}</p>"
            data["body"] = f"<div>{text}</div>"
            return Response(data)


class ArticlesCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Articles.objects.all()
    serializer_class = news_serializers.ArticlesCreateSerializers


class ArticlesDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Articles.objects.all()
    serializer_class = news_serializers.ArticlesDeleteSerializers


class ArticlesUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Articles.objects.all()
    serializer_class = news_serializers.ArticlesUpdateSerializers


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = news_serializers.CategoryListSerializers


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = news_serializers.CategorySerializers

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class CategoryCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = news_serializers.CategoryCreateSerializers


class CategoryUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = news_serializers.CategoryUpdateSerializers


class CategoryDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = news_serializers.CategoryDeleteSerializers


class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = news_serializers.AuthorListSerializers

class AuthorCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Author.objects.all()
    serializer_class = news_serializers.AuthorCreateSerializers


class AuthorUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Author.objects.all()
    serializer_class = news_serializers.ArticlesUpdateSerializers


class AuthorDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Author.objects.all()
   
    serializer_class = news_serializers.AuthorDeleteSerializers

class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = news_serializers.AuthorSerializers