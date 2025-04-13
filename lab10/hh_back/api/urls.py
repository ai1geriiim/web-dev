from django.urls import path 
from .views import CompanyList, CompanyDetail, VacancyList, VacancyDetail 

urlpatterns = [
    path('api/companies/', CompanyList.as_view(), name = 'company-list'),
    path('api/companies/<int:pk>/', CompanyDetail.as_view(), name = 'company-detail'),
    path('api/vacancies/', VacancyList.as_view(), name = 'vacancy-list'),
    path('api/vacancies/<int:pk>/', VacancyDetail.as_view(), name = 'vacancy-detail'),
]