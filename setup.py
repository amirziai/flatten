from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='flatten_json',
    py_modules=['flatten_json', 'util'],
    version='0.1.7',
    description='Flatten JSON objects',
    # long_description=readme(),
    license='MIT',
    author='Amir Ziai',
    author_email='arziai@gmail.com',
    url='https://github.com/amirziai/flatten',
    keywords=['json', 'flatten', 'pandas'],
    classifiers=[],
    entry_points={
        'console_scripts': ['flatten_json=flatten_json:cli']
    },
)
