from rest_framework import serializers, status
from rest_framework.mixins import DestroyModelMixin
from rest_framework.response import Response

from apps.news.models import Articles, Category, Author

class CategorySerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"

class CategoryCreateSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"
    def create(self, validated_data):
        return super().create(validated_data)


class CategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"



class CategoryUpdateSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"

    def update(self, instance, validated_data):
    
        return super().update(instance, validated_data)


class CategoryDeleteSerializers(serializers.ModelSerializer, DestroyModelMixin):
 
    class Meta:
        model = Category
        fields = "__all__"
        
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class AuthorSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = "__all__"

class AuthorListSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = "__all__"

class AuthorCreateSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = "__all__"

    def create(self, validated_data):
        return super().create(validated_data)

class AuthorUpdateSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = "__all__"
    
class AuthorDeleteSerializers(serializers.ModelSerializer, DestroyModelMixin):
    
    class Meta:
        model = Author
        fields = "__all__"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class ArticlesSerializers(serializers.ModelSerializer):
    category =  CategorySerializers(read_only=True)
    author = AuthorSerializers(read_only=True)
    class Meta:
        model = Articles
        fields = "__all__"

class ArticlesCreateSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Articles
        fields = "__all__"

    def create(self, validated_data):
        return super().create(validated_data)


class ArticlesListSerializers(serializers.ModelSerializer):
    category =  CategorySerializers(read_only=True)
    author = AuthorSerializers(read_only=True)
    class Meta:
        model = Articles
        fields = "__all__"

class ArticlesUpdateSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Articles
        fields = "__all__"

    def update(self, instance, validated_data):

        return super().update(instance, validated_data)

class ArticlesDeleteSerializers(serializers.ModelSerializer, DestroyModelMixin):
    
    class Meta:
        model = Articles
        fields = "__all__"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
