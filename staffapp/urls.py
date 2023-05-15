from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.home_view,name='home'),
    path('search/',views.search_detial,name="search"),
    path('profile/',views.profile_view,name='profile'),
    path('profile/<int:id>/',views.profile_view_user,name='profile_for_user'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('signup/',views.sigup_views,name='signup'),
    path('profile/edit/',views.profile_edit,name='profile_edit'),
    path('delete/',views.delete_profile,name="delete"),
]
