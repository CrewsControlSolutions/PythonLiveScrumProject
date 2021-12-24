from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bitcoin_analytics_home'),
    path('/add_competitor/', views.create_competitor, name='create'),
    path('/board/', views.show_competition, name='board'),
    path('/edit_competitor/<int:pk>', views.update_competitor, name='edit_competitor'),
    path('/delete_competitor/<int:pk>', views.delete_competitor, name='delete_competitor'),
]