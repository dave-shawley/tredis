import setuptools

classifiers = ['Development Status :: 3 - Alpha',
               'Intended Audience :: Developers',
               'License :: OSI Approved :: BSD License',
               'Operating System :: OS Independent',
               'Programming Language :: Python :: 2',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Programming Language :: Python :: 3.3',
               'Programming Language :: Python :: 3.4',
               'Programming Language :: Python :: 3.5',
               'Programming Language :: Python :: Implementation :: CPython',
               'Programming Language :: Python :: Implementation :: PyPy',
               'Topic :: Communications', 'Topic :: Internet',
               'Topic :: Software Development :: Libraries']

requirements = ['tornado>4.0']
tests_require = ['nose', 'mock', 'codecov', 'coverage']

setuptools.setup(name='tredis',
                 version='0.1.0',
                 description='An simple asynchronous Redis client for Tornado',
                 long_description=open('README.rst').read(),
                 author='Gavin M. Roy',
                 author_email='gavinmroy@gmail.com',
                 url='http://github.com/gmr/tredis',
                 py_modules=['tredis'],
                 package_data={'': ['LICENSE', 'README.rst']},
                 include_package_data=True,
                 install_requires=requirements,
                 tests_require=tests_require,
                 license=open('LICENSE').read(),
                 classifiers=classifiers)