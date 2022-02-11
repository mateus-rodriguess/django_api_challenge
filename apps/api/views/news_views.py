from apps.api.serializers import news_serializers
from apps.news.models import Category, Articles, Author
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class ArticlesListView(generics.ListAPIView):
    
   queryset = Articles.objects.all()
   serializer_class = news_serializers.ArticlesSerializers


class ArticlesDetailView(generics.RetrieveAPIView):
    
   queryset = Articles.objects.all()
   serializer_class = news_serializers.ArticlesSerializers


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
   queryset = Articles.objects.all()
   serializer_class = news_serializers.CategoryListSerializers


class CategoryView(generics.RetrieveAPIView):
    queryset = Articles.objects.all()
    serializer_class = news_serializers.CategorySerializers


class ArticlesCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Articles.objects.all()
    serializer_class = news_serializers.CategoryCreateSerializers


class ArticlesUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Articles.objects.all()
    serializer_class = news_serializers.CategoryUpdateSerializers

class ArticlesDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Articles.objects.all()
    serializer_class = news_serializers.CategoryDeleteSerializers
