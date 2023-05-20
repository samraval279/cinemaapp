from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
import secrets

from movie.models import *

@receiver(post_save, sender=Movie)
def sync(sender, instance, **kwargs):
    print(instance)
    # if created is not None:
    if kwargs.get('created', False):
        # Create the MongoDBMovie instance
        mongo_instance = Movie.objects.using('mongo').create(
            id=instance.id,
            name=instance.name,
            protagonists=instance.protagonists,
            poster=instance.poster,
            start_date=instance.start_date,
            status=instance.status,
            ranking=instance.ranking,
        )
        created = True
        # mongo_instance.save(using='mongo')

@receiver(post_delete, sender=Movie)
def sync(sender, instance, **kwargs):
    Movie.objects.using('mongo').filter(id=instance.id).delete()