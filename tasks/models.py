from django.db import models

# Create your models here.


class Category(models.Model):
    category_title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 200)
    category_selected = models.BooleanField(default = False)

    def __str__(self):
        return self.category_title

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

class Question(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    question_title = models.CharField(max_length = 50)
    question_text = models.CharField(max_length = 200)

    def __str__(self):
        return self.question_title

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    choice_selected = models.BooleanField(default = False)

    def __str__(self):
        return self.choice_text

