from django.urls import path , include
from . import views


urlpatterns=[
    path("createNote/",views.CreateNoteAPI.as_view()),
    #path("getNote/",views.getNote),
    path("getListOfNotes/<int:cat>/",views.NotesAPI.as_view()),
    path("getListOfNotesCommunity/",views.NotesAPI22.as_view()),
    path("deleteUpdateNote/<pk>/",views.NoteRetrieveUpdateDestroyAPIView.as_view()),
    #path("deleteNote/",views.deleteNote),
    path("createStageNote/",views.CreateStageNoteAPI.as_view()),
    path("getListOfStageNotes/<int:idnote>/",views.StageNotesAPI.as_view()),
    path("getListOfStageNotesCommunity/",views.StageNotesAPI11.as_view()),
    path("deleteUpdateStageNote/<pk>/",views.StageNoteRetrieveUpdateDestroyAPIView.as_view()),
]