from django.urls import path
from tasks import views


urlpatterns = [
    path('createtodo/', views.create_todo),
    path('updatetodo/<int:id>', views.update_todo),
    path('deltodo/<int:id>', views.delete_todo),
    path('todos/', views.all_todos),
    path('todo/<int:id>', views.todo),

]