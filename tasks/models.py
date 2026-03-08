from django.db import models

class Task(models.Model):
    id = models.BigAutoField(primary_key=True)
    project_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    title = models.CharField(max_length=255)

    status = models.CharField(max_length=20)
    priority = models.CharField(max_length=20)

    due_date = models.DateField()

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = "tasks"
        managed = False