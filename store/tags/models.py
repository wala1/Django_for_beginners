from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)

class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE) #what tag applied to what object
    #Type( product - video - article)
    #ID
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey()
