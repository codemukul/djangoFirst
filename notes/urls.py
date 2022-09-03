from django.urls import path


from . import views

urlpatterns = [
    path('smart/',views.NotesListView.as_view()),
    # path('smart/',views.list),
    path('blog/<int:pk>',views.NotesDetailView.as_view()),
    # path('blog/<int:pk>',views.detail),
]