from rest_framework import serializers
from .models import NoteTodo, StageNoteTodo
from django.contrib.auth import get_user_model

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=["id","nickname","profile_picture","email"]



class NoteSerializer(serializers.ModelSerializer):
    authortodo=serializers.SerializerMethodField("get_author")
    class Meta:
        model=NoteTodo
        fields="__all__"
    def get_author(self,model:NoteTodo):
        return AuthorSerializer(model.authortodo,many=False).data



class NoteSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model=NoteTodo
        fields="__all__"



class StageNoteSerializer(serializers.ModelSerializer):
    authorstage=serializers.SerializerMethodField("get_author")
    class Meta:
        model=StageNoteTodo
        fields="__all__"
    def get_author(self,model:StageNoteTodo):
        return AuthorSerializer(model.authorstagetodo,many=False).data



class StageNoteSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model=StageNoteTodo
        fields="__all__"
        

class NotePictureUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteTodo
        fields = ['note_picturetodo']

    def update(self, instance, validated_data):
        instance.note_picturetodo = validated_data.get('note_picturetodo', instance.note_picturetodo)
        instance.save()
        return instance
    

class NoteListUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteTodo
        fields = ['pk', 'titletodo', 'notetodo', 'dataendtodo', 'authortodo', 'cattodo', 'statustodo']


