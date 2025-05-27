from rest_framework import generics, viewsets, permissions
from rest_framework.response import Response
from .models import Category, Product, Cart
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import render
# Auth Views
def product(request):
    return render(request,"product.html")
def signup(request):
    return render(request,"signup.html")
def login(request):
    return render(request,"login.html")
def category(request):
    return render(request,"category.html")
def home(request):
    return render(request,"home.html")
def shop(request):
    return render(request,"shop.html")
def singlepro(request):
    return render(request,"single-product.html")
def cart(request):
    return render(request,"cart.html")
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class LogoutView(generics.GenericAPIView):
    def post(self, request):
        try:
            token = RefreshToken(request.data["refresh"])
            token.blacklist()
            return Response({"message": "Logged out successfully."})
        except:
            return Response({"error": "Invalid refresh token"}, status=400)

# # Category
# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

#     def get_permissions(self):
#         if self.request.method in ['POST']:
#             return [permissions.IsAdminUser()]
#         return [permissions.AllowAny()]

# # Product
# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def get_permissions(self):
#         if self.request.method in ['POST', 'PATCH', 'DELETE']:
#             return [permissions.IsAdminUser()]
#         return [permissions.AllowAny()]

# # Cart
# class CartViewSet(viewsets.ModelViewSet):
#     serializer_class = CartSerializer

#     def get_queryset(self):
#         return Cart.objects.filter(user=self.request.user)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
