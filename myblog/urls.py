from django.urls import path
from.views import *


urlpatterns=[
    path('',home,name='home'),
    path('privacy_policy', privacy_policy, name='privacy_policy'),
    path('disclaimer', disclaimer, name='disclaimer'),
    path('posts',posts,name='posts'),
    path('post/<int:id>',post,name='post'),
    path('search', search, name='search'),

    path('tag/<int:id>',tag,name='tag'),
    path('send_email/', sendEmail, name='send_email'),
    path('create_post', createPost, name='create_post'),
    path('update_post/<int:id>', updatePost, name='update_post'),
    path('delete_post/<int:id>', deletePost, name='delete_post'),

]