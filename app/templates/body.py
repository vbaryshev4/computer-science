from pkgs.html import Tag, Heading

div = Tag('div')
h1 = Heading(3)

def body_template(data = {}):
	return div.render([
		h1.render(data.get('heading')),
		div.render(data.get('content'), class_name="content")
	], class_name="container")