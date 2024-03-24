from django.urls import path
from . import views
from django.urls import path
from .views import (
    post_list,
    post_publish,
    post_remove,
    add_comment_to_post,
    comment_approve,
    comment_remove,
    post_draft_list,
    post_new,
    post_edit,
    post_detail,
    user_login,
    user_logout,
)

urlpatterns = [
    # Blog-related URLs
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/<pk>/publish/', post_publish, name='post_publish'),
    path('post/<pk>/remove/', post_remove, name='post_remove'),
    path('post/<int:pk>/comment/', add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', comment_remove, name='comment_remove'),
    path('drafts/', post_draft_list, name='post_draft_list'),
    path('post/new/', post_new, name='post_new'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    
    # Authentication-related URLs
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('skip/<int:current_post_id>/', views.skip_to_next_post, name='skip_to_next_post'),
    

   

]

