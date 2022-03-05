from django.db import models

#this class object and their attributes creates the diffeerent aspects to
class DjangoClasses(models.Model):
    Title = models.CharField(max_length=60, blank=False, default="")
    Course_Number = models.DecimalField(default=0, max_digits=10000, decimal_places=2)
    Instructor_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Duration = models.FloatField(max_length=100, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.Title
