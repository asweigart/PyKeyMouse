import re
from setuptools import setup

# Load version from module (without loading the whole module)
with open('pykeymouse/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

# Read in the README.md for the long description.
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='PyKeyMouse',
    version=version,
    url='https://github.com/asweigart/pykeymouse',
    author='Al Sweigart',
    author_email='al@inventwithpython.com',
    description=('A simple, cross-platform Python 2/3 module to detect mouse and keyboard input.'),
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='BSD',
    packages=['pykeymouse'],
    test_suite='tests',
    install_requires=[],
    keywords="gui automation test testing keyboard mouse cursor click press keystroke control hook keylogger",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7'
    ],
)