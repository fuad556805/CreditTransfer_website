from django.db import models

class AllCourse(models.Model):
    university_name = models.CharField(max_length=50, primary_key=True)
    course_code = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'all_courses'
        managed = True  # Django will manage this table (create/migrate)

class University(models.Model):
    university_name = models.CharField(max_length=50, primary_key=True)

    class Meta:
        db_table = 'university'
        managed = False  # Because the table already exists in your SQL database

    def __str__(self):
        return self.university_name
