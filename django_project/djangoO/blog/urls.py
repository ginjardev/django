from django.urls import path
from blog import views
from .views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('about/', views.about, name="about-page")
] 