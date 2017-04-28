from django.conf.urls import url

from codescript import views

urlpatterns = [
    url(r'^$', views.code_scripts, name="codeScripts"),

    url(r'^save$', views.save_code_script, name="save_scripts"),
    url(r'^codenow/$', views.new_code_script, name="codenow"),
    url(r'^codenow/(?P<id>\d+)/$', views.load_code_script, name='codescript'),

]
