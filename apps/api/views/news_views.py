from unicodedata import category, name
from apps.api.serializers import news_serializers
from apps.news.models import Category, Articles, Author
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
class ArticlesListView(generics.ListAPIView):
    
    queryset = Articles.objects.all()
    serializer_class = news_serializers.ArticlesSerializers


class ArticlesListCategoryView(generics.ListAPIView):

    serializer_class = news_serializers.ArticlesSerializers
    # category_slug = "category_slug"
    def get_queryset(self):
        category_name = self.request.query_params.get('category')
        
        category = Category.objects.get(name="festa")
      
        queryset = Articles.objects.filter(category=category)
        
        return queryset


class ArticlesDetailView(generics.RetrieveAPIView):

    # queryset = Articles.objects.all()
    serializer_class = news_serializers.ArticlesSerializers
    
   
    def get_queryset(self, request, *args, **kwargs):
        queryset = Articles.objects.all()
        return queryset
    

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


class CategoryCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
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
