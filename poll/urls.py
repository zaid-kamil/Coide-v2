from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^fake/$', views.home, name="home"),
    url(r'^list/$', views.list, name="list"),
    url(r'^about/$', views.about_us, name="about"),
    url(r'^useraccount/$', views.user_account, name="useraccount"),
    url(r'^article/$', views.articles_list, name="articles"),
    url(r'^tellme/', include("tellme.urls")),
    url(r'^article/(?P<id>\d)/$',views.article_details,name="details"),
    url(r'^article/(?P<category>\w+)/$',views.article_category),


]

