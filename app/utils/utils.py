from pkgs.html import Tag

heading = Tag('h4')
ul = Tag('ul')
li = Tag('li')
box = Tag('div')
link = Tag('a')

def render_dir(name, files_count, dirs, files):
	files_count = '({0})'.format(files_count)
	return box([heading([name, files_count]), ul([dirs,files])], class_name='tree')

def generate_files(files, path = []):
	s = ''
	# print(files)

	for i in files:
		ext = '/'.join(path + [i])
		file_path = '/file/{0}'.format(ext)
		run = ''

		if i == 'test.py':
			run = '..... <a href="{}">(▶ run test)</a>'.format('/test/' + '/'.join(path) + '/')
			# print('run', run, '\n')

		s += li([
			link(i, href=file_path),
			run
		])
	
	# print('s', s, '\n')
	return s


def generate_list(root_name, tree, path = []):
	# print('files:', tree['files'], '\n')
	files_count = len(tree['files'])

	files_items = generate_files(tree['files'], path)
	
	dirs_items = ''

	for dir_name in tree['dirs']:
		dirs_items += generate_list(
			dir_name, 
			tree['dirs'][dir_name],
			path + [dir_name]
		)
	res = render_dir(root_name, files_count, dirs_items, files_items)
	
	return res



