from django.urls import path

from .views import (

	login_view,signup_view,log_in, sign_up, create_view, create, todo, delete, log_out, completed_task,

	)


urlpatterns = [
	
	path('login_view/',login_view,name='login_view'),
	path('signup_view/',signup_view,name='signup_view'),
	path('login/',log_in,name='login'),
	path('signup/',sign_up,name='signup'),
	path('create_view/',create_view,name='create_view'),
	path('create/',create,name='create'),
	path('todo/',todo,name='todo'),
	path('delete/<int:task>',delete,name='delete'),
	path('log_out/',log_out,name="log_out"),
	path('completed/<int:task_id>',completed_task,name='completed'),

]