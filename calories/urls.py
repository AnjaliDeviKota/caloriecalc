from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomePageView,LoginPage,LogOutPage,select_food,add_food,RegisterPage,ProfilePage,update_food,delete_food

urlpatterns = [
	path('', HomePageView,name='home'),
	path('login/',LoginPage,name='login'),
	path('logout/',LogOutPage,name='logout'),
	path('select_food/',select_food,name='select_food'),
	path('add_food/',add_food,name='add_food'),
	path('update_food/<str:pk>/',update_food,name='update_food'),
	path('delete_food/<str:pk>/',delete_food,name='delete_food'),
	path('register/',RegisterPage,name='register'),
	path('profile/',ProfilePage,name='profile'),
	path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password"),

    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),

    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]