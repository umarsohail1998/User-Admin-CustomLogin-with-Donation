from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('signup/', views.registration_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('Donate/', views.donate_view, name='Donate'),
    path('Form/', views.forms, name='Form'),
    
    # path('admins/', views.admins, name='admins'),
    # path('submitted/', views.submitted, name='submitted'),
    # path('edit/', views.edit, name='edit'),
    # path('form/', views.formView, name='form'), 
    # path('deleteRecord/<str:pk>/', views.deleteRecord, name='deleteRecord'),
    # path('viewRecord/<str:pk>/', views.viewRecord, name='viewRecord'),
    # path('viewRecords/<str:pk>/', views.viewRecords, name='viewRecords'),
    # path('updateRecord/<str:pk>/', views.updateRecord, name='updateRecord'),
    # path('up_record/<str:pk>/', views.up_record, name='up_record'),
    # path('login/', views.loginPage, name='login'),
    # path('register/', views.registerPage, name='register'),
    # path('logout/', views.logoutPage, name='logout'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)