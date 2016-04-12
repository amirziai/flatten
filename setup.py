from distutils.core import setup
from Cython.Build import cythonize

setup(
	name = 'flatten',
	packages = ['flatten'],
	version = '0.1',
	description = 'Flatten JSON objects',
	author = 'Amir Ziai',
	author_email = 'arziai@gmail.com',
	url = 'https://github.com/amirziai/flatten',
	download_url = '...',
	keywords = ['json', 'flatten', 'pandas'],
	classifiers = [],
    ext_modules = cythonize("flatten.pyx")
)