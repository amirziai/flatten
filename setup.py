from setuptools import setup

# For release: `python -m pip install build && python -m build .`
# The upload both the sdist and wheel under ./dist

setup(
    name='flatten_json',
    packages=['flatten_json'],
    version='0.1.14',
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
