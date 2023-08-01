from django.urls import path
from .views import NewsList, NewsDetail, PostCreate, PostUpdate, PostDelete, PostSearch
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
   path('', NewsList.as_view(), name='post_list'),
   # path('login/', include('sign.urls'))
   path('<int:pk>', NewsDetail.as_view(), name='post_detail'),
   path('search/', PostSearch.as_view(), name='post_search'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('articles/create/', PostCreate.as_view(), name='articles_create'),
   path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='articles_edit'),
   path('articles/<int:pk>/delete/', PostDelete.as_view(), name='articles_delete'),
   path('sign/login/', LoginView.as_view(template_name='sign/login.html'), name='login'),
   path('sign/logout/', LogoutView.as_view(template_name='sign/logout.html'), name='logout'),
]