from templates import body_template
from templates import html_page_template
from templates import footer_template

def file_page(data):

	data = data.copy()

	data['body'] = body_template({
		'heading': data.get('title'),
		'content': data.get('body'),
	})

	if data.get('footer'):
		data['footer'] = footer_template({
			'back_button': data.get('footer')
			})
	
	print("LOOKING FOOTER", data)
	res = html_page_template(data)
	# print("LOOKING FOOTER", res)

	return res