from django.db import models
from django.core.serializers import serialize
from django.conf import settings
import json

def upload_update_image(instance,filename):
    return "updates/{user}/{filename}".format(user = instance.user,filename = filename)

# Create your models here.
class UpdateQueryset(models.QuerySet):
    def serialize(self):
        list_values = list(self.values('user','content','image'))
        return json.dumps(list_values)


class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQueryset(self.model,using=self._db)

class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content = models.TextField(blank=True,null = True)
    image = models.ImageField(upload_to = upload_update_image,blank=True,null = True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = UpdateManager()

    def __str__(self):
        return self.content or ""
    
    def serialize(self):
        json_data =  serialize('json',[self],fields=('user','content','image'))
        struct = json.loads(json_data)
        json_data = json.dumps(struct[0]['fields'])
        return json_data