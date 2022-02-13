from rest_framework import serializers, status
from rest_framework.mixins import DestroyModelMixin
from rest_framework.response import Response

from apps.news.models import Articles, Category, Author

class CategorySerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ["id", "name"]

class CategoryCreateSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ["id", "name"]
    def create(self, validated_data):
        return super().create(validated_data)


class CategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class CategoryUpdateSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ["id", "name"]

    def update(self, instance, validated_data):
    
        return super().update(instance, validated_data)


class CategoryDeleteSerializers(serializers.ModelSerializer, DestroyModelMixin):
 
    class Meta:
        model = Category
        fields = ["id", "name"]
        
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class AuthorSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = ["id", "name", "picture"]

class AuthorListSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = ["id", "name", "picture"]

class AuthorCreateSerializers(serializers.ModelSerializer):
   
    class Meta:
        model = Author
        fields = ["id","name", "user", "picture"]
    
    def create(self, validated_data):

        if not Author.objects.filter(user=self.data["user"]).exists():
            return super().create(validated_data)
        data = {"message": "An author is already registered with this user"}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class AuthorUpdateSerializers(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ["id", "name", "picture"]
    
class AuthorDeleteSerializers(serializers.ModelSerializer, DestroyModelMixin):
  
    class Meta:
        model = Author
        fields = ["id", "name", "picture"]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ArticlesSerializers(serializers.ModelSerializer):
    category =  CategorySerializers()
    author = AuthorSerializers()
    class Meta:
        model = Articles
        fields = ["id", "author", "category", "title", "summary"]
    

class ArticlesCreateSerializers(serializers.ModelSerializer):
   
    class Meta:
        model = Articles
        fields = ["id", "author", "category", "title", "summary"]

    def create(self, validated_data):
        return super().create(validated_data)


class ArticlesListSerializers(serializers.ModelSerializer):
    category =  CategorySerializers(read_only=True)
    author = AuthorSerializers(read_only=True)
    class Meta:
        model = Articles
        fields = ["id", "author", "category", "title", "summary"]


class ArticlesUpdateSerializers(serializers.ModelSerializer):
   
    class Meta:
        model = Articles
        fields = ["id", "author", "category", "title", "summary"]

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class ArticlesDeleteSerializers(serializers.ModelSerializer, DestroyModelMixin):
    class Meta:
        model = Articles
        fields = ["id", "author", "category", "title", "summary"]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
