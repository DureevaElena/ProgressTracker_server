from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from .models import NoteTodo, StageNoteTodo
from .serializers import NoteListUpdateSerializer, NotePictureUploadSerializer, NoteSaveSerializer,NoteSerializer, StageNoteSaveSerializer, StageNoteSerializer
from rest_framework.generics import (CreateAPIView , RetrieveUpdateDestroyAPIView, ListCreateAPIView)
from rest_framework import generics



@api_view(["POST"])
def createNote(request):
    data=request.data.dict()
    print(request.user)
    print(data)
    data["authortodo"]=request.user.id
    serializer=NoteSaveSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        notetodo=serializer.save()
        return Response(NoteSerializer(notetodo,many=False).data)
    return Response({})



class CreateNoteAPI(CreateAPIView):
    serializer_class = NoteSaveSerializer


class NotesAPI(ListCreateAPIView):
    serializer_class = NoteSerializer
    queryset = NoteTodo.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ["cattodo"]

    def get_queryset(self):
        queryset = NoteTodo.objects.filter(authortodo=self.request.user)  # Default queryset
        cattodo = self.kwargs.get("cattodo")
        if cattodo is not None:
            queryset = queryset.filter(cattodo=cattodo)  # Further filter if cattodo is provided
        return queryset



    
class NotesAPIStatusTeky(ListCreateAPIView):
    serializer_class = NoteSerializer
    queryset = NoteTodo.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ["statustodo"]

    def get_queryset(self):
        queryset = NoteTodo.objects.filter(authortodo=self.request.user, statustodo=1)  # Default queryset
          # Further filter if cattodo is provided
        return queryset
   

class NotesAPIStatusOD(ListCreateAPIView):
    serializer_class = NoteSerializer
    queryset = NoteTodo.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ["statustodo"]

    def get_queryset(self):
        queryset = NoteTodo.objects.filter(authortodo=self.request.user, statustodo=2)  # Default queryset
          # Further filter if cattodo is provided
        return queryset
   

class NotesAPIStatusEnd(ListCreateAPIView):
    serializer_class = NoteSerializer
    queryset = NoteTodo.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ["statustodo"]

    def get_queryset(self):
        queryset = NoteTodo.objects.filter(authortodo=self.request.user, statustodo=3)  
        return queryset
   

class NotesAPI22(ListCreateAPIView):
    serializer_class = NoteSerializer
    queryset = NoteTodo.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ["cattodo"]

    def get_queryset(self):
        queryset = NoteTodo.objects.filter(cattodo=2)
        return queryset




class NoteRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = NoteListUpdateSerializer
    queryset = NoteTodo.objects.all()
    lookup_field = 'pk'
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = NoteSerializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        instance=serializer.save()
        serializer = NoteSerializer(instance)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
    


class NotePictureUploadView(generics.UpdateAPIView): 
    serializer_class = NotePictureUploadSerializer
    queryset = NoteTodo.objects.all()

    def get_object(self):
        # Получаем объект записи по переданному в URL идентификатору (pk)
        pk = self.kwargs.get('pk')
        return self.queryset.get(pk=pk)

    def put(self, request, *args, **kwargs):
        # Обработка PUT-запроса (полное обновление объекта)
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        # Обработка PATCH-запроса (частичное обновление объекта)
        return self.partial_update(request, *args, **kwargs)
    

#///////////////////////////////////////STAGE_NOTE///////////////////



@api_view(["POST"])
def createStageNote(request):
    data=request.data.dict()
    print(request.user)
    print(data)
    data["authorstagetodo"]=request.user.id
    serializer=StageNoteSaveSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        notestagetodo=serializer.save()
        return Response(StageNoteSerializer(notestagetodo,many=False).data)
    return Response({})





class CreateStageNoteAPI(CreateAPIView):
    serializer_class = StageNoteSaveSerializer


class StageNotesAPI(ListCreateAPIView):
    serializer_class = StageNoteSerializer
    queryset = StageNoteTodo.objects.all()
    filter_backends = [SearchFilter]

    lookup_field = 'pk'
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        queryset = StageNoteTodo.objects.filter(idnotetodo=pk)
        return queryset
   
class StageNoteRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class =StageNoteSaveSerializer
    queryset = StageNoteTodo.objects.all()
    lookup_field = 'pk'
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer =StageNoteSerializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        instance=serializer.save()
        serializer = StageNoteSerializer (instance)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)




