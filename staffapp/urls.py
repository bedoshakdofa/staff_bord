from django.urls import path
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path('home/',views.home,name='home'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('signup/',views.sigup_views,name='signup'),
    path('profile/',views.profile_view,name='profile'),
    path('profile/edit/',views.profile_edit,name='profile_edit'),
    path('search/',views.search_detial,name="search"),
    # path('detial/',views.recipe_detial,name="detial"),
    # path('record/',views.recipe_record,name='recipeRecord'),
]
