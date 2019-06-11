from django.conf.urls import re_path
from .views import PostListView, PostDetailView, UserPostForm,\
    UserPostFormSuccess, get_ip #get_ip_address_from_request#get_client_ip


urlpatterns = [
    re_path('^$', PostListView.as_view(), name='post_list'),
    re_path('article-(?P<id>[0-9]+)-(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='post_detail'),
    re_path('write-your-article/$', UserPostForm.as_view(), name='user_post_form'),
    re_path('published-success/$', UserPostFormSuccess.as_view(), name='success'),
    re_path('ip-test/', get_ip, name='get_ip'),
    # re_path('ip-test/', get_ip_address_from_request, name='get_ip'),
]