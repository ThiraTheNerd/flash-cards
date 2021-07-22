from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    def save_course(self):
        self.save()

    @classmethod
    def delete_course(cls , id):
        cls.objects.filter(id=id).delete()

       