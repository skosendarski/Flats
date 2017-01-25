from django.shortcuts import render
from django.http import HttpResponse
from .models import City, Flat
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .form import BookedForm, SearchForm


class HomeView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'flats_list'

    def get_queryset(self):
        return Flat.objects.filter(status='a')


class SelectView(generic.DetailView):
    model = Flat
    template_name = 'select.html'
    context_object_name = 'flat'


def booked_view(request, pk): #dlaczego pk jest tutaj? i czemu to działa?
    flat = get_object_or_404(Flat, pk=pk)

    if request.method == 'POST':
        form = BookedForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data['nickname']
            date_start = form.cleaned_data['date_from']
            date_end = form.cleaned_data['date_to']
            if (flat.available_from <= date_start <= flat.available_to and
                    flat.available_from <= date_end <= flat.available_to and
                    date_start <= date_end):
                flat.rented_from = date_start
                flat.rented_to = date_end
                flat.nickname = nickname
                flat.status = 'n'
                flat.save()
                return render(request, 'booked.html', {'flat': flat, 'error_message': "Incorrect dates!"})

            else:
                form = BookedForm()
                return render(request, 'select.html', {'flat': flat, 'error_message': "Incorrect dates!"})
    else:
        form = BookedForm()
        return render(request, 'booked.html', {'error_message': "invalid method"})


def search_view(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['city']
            city_search = City.objects.filter(Q(city_name=name))
            if city_search.count() != 0:
                city_id = city_search.id
                date_start = form.cleaned_data['date_from']
                date_end = form.cleaned_data['date_to']
                if date_start <= date_end:
                    result = Flat.objects.filter(Q(city=city_id)
                                         & Q(available_from__lte=date_start)
                                         & Q(available_to__gte=date_start)
                                         & Q(available_from__lte=date_end)
                                         & Q(available_to__gte=date_end)
                                         & Q(status='a'))
                    return render(request, 'search.html', {'result': result})

            else:
                form = SearchForm()
                result = []
                return render(request, 'home.html', {'result': result, 'error_message': "Incorrect dates"
                                                                                        " or city is not"
                                                                                        "in out base!"})

    else:
        form=SearchForm
    return render(request, 'home.html', {'error_message': "invalid method"})













# Create your views here.
