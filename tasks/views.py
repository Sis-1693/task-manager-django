import requests
from datetime import date
from rest_framework.decorators import api_view
from rest_framework.response import Response

LARAVEL_API = "https://task-manager-s0b7.onrender.com/api"


@api_view(['GET'])
def update_overdue(request):

    response = requests.get(f"{LARAVEL_API}/tasks")
    tasks = response.json()

    today = str(date.today())
    updated = []

    for task in tasks:

        if task["status"] not in ["DONE", "OVERDUE"]:

            if task["due_date"] < today:

                task_id = task["id"]

                requests.put(
                    f"{LARAVEL_API}/tasks/{task_id}/status",
                    json={"status": "OVERDUE"}
                )

                updated.append(task_id)

    return Response({
        "message": "Overdue tasks updated",
        "updated_tasks": updated
    })