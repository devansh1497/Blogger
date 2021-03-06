from django.urls import path
from django.conf.urls import url
from . import views
'''
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
]
'''
urlpatterns=[
url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
url(r'^$', views.post_list, name='post_list'),
url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
url(r'^post/new/$', views.post_new, name='post_new'),
url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),

url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
]

'''
path(r'^$', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path(r'post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    path('/post/<pk>/remove/', views.post_remove, name='post_remove')
]'''