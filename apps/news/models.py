from uuid import uuid4
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from apps.account.models import User


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    picture = models.ImageField(upload_to=f'author/images/', null=True,blank=True)
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("news:author_detail", kwargs={"pk": self.pk})


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=150,null=False, blank=False, unique=True)
    slug = models.SlugField(unique=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Category"
        verbose_name_plural = "Categoryes"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('news:category_list_by_category', args=[self.slug])


class Articles(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=140, null=False, blank=False)
    summary = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "articles"
        verbose_name_plural = "articles"

    def __str__(self):
        return str(self.title[:30])

    def get_absolute_url(self):
        return reverse("news:articles_detail", kwargs={"pk": self.pk})
