from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ribbit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'ribbit_app.views.index'), # root
    url(r'^login$', 'ribbit_app.views.login_view'), # login
    url(r'^logout$', 'ribbit_app.views.logout_view'), # logout
    url(r'^signup$', 'ribbit_app.views.signup'), # signup
    url(r'^submit$', 'ribbit_app.views.submit'), # submit new ribbit
    url(r'^users/$', 'ribbit_app.views.users'),
    url(r'^users/(?P<username>\w{0,30})/$', 'ribbit_app.views.users'),
    url(r'^follow$', 'ribbit_app.views.follow'),
)
