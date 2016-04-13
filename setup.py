from distutils.core import setup
#from Cython.Build import cythonize


# with open('README.md') as f:
# 	readme = f.read()


# with open('LICENSE') as f:
# 	license = f.read()

setup(
	name = 'flatten_json',
	packages = ['flatten_json'],
	version = '0.1.2',
	description = 'Flatten JSON objects',
#	long_description = readme,
	author = 'Amir Ziai',
	author_email = 'arziai@gmail.com',
	url = 'https://github.com/amirziai/flatten',
#	download_url = '...',
	keywords = ['json', 'flatten', 'pandas'],
#	license=license,
	classifiers = [],
#    ext_modules = cythonize("flatten_json/flatten_json.pyx")
)