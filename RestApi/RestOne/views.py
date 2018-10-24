from django.shortcuts import render
from rest_framework import generics,mixins
from RestOne.models import ModelEmail
from RestOne.serializers import EmailCommonSerializers

class EmailRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = EmailCommonSerializers

    def get_queryset(self):
        return ModelEmail.objects.all()

    def get_object(self):
        pk = self.kwargs.get('pk')
        return ModelEmail.objects.get(pk=pk)

class EmailCreateView(generics.CreateAPIView):
    serializer_class = EmailCommonSerializers

    def get_queryset(self):
        return ModelEmail.objects.all()

class EmailListCreateMixinView(generics.ListAPIView, mixins.CreateModelMixin):
    serializer_class = EmailCommonSerializers

    def get_queryset(self):
        return ModelEmail.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class EmailListView(generics.ListAPIView):
    serializer_class = EmailCommonSerializers

    def get_queryset(self):
        return ModelEmail.objects.all()
