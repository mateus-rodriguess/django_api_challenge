from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import account_views
from .views import news_views
from .views_sets import views_sets

app_name = "api"

router = routers.DefaultRouter()
router.register('articles',views_sets.ArticlesViewSet)
router.register('category', views_sets.CategoryViewSet)
router.register('author', views_sets.AuthorViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    path("account/sign-up/", account_views.AccountCreateView.as_view(), name="sign-up"),
    path("account/update/<uuid:pk>/", account_views.AccountUpdateView.as_view(), name="accout_update"),
    path("admin/accounts/", account_views.AccountListView.as_view(), name="accout_list"),

    path("articles/<uuid:pk>/", news_views.ArticlesDetailView.as_view(), name="articles_detail"),
    path("articles/", news_views.ArticlesListView.as_view(), name="articles_list"),
    path("admin/articles/update/<uuid:pk>/", news_views.ArticlesUpdateView.as_view(), name="articles_update"),
    path("admin/articles/delete/<uuid:pk>/", news_views.ArticlesDeleteView.as_view(), name="articles_delete"),
    path("admin/articles/create/", news_views.ArticlesCreateView.as_view(), name="articles_create"),

    path("category/", news_views.CategoryListView.as_view(), name="category_list"),
    path("category/<uuid:pk>/", news_views.CategoryDetailView.as_view(), name="category_detail"),
    path("admin/category/update/<uuid:pk>/", news_views.CategoryUpdateView.as_view(), name="category_update"),
    path("admin/category/create/", news_views.CategoryCreateView.as_view(), name="category_create"),
    path("admin/category/delete/<uuid:pk>/", news_views.AuthorDeleteView.as_view(), name="author_delete"),

    path("admin/author/<uuid:pk>/", news_views.AuthorDetailView.as_view(), name="author_detail"),
    path("admin/authors/", news_views.AuthorListView.as_view(), name="author_list"),
    path("admin/author/create/", news_views.AuthorCreateView.as_view(), name="author_create"),
    path("admin/author/update/<uuid:pk>/", news_views.AuthorUpdateView.as_view(), name="author_update"),

    # API ROOT
    path('', include(router.urls)),
]

