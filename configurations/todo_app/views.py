from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from .models import Note, StageNote
from .serializers import NoteSaveSerializer,NoteSerializer, StageNoteSaveSerializer, StageNoteSerializer
from rest_framework.generics import (CreateAPIView , RetrieveUpdateDestroyAPIView, ListCreateAPIView)

@api_view(["POST"])
def createNote(request):
    data=request.data.dict()
    print(request.user)
    print(data)
    data["author"]=request.user.id
    serializer=NoteSaveSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        note=serializer.save()
        return Response(NoteSerializer(note,many=False).data)
    return Response({})



class CreateNoteAPI(CreateAPIView):
    # queryset = None
    serializer_class = NoteSaveSerializer


class NotesAPI(ListCreateAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ["cat"]

    def get_queryset(self):
        #queryset = Note.objects.filter(author=self.request.user)
        cat = self.kwargs.get("cat")  # Получаем значение cat из URL
        print(cat)
        if cat is not None:
            queryset = Note.objects.filter(author=self.request.user, cat=cat)
        return queryset
    

class NotesAPI22(ListCreateAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ["cat"]

    def get_queryset(self):
        queryset = Note.objects.filter(cat=2)
        return queryset

class NoteRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSaveSerializer
    queryset = Note.objects.all()
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
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)



@api_view(["POST"])
def createStageNote(request):
    data=request.data.dict()
    print(request.user)
    print(data)
    data["authorstage"]=request.user.id
    serializer=StageNoteSaveSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        notestage=serializer.save()
        return Response(StageNoteSerializer(notestage,many=False).data)
    return Response({})





class CreateStageNoteAPI(CreateAPIView):
    # queryset = None
    serializer_class = StageNoteSaveSerializer


class StageNotesAPI(ListCreateAPIView):
    serializer_class = StageNoteSerializer
    queryset = StageNote.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ["idnote"]

    def get_queryset(self):
        idnote = self.kwargs.get("idnote")
        print(idnote)
        if idnote is not None:
            queryset = StageNote.objects.filter(authorstage=self.request.user, idnote=idnote)
        return queryset


class StageNotesAPI11(ListCreateAPIView):
    serializer_class =StageNoteSerializer
    queryset = StageNote.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ["catstage"]

    def get_queryset(self):
        queryset = StageNote.objects.filter(catstage=1)
        return queryset
    


    





class StageNoteRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class =StageNoteSaveSerializer
    queryset = StageNote.objects.all()
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
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
