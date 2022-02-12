from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import account_views
from .views import news_views
app_name = "api"

router = routers.DefaultRouter()


urlpatterns = [
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
    
    path("account/sign-up", account_views.AccountCreateView.as_view(), name="sign-up"),
    path("account/update/<int:pk>", account_views.AccountUpdateView.as_view(), name="accout_update"),

    path("articles/?category=<slug:category_slug>", news_views.ArticlesListCategoryView.as_view(), name="articles_list_category"),

    path("articles/<int:pk>", news_views.ArticlesDetailView.as_view(), name="articles_detail"),
    path("articles", news_views.ArticlesListView.as_view(), name="articles_list"),
    path("articles/update/<int:pk>", news_views.ArticlesUpdateView.as_view(), name="articles_update"),
    path("articles/delete/<int:pk>", news_views.ArticlesDeleteView.as_view(), name="articles_delete"),
    path("articles/create", news_views.ArticlesCreateView.as_view(), name="articles_create"),

    path("category", news_views.CategoryListView.as_view(), name="category_list"),
    path("category/<int:pk>", news_views.CategoryDetailView.as_view(), name="category_detail"),
    path("category/update/<int:pk>", news_views.CategoryUpdateView.as_view(), name="category_update"),
    path("category/create", news_views.CategoryCreateView.as_view(), name="category_create"),

]

