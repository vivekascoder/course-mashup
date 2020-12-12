from django.db import models

class CourseHub(models.Model):
    name = models.CharField(max_length=100)
    lang_tag = models.CharField(max_length=100)
    module = models.BooleanField()
    course_tag = models.CharField(max_length=100)
    location_url = models.URLField(max_length=200)
    rating = models.IntegerField(default=1)
    joined_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('rating',)
    

    def __str__(self):
        return self.name
