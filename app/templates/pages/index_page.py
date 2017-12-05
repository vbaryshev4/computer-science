from templates import body_template, html_page_template

def index_page(data):
	data = data.copy()

	data['body'] = body_template({
		'heading': data.get('title'),
		'content': data.get('body')
	})

	return html_page_template(data)