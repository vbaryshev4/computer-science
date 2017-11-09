import requests as req
import urllib

class Resource(object):
	"""docstring for Resource"""
	def __init__(self, url):
		if url.startswith('http:'):
			self.url = url
		else:
			raise TypeError('Should starts with http or https')

	def __url_join(self, path):
		if self.url.endswith('/'):
			if path.startswith('/'):
				return self.url + path[1:]
			else:
				return self.url + path
		else:
			if path.startswith('/'):
				return self.url + path
			else:
				return self.url + '/' + path

	@staticmethod
	def encode_uri_component(arg):
		return urllib.parse.quote(arg.encode("utf-8"))

	def get(self, path):
		return req.get(self.__url_join(path))

	def search(self, path, **kwargs):
		s = self.__url_join(path)
		query = '?'
		for i in kwargs:
			string = str(kwargs.get(i))
			key = self.__encode_uri_component(i)
			value = self.__encode_uri_component(string)
			query += key + '=' + value + '&'

		url = s + query[:-1]

		return req.get(url)



class Api(Resource):
	"""docstring for Api"""
	def __init__(self, url):
		# self - пустой объект

		super(Api, self).__init__(url)

		# self.url - появился

		def create_universal_request_fn(method):
			def request_fn(path, payload=None):
				return self.universal_request(method, path, payload)
			return request_fn

		self.post = create_universal_request_fn('post')

		"""
		self.post = ( method = 'post'
			def request_fn(path, payload=None)
				return self.request(method, path, payload)
		)

		"""
		self.patch = create_universal_request_fn('patch')
		self.put = create_universal_request_fn('put')
		self.delete = create_universal_request_fn('delete')
	
	def universal_request(self, method, path, payload=None):
		url = self._Resource__url_join(path)
		req_method = getattr(req, method)
		return req_method(url, params=payload)
