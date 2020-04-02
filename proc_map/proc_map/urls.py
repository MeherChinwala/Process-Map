


from django.conf.urls import url
from django.contrib import admin
from map.views import home, final, selected_domain, sub_proc_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', home),
    url(r'^home/([0-9])/$',selected_domain),
    url(r'^home/([0-9])/([0-9])/$',final),
    url(r'^home/([0-9])/([0-9])/([0-9])/$',sub_proc_view),

]
