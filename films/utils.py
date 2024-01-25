from django.db.models import Max
from django.http import HttpResponse
from films.models import UserFilms


def get_max_order(user) -> int:
    existing_films = UserFilms.objects.filter(user=user)
    if not existing_films.exists():
        return 1
    else:
        current_max = existing_films.aggregate(max_order=Max("order"))["max_order"]
        return current_max + 1


def reorder(user):
    existing_films = UserFilms.objects.filter(user=user)
    if not existing_films.exists():
        return

    for order, user_film in enumerate(existing_films, start=1):
        user_film.order = order
        user_film.save()
