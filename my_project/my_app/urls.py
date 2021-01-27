from django.urls import path
from my_app.views import *

urlpatterns = [
    path('', NewLoginView.as_view(), name='index'),
    path('logout', NewLogoutView.as_view(), name='logout'),
    
    path('positions', AllPositionView.as_view(), name="all_positions"),
    path('positions/add/', CreatePositionView.as_view(), name="position_add"),
    path('positions/<int:pk>/update', UpdatePositionView.as_view(), name="position_update"),
    path('positions/<int:pk>/', DetailPositionView.as_view(), name="position_detail"),
    path('positions/<int:pk>/delete', DeletePositionView.as_view(), name="position_delete"),
    
    path('workers', WorkerListView.as_view(), name='all_workers'),
    path('workers/add/', CreateWorkerView.as_view(), name="worker_add"),
    path('workers/<int:pk>/update', UpdateWorkerView.as_view(), name="worker_update"),
    path('workers/<int:pk>/delete', DeleteWorkerView.as_view(), name="worker_delete"),
    path('avg_workers', AvgWorkersView.as_view(), name='avg_workers'),
]
