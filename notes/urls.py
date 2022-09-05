from django.urls import path


from . import views

urlpatterns = [
    path('smart/',views.NotesListView.as_view(),name='notes.list'),
    # path('smart/',views.list),
    path('blog/<int:pk>',views.NotesDetailView.as_view(),name='notes.detail'),
    path('blog/<int:pk>/edit',views.NotesUpdateView.as_view(),name='notes.update'),
    # path('blog/<int:pk>',views.detail),
    path('notes/new',views.NotesCreateView.as_view(), name='notes.new'),
    path('blog/<int:pk>/delete',views.NotesDeleteView.as_view(), name='notes.delete'),
]