from setuptools import setup

setup(
    name='flatten_json',
    modules=['flatten_json'],
    version='0.1.7',
    description='Flatten JSON objects',
    author='Amir Ziai',
    author_email='arziai@gmail.com',
    url='https://github.com/amirziai/flatten',
    keywords=['json', 'flatten', 'pandas'],
    classifiers=[],
    entry_points={
        'console_scripts': ['flatten_json=flatten_json:cli']
    },
)
