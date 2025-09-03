
from .views import home, signupview,loginview, DashboardView,BlogDetailView,CreateBlogView
from django.urls import path



urlpatterns=[
    path ('', home,name='home'),
    path ('signup/',signupview.as_view(),name='signup'),
    path('login/', loginview.as_view(), name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('blogdetail/<int:id>',BlogDetailView.as_view(), name='blogdetail'),
    path('createblog',CreateBlogView.as_view(), name='createblog'),

    ]
    


    
