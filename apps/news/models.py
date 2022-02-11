from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from apps.account.models import User


class Author(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    image = models.ImageField(upload_to=f'author/images/', null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("articles:author_detail", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=150,null=False, blank=False)
    slug = models.SlugField(unique=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categoryes"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('articles:category_list_by_category', args=[self.slug])


class Articles(models.Model):
    title = models.CharField(max_length=140, null=False, blank=False)
    summary = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        #ordering = ('name',)
        verbose_name = "articles"
        verbose_name_plural = "articles"

    def __str__(self):
        return str(self.title[:30])

    def get_absolute_url(self):
        return reverse("articles:articles_detail", kwargs={"pk": self.pk})
