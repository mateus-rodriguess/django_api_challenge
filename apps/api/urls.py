from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import account_views
app_name = "api"

router = routers.DefaultRouter()


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    path("account/sign-up/", account_views.AccountCreateView.as_view(), name="sign-up"),
    path("account/update/<int:pk>/", account_views.AccountUpdateView.as_view(), name="accout_update"),
]
