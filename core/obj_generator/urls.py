from .views import GenerateObjAPIView, ReportAPIView, HomeView
from django.urls import path

urlpatterns = [
    path('generate-obj/', GenerateObjAPIView.as_view(), name='generate_obj'),
    path('report/', ReportAPIView.as_view(), name='report'),
]
