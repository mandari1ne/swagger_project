from django.shortcuts import render, get_object_or_404
from .models import Film, Actor

def film_index(request):
    films = Film.objects.all()

    # Фильтрация по году выпуска
    release_year = request.GET.get('release_year')
    if release_year:
        films = films.filter(release_year=release_year)

    # Фильтрация по главному актёру (по имени актера)
    main_actor = request.GET.get('main_actor')
    if main_actor:
        films = films.filter(main_actor__name__icontains=main_actor)

    visits_count = request.session.get('visits_num', 0)
    request.session['visits_num'] = visits_count + 1

    film_num = films.count()

    return render(request, 'film_index.html',
                  {
                      'films': films,
                      'num': film_num,
                      'visits_count': visits_count
                  })

def film_detail(request, pk):
    film = get_object_or_404(Film, pk=pk)
    return render(request, 'film_detail.html', {'film': film})