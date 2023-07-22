from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import filters
from .models import User
from .serializers import UserSerializer, CreateUserSerializer

class UserListView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name']
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateUserSerializer
        return self.serializer_class
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_param = self.request.query_params.get('first_name', None)
        if search_param:
            queryset = queryset.filter(first_name__startswith=search_param)
        return queryset
    
    
