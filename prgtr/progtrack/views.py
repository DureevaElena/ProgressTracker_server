from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Plans, Category
from .permissions import IsAdminReadOnly, IsOwnerOrReadOnly
from .serializers import PlansSerializer

from rest_framework.views import APIView

#class PlansViewSet(mixins.CreateModelMixin,
#                   mixins.RetrieveModelMixin,
#                   mixins.UpdateModelMixin,
#                   mixins.DestroyModelMixin,
#                   mixins.ListModelMixin,
#                   GenericViewSet):
#    queryset = Plans.objects.all()
#    serializer_class = PlansSerializer

#    def get_queryset(self):
#        pk = self.kwargs.get("pk")

#        if not pk:
#            return Plans.objects.all()[:2]

#        return Plans.objects.filter(pk=pk)

#    @action(methods=['get'], detail=True)
#    def category(self, request, pk=None):
#        cats = Category.objects.get(pk=pk)
#        return Response({'cats': cats.name})

class PlansAPIListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10000

class PlansAPIList(generics.ListCreateAPIView):
    queryset = Plans.objects.all()
    serializer_class = PlansSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = PlansAPIListPagination

class PlansAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Plans.objects.all()
    serializer_class = PlansSerializer
    permission_classes = (IsAuthenticated, )
#    authentication_classes = (TokenAuthentication, )

class PlansAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Plans.objects.all()
    serializer_class = PlansSerializer
    permission_classes = (IsAdminReadOnly,)
