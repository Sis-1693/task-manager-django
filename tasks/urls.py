from django.urls import path
from .views import update_overdue

urlpatterns = [
    path('update-overdue/', update_overdue),
]