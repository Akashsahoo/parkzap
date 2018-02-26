from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^signup/$',views.signup,name="signup"),
    url(r'^signin/$',views.signin,name="signin"),
    url(r'^$',views.index,name="index"),
    url(r'^status/$',views.status,name="status"),

]