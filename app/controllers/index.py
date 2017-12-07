from templates.pages import index_page

def index_controller(http_request):
	res = index_page({
		'title': 'Index',
		'body': 'Hello',
		'styles': [
			'/static/new.css']
		})
	print('index_controller, res:', res, '\n')
	return res