from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone

from movies.models import Movie

class MovieDetailView(DetailView):
    model = Movie
    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class MovieList(ListView):
    model = Movie

class MovieCreate(CreateView):
    model = Movie
    success_url = reverse_lazy('movie_list')

class MovieUpdate(UpdateView):
    model = Movie
    success_url = reverse_lazy('movie_list')

class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('movie_list')
