from django.db import models

class SimilarCourse(models.Model):
    university_name = models.CharField(max_length=50, primary_key=True)
    course_code = models.CharField(max_length=20)
    course_name = models.CharField(max_length=255)
    course_credit = models.FloatField()

    class Meta:
        db_table = 'similar_courses'
        managed = True
        unique_together = (('university_name', 'course_code'),)
