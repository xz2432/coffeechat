from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
     	url(r'^$', 'newsletter.views.home', name='home'),
     	url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    # url(r'^blog/', include('blog.urls')),
	
	#url(r'^admin/', include(admin.site.urls)),
	url(r'^admin/', include(admin.site.urls)),
]