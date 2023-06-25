
def user_name(request):
	username = request.user
	return {'username':username}
