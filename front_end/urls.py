from django.conf.urls import url
from front_end import views

app_name = 'front_end'
urlpatterns = [
    #url(r'^query/$', views.PlatformRequestView.as_view(), name='platform_request'),
    url(r'^$', views.index, name='index'),
    url(r'^signup-user/$', views.signup_user, name='sign_up'),
    url(r'^login-user/$', views.login_user, name='login_user'),
    url(r'^logout-user/$', views.logout_user, name='logout_user'),
    url(r'^home/$', views.home),
    url(r'^get_medicine_list/$', views.get_medicine_list, name='get_medicine_list'),
    url(r'^send_medicine_data/$', views.send_medicine_data, name='send_medicine_data'),
    url(r'^practo_layer/$', views.practo_layer, name='practo_layer'),
    url(r'^watson_endpoint/$', views.watson_endpoint, name='watson_endpoint'),
    url(r'^results/$', views.watson_endpoint, name='results'),
]