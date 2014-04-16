import django
from django.conf.urls import patterns, url


urlpatterns = patterns('authtools.views',
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^password_change/$', 'password_change', name='password_change'),
    url(r'^password_change/done/$', 'password_change_done', name='password_change_done'),
    url(r'^password_reset/$', 'password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'password_reset_done', name='password_reset_done'),
    url(r'^reset/done/$', 'password_reset_complete', name='password_reset_complete'),
    url(r'^registration/$', 'registration_view', name='revistration_view'),
    url(r'^registration/done$', 'registration_done_view', name='revistration_done_view'),
    url(r'^registration/complete$', 'registration_complete_view', name='revistration_complete_view'),
    url(r'^registration/disallowed$', 'registration_disallowed_view', name='revistration_disallowed_view'),
)

if django.VERSION < (1, 6):
    urlpatterns += patterns('authtools.views',
        url(r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            'password_reset_confirm',
            name='password_reset_confirm'),
        url(r'^registration/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            'registration_view',
            name='registration_confirm_view'),

    )
else:
    urlpatterns += patterns('authtools.views',
        url(r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            'password_reset_confirm_uidb36'),
        url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            'password_reset_confirm',
            name='password_reset_confirm'),
        url(r'^registration/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            'registration_view',
            name='registration_confirm_view'),

    )
