import sys
if sys.version_info < (2, 7):
    print(sys.stderr, "{}: need Python 2.7 or later.".format(sys.argv[0]))
    print(sys.stderr, "Your Python is {}".format(sys.version))
    sys.exit(1)

from setuptools import setup, find_packages

setup(
    name = "python-json-logger",
    version = "0.1.9",
    url = "http://github.com/madzak/python-json-logger",
    license = "BSD",
    description = "A python library adding a json log formatter",
    author = "Zakaria Zajac",
    author_email = "zak@madzak.com",
    package_dir = {'': 'src'},
    packages = find_packages("src", exclude="tests"),
    test_suite = "tests.tests",
    install_requires = ['setuptools'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: System :: Logging',
    ]
)
