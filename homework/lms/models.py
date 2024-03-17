from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255)
    preview = models.ImageField(upload_to='courses_previews/')
    description = models.TextField()


class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    preview = models.ImageField(upload_to='lessons_previews/')
    video_url = models.URLField()