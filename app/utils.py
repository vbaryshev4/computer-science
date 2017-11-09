from pkgs.fs import fs_read
from pkgs.html import Tag

heading = Tag('h4')
ul = Tag('ul')
li = Tag('li')
box = Tag('div')
link = Tag('a')

def renderDir(name, files_count, dirs, files):
	return box([
		heading([name, '(' + files_count + ')']),
		ul([
			dirs,
			files
		])
	], class_name='tree')

def generate_files(files, path = []):
	s = ""

	for i in files:
		file_package_path = '/'.join(path + [i])
		file_path = '/file/' + file_package_path
		run = ''

		if i == 'test.py':
			run = '..... <a href="{}">(▶ run test)</a>'.format('/test/' + '/'.join(path) + '/')

		s += li([
			link(i, href=file_path),
			run
		])

	return s


def generate_list(root_name, tree, path = []):
	print(tree)

	files_count = len(tree['files'])

	files_items = generate_files(tree['files'], path)
	
	dirs_items = ''

	for dir_name in tree['dirs']:
		dirs_items += generate_list(
			dir_name, 
			tree['dirs'][dir_name],
			path + [dir_name]
		)

	return renderDir(root_name, str(files_count), dirs_items, files_items)



