from django.db import models
import os
import uuid

def thumbnail_dir_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{0}.{1}'.format(uuid.uuid4().hex[:10], ext)
    return os.path.join("files", filename)

SYS_SORT_CHOICES = [
    (1, 'id'),
    (2, 'Title'),
    (3, 'ProjectUrl'),
    (4, 'created_at'),
]

SYS_SORTKIND_CHOICES = [
    (1,'Asending'),
    (2,'Desending'),
]

class PortalSoring(models.Model):
    sortby = models.IntegerField(choices=SYS_SORT_CHOICES, default=2, verbose_name='Sorting By')
    sortkind = models.IntegerField(choices=SYS_SORTKIND_CHOICES, default=1, verbose_name='Sorting Kind')

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now     = True)

    def __str__(self):
        return 'Sorting by {0}  | Sorting kind {1}'.format(dict(SYS_SORT_CHOICES)[self.sortby], dict(SYS_SORTKIND_CHOICES)[self.sortkind])

class Project(models.Model):

    Title = models.CharField(max_length=50, null=False, blank=False)
    Description = models.CharField(max_length=150, null=False, blank=False)
    Thumbnail = models.ImageField(upload_to=thumbnail_dir_path,  null=False, blank=False)

    ProjectUrl = models.CharField(max_length=250, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now     = True)    

    def __str__(self):
        return self.Title