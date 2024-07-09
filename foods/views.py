from django.shortcuts import render
from .models import FoodType,Food,Comment
from .serializers import FoodTypeSerializer,FoodSerializer,CommentSerializer
from .permissions import CustomPermission
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication


class FoodTypeAPIView(ModelViewSet):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer
    permission_classes = [CustomPermission]
    authentication_classes = [BasicAuthentication,SessionAuthentication]

class FoodAPIView(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [CustomPermission]
    authentication_classes = [TokenAuthentication]

class CommentAPIView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CustomPermission]
