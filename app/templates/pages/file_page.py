from templates import body_template
from templates import html_page_template

def file_page(data):

	data = data.copy()

	data['body'] = body_template({
		'heading': data.get('title'),
		'content': data.get('body'),
	})
	
	res = html_page_template(data)

	back_button = '''
		<html>
		<div>
		<hr>
		<a href="/">Back</a>
		</div>
		</html>
		'''

	return res + back_button
