from django.db import models
from django.utils import timezone

# Create your models here.

class ChaiVarity(models.Model):

    CHAI_TYPES_CHOICES = [
        
    ('ML', 'MASALA'),
    ('GR', 'GINGER'),   
    ('KL', 'KIWI'),
    ('PL', 'PLAIN'),
    ('EL', 'ELAICHI'),

    ]

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='chai_images')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=CHAI_TYPES_CHOICES,default='ML')
    description = models.TextField(default="")

    def __str__(self):
        return self.name