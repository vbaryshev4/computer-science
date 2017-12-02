from templates.pages import index_page

def index_controller(http_request):
	return index_page({
		'title': 'Index',
		'body': 'Hello',
		'styles': [
			'/static/new.css'
		]
	})