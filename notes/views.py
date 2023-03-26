from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Notes
from .forms import NotesForms


class NotesListView(LoginRequiredMixin,ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes.notes_list.html'
    login_url = 'home.login'

    def get_queryset(self):
        return self.request.user.notes.all()
        

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/project/notes'
    form_class = NotesForms

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/project/notes'
    template_name = 'notes/notes_delete.html'

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes/notes_detail.html'

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/project/notes'
    form_class = NotesForms

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    



# Original views - new class views above
# Create your views here.
# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html',{'notes':all_notes})

# def detail(request,pk):
#     note = Notes.objects.get(pk=pk)
#     return render(request, 'notes/notes_detail.html',{'notes':note})