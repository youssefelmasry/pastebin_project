from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from .models import Paste
from .serializers import PasteSerializer
from .custom_permissions import *

class PasteView(generics.ListAPIView):
    model = Paste
    serializer_class = PasteSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            user_paste = Paste.objects.filter(author=user)
            user_sharedWith = Paste.objects.filter(sharedWith=user)
            queryset = user_paste.union(user_sharedWith, all=False)
            return queryset          
        else:
            return Paste.objects.filter(public=True)


class PasteCreate(generics.CreateAPIView):
    model = Paste
    serializer_class = PasteSerializer
    permission_classes = [permissions.IsAuthenticated,]
    queryset = Paste.objects.all()

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user)



class PasteUpdate(generics.RetrieveUpdateAPIView):
    model = Paste
    serializer_class = PasteSerializer
    permission_classes = (permissions.IsAuthenticated ,IsOwner,)
    queryset = Paste.objects.all()

class PasteDelete(generics.RetrieveDestroyAPIView):
    model = Paste
    serializer_class = PasteSerializer
    permission_classes = [permissions.IsAuthenticated ,IsOwner,]
    queryset = Paste.objects.all()