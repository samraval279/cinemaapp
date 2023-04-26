from djongo import models
import secrets
# Create your models here.
class CommonBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
STATUS_CHOICE = {
    ('coming-up','coming-up'),
    ('starting','starting'),
    ('running','running'),
    ('finished','finished'),
    
}

class Movie(CommonBase):
    id = models.CharField(max_length=255,primary_key=True,default=secrets.token_hex(16))
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    protagonists = models.CharField(max_length=255, null=False, blank=False)
    poster = models.ImageField(upload_to='poster',null=False, blank=False)
    start_date = models.DateField(null=False, blank=False)
    status = models.CharField(max_length=255, choices=STATUS_CHOICE, null=False, blank=False)
    ranking = models.IntegerField(default=0)

    class Meta:
        db_table = 'movie'
        
    def __str__(self):
        return self.name
