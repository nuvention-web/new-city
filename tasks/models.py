from django.db import models

# Create your models here.


class Category(models.Model):
    cat_title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)
    selected = models.BooleanField(default = False)

    def __str__(self):
        return self.cat_title

class Task(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    task_title = models.CharField(max_length = 50)
    content = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.task_title

    # question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')

