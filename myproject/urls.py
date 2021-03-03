from django.urls import path
from.views import *

urlpatterns=[
path('all_project/', all_project, name='all_project'),
    path('type/<int:id>/',type,name='type'),
    path('explore_product/<int:id>/',project_by_slug,name='project_by_slug'),
    path('create_explore/', CreateExploreProject, name='create_explore'),
    path('update_explore/<int:id>', UpdateExploreProject, name='update_explore'),
    path('delete_explore/<int:id>', DeleteExporeProject, name='delete_explore'),
]