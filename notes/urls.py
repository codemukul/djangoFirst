from django.urls import path


from . import views

urlpatterns = [
    path('smart/',views.list),
    path('blog/<int:pk>',views.detail),

]