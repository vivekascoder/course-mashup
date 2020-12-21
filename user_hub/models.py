from django.db import models
from authentication.models import User
from courses.models import CourseHub


# Json-field be like
{
	"course-collection": {
		"id-1": {
			"name": "Hello world in python",
			"course_rating": "9",
			"course_link": "http://lol.com"
		},
		"id-2": {
			"name": "Hello world in python",
			"course_rating": "9",
			"course_link": "http://lol.com"
		}
	}
}

class UserCourse(models.Model):
    profile = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100) # Python zero to hero
    lang_tag = models.CharField(max_length=100) #python
    module = models.BooleanField() #false
    course_tag = models.CharField(max_length=100) #python
    course_collection = models.JSONField()
    rating = models.IntegerField(default=1) #overall rating of this course
    joined_date = models.DateTimeField(auto_now_add=True) # established date

    class Meta:
        ordering = ('rating',)
    

    def __str__(self):
        return self.name

