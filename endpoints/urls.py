from django.urls import path, include

from endpoints.views import edit_endpoint, delete_endpoint, details_endpoint, add_endpoint, tags_list, tag_details, \
    edit_tag, add_tag


app_name = 'endpoints'

urlpatterns = [
    path('tags/', tags_list, name='tags_list'),
    path('tags/create/', add_tag, name='add_tag'),
    path('tags/<int:pk>/', include([
        path('', tag_details, name='tag_details'),
        path('edit/', edit_tag, name='edit_tag'),
    ])),
    path('<int:pk>/', include([

        path('project/create/', add_endpoint, name='add_endpoint'),
        path('details/', details_endpoint, name='detail_endpoint'),
        path('edit/', edit_endpoint, name='edit_endpoint'),
        path('delete/', delete_endpoint, name='delete_endpoint'),
    ]))



]