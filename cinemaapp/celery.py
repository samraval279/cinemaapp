from datetime import timedelta
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cinemaapp.settings")
app = Celery("movie.tasks")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'update-rank-every-5-minutes': {
        'task': 'update_rank',
        'schedule': timedelta(minutes=5),
    },
}