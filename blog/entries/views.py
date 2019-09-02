from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Entry
from .forms import CommentForm

class HomeView(ListView):
	model = Entry
	template_name = 'entries/index.html'
	context_object_name = "blog_entries" # why did single quote not work?
	ordering = ['-entry_date']
	paginate_by = 3

class EntryView(DetailView):
	model = Entry
	template_name = 'entries/entry_detail.html'

class CreateEntryView(CreateView):
	model = Entry
	template_name = 'entries/create_entry.html'
	fields = ['entry_title', 'entry_text']

	def form_valid(self, form):
		form.instance.entry_author = self.request.user
		return super().form_valid(form)

def create_comment(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST) # how does django know the model is comment
        if form.is_valid():
            comment = form.save(commit=False)
            comment.entry = entry
            comment.comment_author = request.user
            comment.save()
            return redirect('entry-detail', pk=entry.pk)
    else:
        form = CommentForm()
    return render(request, 'entries/create_comment.html', {'form': form}) # how does django know which entry?