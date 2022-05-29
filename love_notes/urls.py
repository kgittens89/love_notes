from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    # path('', views.Home.as_view(), name="home"),
    path('notes/', views.NoteList.as_view(), name="note_list"),
    path('notes/<int:pk>', views.NoteDetail.as_view(), name="note_detail")
]