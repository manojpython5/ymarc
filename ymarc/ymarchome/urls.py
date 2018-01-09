from django.conf.urls import url
from ymarchome import views



app_name="ymarchome"

urlpatterns = [
    url(r'^$', views.home,name="index"),
    url(r'^veg/$',views.veg,name="veg"),
    url(r'^user_login/$',views.user_login,name='user_login'),
]
