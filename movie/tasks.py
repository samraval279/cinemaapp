from datetime import datetime, timedelta
from movie.models import Movie
from celery import shared_task

@shared_task(name="update_rank")
def update_rank():
    movies = Movie.objects.filter(status='coming-up')
    for movie in movies:
        created_at = movie.created_at
        now = datetime.now(created_at.tzinfo)
        if movie.status == 'coming-up' and now >= created_at + timedelta(minutes=5):
            movie.ranking += 10
            movie.save()
        elif movie.status == 'running':
            continue