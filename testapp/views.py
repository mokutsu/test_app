from rest_framework import generics

from testapp.models import Contact, Post
from testapp.serializers import ContactSerializer, PostSerializer


class ContactListCreate(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
