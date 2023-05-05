from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    read_time = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    person_that_make_it = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created", "-updated"]
