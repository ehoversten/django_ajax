from django.conf.urls import url
from . import views
# from views import Posts

app_name = 'ajaxify'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^insert$', views.insert, name='insert'),

    # CBV routes
    url(r'^posts$', views.Posts.as_view(), name='posts'),
    url(r'^template$', views.PostTemplateView.as_view(), name='template'),
    url(r'^form$', views.PostFormView.as_view(), name='form'),

    url(r'^posty$', views.PostListView.as_view(), name='posty'),
    url(r'^new_post$', views.NewPostView.as_view(), name='new_post'),

]
