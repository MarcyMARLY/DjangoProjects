from django.db import models

class Status(models.Model):
    status_text = models.CharField(max_length = 200)
    def to_json(self):
        return{
            'status_text' : self.status_text,
        }
    def __str__(self):
        return self.status_text
class TodoItem(models.Model):
    todo_text = models.CharField(max_length=200)
    todo_status = models.CharField(max_length=200)

    def to_json(self):
        return{
            'id':self.id,
            'todo_text':self.todo_text,
            'todo_status':self.todo_status,
        }
    def __str__(self):
        return self.todo_text
