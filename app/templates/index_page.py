from templates import body_template, html_page_template

def index_page(data):
	data['body'] = body_template(data.get('body'))
	return html_page_template(data)