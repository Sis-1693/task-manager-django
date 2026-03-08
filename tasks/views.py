from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import date
from .models import Task

@api_view(['GET'])
def update_overdue(request):

    today = date.today()

    overdue_tasks = Task.objects.filter(
        due_date__lt=today
    ).exclude(status__in=['DONE', 'OVERDUE'])

    count = overdue_tasks.update(status='OVERDUE')

    return Response({
        "message": "Overdue tasks updated",
        "updated_tasks": count
    })