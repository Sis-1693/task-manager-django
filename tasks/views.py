from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.timezone import now
from .models import Task

@api_view(['GET'])
def update_overdue(request):
    today = now().date()

    overdue_tasks = Task.objects.filter(
        due_date__lt=today
    ).exclude(status='DONE').exclude(status='OVERDUE')

    count = overdue_tasks.update(status='OVERDUE')

    return Response({
        "message": "Overdue updated successfully",
        "updated_tasks": count
    })