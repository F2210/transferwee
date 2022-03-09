import os
from setuptools import find_packages, setup

short_description = 'An application to up and download files to and from wetransfer '

try:
    import pypandoc

    long_description = pypandoc.convert('README.md', 'rst')
except ModuleNotFoundError:
    long_description = short_description

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

install_requirements = [
    "requests",
]

setup(
    name='transferwee',
    version='1.0.3',
    packages=find_packages(),
    install_requires=install_requirements,
    include_package_data=True,
    license='No rights',
    description=short_description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/iamleot/transferwee',
    author='Leonardo Taccari',
    author_email='',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
