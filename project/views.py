from django.db.models import Q
from django.views.generic import ListView

from celebs import models as celeb_models
from movies import models as movie_models


class IndexView(ListView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['celebs'] = celeb_models.Celebrity.objects.prefetch_related(
            'movie_crews__duty', 'movie_crews__crew', 'comments'
        )[:3]
        context['celeb_title'] = 'Celebrities'
        context['movie_title'] = 'Latest Movies'
        context['movie_title_small'] = 'by release date'
        return context

    def get_queryset(self):
        return movie_models.Movie.objects.prefetch_related(
            'movie_crews__duty', 'movie_crews__crew', 'genres', 'comments').order_by(
            '-release_year', 'title')[:3]


class SearchResultsView(ListView):
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        query = str(self.request.GET.get('q'))
        context = super(SearchResultsView, self).get_context_data(**kwargs)
        context['q'] = query
        context['celebs'] = celeb_models.Celebrity.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)).values_list(
                'pk', 'slug', 'first_name', 'last_name', named=True)
        context['celeb_title'] = 'Found Celebrities'
        context['movie_title'] = 'Found Movies'
        context['movie_title_small'] = 'ordered by release date'
        return context

    def get_queryset(self):
        query = str(self.request.GET.get('q')).strip()
        return movie_models.Movie.objects.filter(Q(title__icontains=query)).values_list(
            'pk', 'slug', 'title', named=True
            ).order_by('-release_year', 'title')
        