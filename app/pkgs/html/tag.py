class Tag(object):
	def __init__(self, tag, **defaults):
		self.tag = tag
		self.default_attrs = defaults

	template = '<{tag}{attrs}>{content}</{tag}>'

	@staticmethod
	def get_html_attrs(attrs):
		new_attrs = {}

		html_attrs = {
			'class_name': 'class',
			'html_for': 'for'
		}

		for key in attrs.keys():
			attr_value = attrs.get(key)

			if key in html_attrs.keys():
				new_key = html_attrs.get(key)
				new_attrs[new_key] = attr_value
			else:
				new_attrs[key] = attr_value

		return new_attrs
	
	@staticmethod
	def attrs_to_string(attrs):
		s = ''
		for key in attrs.keys():
			s += ' {key}="{val}"'.format(
				key=key,val=attrs[key]
				)

		return s

	def __call__(self, *args, **kwargs):
		return self.render(*args, **kwargs)

	def render(self, content, **kwargs):
		attrs = self.default_attrs.copy()
		attrs.update(kwargs)
		attrs = self.get_html_attrs(attrs)
		attrs = self.attrs_to_string(attrs)

		if isinstance(content, list):
			content = self.parcer(content)

		return self.template.format(
			tag=self.tag,
			attrs=attrs,
			content=content
		)

	def parcer(self, content):
		content = ''.join(content)
		return content

class Img(Tag):
	def __init__(self, **default_attrs):
		super(Img, self).__init__('img', 
			**default_attrs
			)

	template = '<{tag} src="{content}" {attrs} />'

class Heading(Tag):
	def __init__(self, intgr, **default_attrs):
		super(Heading, self).__init__(
			'h' + str(intgr), **default_attrs
			)
	
class List(Tag):
	def __init__(self, ordered, **default_attrs):
		self.class_for_li = None

		if 'item_class_name' in default_attrs:
			value = default_attrs['item_class_name']
			self.class_for_li = value
			default_attrs.pop('item_class_name')

		if ordered is True:
			super(List, self).__init__('ol', **default_attrs)
		else:
			super(List, self).__init__('ul', **default_attrs)

	def parcer(self, content):
		new_content = ''
		for i in content:
			li = Tag('li')
			if self.class_for_li:
				new_content += li.render(
					i, class_name=self.class_for_li
					)
			else:
				new_content += li.render(i)
		return new_content