from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    # localhost:8000/post/1
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    # 신규등록
    url(r'^post/new/$', views.post_new_form, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    # 댓글 등록
    url(r'^post/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),
]