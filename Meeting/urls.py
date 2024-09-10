from django.urls import path
from . import views  # Import the views from your app

urlpatterns = [
    path('', views.index, name='index'),  # Root URL (e.g., /)
    path('home/', views.home, name='home'),  # URL for home page (e.g., /home/)
    path('planner/', views.planner, name='planner'),  # URL for planner page (e.g., /planner/)
]
