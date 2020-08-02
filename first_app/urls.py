from django.conf.urls import url
from first_app import views

app_name='first_app'

urlpatterns=[
    url(r'$^',views.index, name='index'),
    url(r'EmployeeLanding/', views.EmployeeLogin, name="EmployeeLogin"),
    url(r'Post/', views.Posting, name="Posting"),
    url(r'PageOne/$', views.PageOne, name='PageOne'),
    url(r'Contacts/$', views.Contacts, name='Contacts'),
    url(r'PageTwo/$', views.PageTwo, name='PageTwo'),
    url(r'Registration/$', views.Registration, name='Registration'),
    url(r'HomePage/$', views.AppHomePage, name='AppHomePage'),
    url(r'user_login/$', views.user_login, name='user_login'),
    url(r'user_logout/$', views.user_logout, name='user_logout'),
]