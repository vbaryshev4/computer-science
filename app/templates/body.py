from pkgs.html import Tag, Heading

div = Tag('div')
h = Heading(3)
code = Tag('code')
pre = Tag('pre')
a = Tag('a')
hr = Tag('hr')

# {
	# 'title': 'Index',
	# 'body': 'Hello', 
	# 'styles': ['/static/new.css']
# }

def body_template(data = {}):
	res = div.render([
		h.render(data.get('heading')),
		div.render(
			pre.render(
				code.render(
					data.get('content'), class_name="content"
					)
				), class_name='python')
			], 
			class_name="container")

	return res

def footer_template(data = {}):
	res = hr.render(
		a.render(
			data.get('back_button')
		), class_name='/'
	)
	return res



