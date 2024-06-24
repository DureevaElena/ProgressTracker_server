from django.urls import path , include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path("createNote/",views.CreateNoteAPI.as_view()),

    path("getListOfNotes/<int:cat>/",views.NotesAPI.as_view()),
    path("getListOfStatusNotesTeky/",views.NotesAPIStatusTeky.as_view()),
    path("getListOfStatusNotesOverdate/",views.NotesAPIStatusOD.as_view()),
    path("getListOfStatusNotesEnd/",views.NotesAPIStatusEnd.as_view()),    
    path("getListOfNotesCommunity/",views.NotesAPI22.as_view()),
    path("deleteUpdateNote/<pk>/",views.NoteRetrieveUpdateDestroyAPIView.as_view()),
    path("note/<int:pk>/update/", views.NotePictureUploadView.as_view(), name='note-picture-update'),

    path("createStageNote/",views.CreateStageNoteAPI.as_view()),
    path("getListOfStageNotes/<int:pk>/",views.StageNotesAPI.as_view()),
    path("deleteUpdateStageNote/<pk>/",views.StageNoteRetrieveUpdateDestroyAPIView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)