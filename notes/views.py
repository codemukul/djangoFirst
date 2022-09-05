from msilib.schema import ListView
from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView,DetailView, ListView,UpdateView
from django.views.generic.edit import DeleteView

from .forms import NotesForm

from .models import Notes

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart'
    template_name = 'notes/notes_delete.html'

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart'
    form_class = NotesForm

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart'
    form_class = NotesForm

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    # template_name = "notes/notes_list.html" (not required because we have named as the standard name of class , so it automatically fetches it .....)

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    # template_name = "notes/notes_detail.html"

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request,'notes/notes_list.html',{'notes':all_notes})

# def detail(request , pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         # raise Http404('notes/notes_list.html')
#         all_notes = Notes.objects.all()
#         return render(request,'notes/notes_list.html',{'notes':all_notes})
#     return render(request,'notes/notes_detail.html',{'note':note})