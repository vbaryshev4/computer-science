from templates import body_template, html_page_template

def index_page(data):
	data = data.copy()

	print('\n', '****INDEX_PAGE ASSAMBLE****', '\n')
	print('data before body_template:', data, '\n')
	# {'title': 'Index', 'body': 'Hello', 'styles':
		 # ['/static/new.css']
		 # }

	data['body'] = body_template({
		'heading': data.get('title'),
		'content': data.get('body')
	})
	print('data after body_template:', data, '\n')
	# {'title': 'Index', 
	# 'body': '<div class="container"><h3>Index</h3>
	# 				<div class="content">Hello</div></div>', 
	# 'styles': ['/static/new.css']}

	res = html_page_template(data)

	print('data after html_page_template:', res, '\n')
	# <html><head><title>Index</title><style href="/static/main.css"></style><style href="/static/new.css"></style></head><body><div class="container"><h3>Index</h3><div class="content">Hello</div></div></body></html>


	print('****END OF ASSAMBLE****', '\n')
	
	return res