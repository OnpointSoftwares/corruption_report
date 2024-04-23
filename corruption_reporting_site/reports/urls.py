from django.urls import path
from .views import chat_room, ReportListCreate, ReportListView, ReportDetailView, ReportCreateView
from . import views

urlpatterns = [
    path('api/reports/', ReportListCreate.as_view(), name='report-list-create'),
    path('reports/', ReportListView.as_view(), name='report-list'),
    path('reports/<int:pk>/', ReportDetailView.as_view(), name='report-detail'),
    path('reports/new/', ReportCreateView.as_view(), name='report-create'),
    path('chat/<str:room_name>/', chat_room, name='chat_room'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),

]
