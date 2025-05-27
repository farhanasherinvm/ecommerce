from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# router = DefaultRouter()
# router.register('categories', CategoryViewSet)
# router.register('products', ProductViewSet)
# router.register('cart', CartViewSet, basename='cart')

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views
urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),
    path('auth/logout/', LogoutView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    # path('', include(router.urls)),
    path('home/',views.home),
    path('shop/',views.shop),
    path('list/',views.singlepro),
    path('cart/',views.cart),
    path('category/',views.category),
    path('product/',views.product),
    path('signup/',views.signup),
    path('login/',views.login),
]
