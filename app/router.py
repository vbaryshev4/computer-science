from flask import request

from controllers.index import index_controller
from controllers.file import file_controller
from controllers.pkgs import pkgs_controller

def init(app):
    @app.route('/')
    def index():
        res = index_controller(request)
        return res

    @app.route('/file/<path:file_path>')
    def file(file_path):
        return file_controller(file_path)

    @app.route('/pkgs/')
    def route():
        # print('YO: 1', '\n')
        return pkgs_controller()


# template = """
# <!DOCTYPE html>
# <html>
#     <head>
#         <link rel="stylesheet" href="/static/main.css">
#         <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/styles/default.min.css">

#         <title>{title}</title>
#     </head>
#     <body>
#         <main>
#             {body}
#         </main>
#     <script src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/highlight.min.js"></script>
#     <script>hljs.initHighlightingOnLoad();</script>
#     </body>
# </  html>
# """


# style = Tag('link', rel="stylesheet")
# html = Tag('html')
# head = Tag('head')
# title = Tag('title')
# body = Tag('body')
# heading = Tag('h1')

# def html_page(title_value, body_value, styles=[]):
#     return html([
#         head([
#             title(title_value),
#             style('', href="/static/main.css")
#         ]),
#         body(body_value)
#     ])


# @app.route('/pkgs/')
# def pkgs():
#     tree = fs_read('./app/pkgs')
#     body = generate_list('pkgs', tree)

#     return html_page(
#         'pkgs stats',
#         [
#             heading('pkgs statistics'),
#             body
#         ]
#     )

# def render_code(path, content):

#     a = '''
#         <h1>{header}</h1>
#         <hr>
#         <pre><code class="python">{code}</code></pre>
#         <hr>
#         <a href="/pkgs/">Back</a>
#     '''
#     file_name = path.split("/")[-1]
#     result = a.format(header=file_name, code=content)
#     return result



# @app.route('/test/<string:pkg>/')
# def run_test(pkg):
#     test_path = '.'.join(['app.pkgs', pkg, 'test'])
#     result = __import__(test_path)
#     result = getattr(result, pkg)
#     result = getattr(result, 'test')

#     return result.MainTest.run()

# Preferences