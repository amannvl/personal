from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="home"),
    path("blogwrite/",views.blogwrite, name="blogwrite"),
    path("about/", views.about, name="about"),
    path("blog/", views.bloghome, name="blog"),
    path("contact/", views.contact, name="contact"),
    path("elements/", views.elements, name="elements"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("<int:p_id>/", views.portfoliodetails, name="portfoliodetails"),
    path("services/", views.services, name="services"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    # api for comments
    path("postComment", views.postComment, name="postComment"),

    path("<str:title>/", views.singleblog, name="singleblog"),
]
