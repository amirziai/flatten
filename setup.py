from setuptools import setup


setup(
    name='flatten_json',
    py_modules=['flatten_json', 'util'],
    version='0.1.8',
    description='Flatten JSON objects',
    license='MIT',
    author='Amir Ziai',
    author_email='arziai@gmail.com',
    url='https://github.com/amirziai/flatten',
    keywords=['json', 'flatten', 'pandas'],
    classifiers=[],
    entry_points={
        'console_scripts': ['flatten_json=flatten_json:cli']
    },
    install_requires=['six'],
)
