from pkgs.fs import fs_read

DIR = """
<h4> {dir_name} ({files_count})</h4>
<ul>
	{dirs}
	{files}
</ul>
"""


FILE = """
	<li class="file">
		<a href="{href}">{file_name}</a>
	</li>
"""

def generate_files(files, path = []):
	s = ""
	for i in files:
		file_path = '/file/' + '/'.join(path + [i])
		s += FILE.format(
			file_name=i,
			href=file_path,
		)

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

	return DIR.format(
		dir_name=root_name,
		files_count=files_count,
		dirs=dirs_items,
		files=files_items
	)



