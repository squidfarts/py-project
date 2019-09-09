#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: setup.py                                                                  #
#                                                                                 #
# AUTHOR: Michael Brockus.                                                        #
#                                                                                 #
# CONTACT: <mailto:michaelbrockus@squidfarts.com>                                 #
#                                                                                 #
# NOTICES:                                                                        #
#                                                                                 #
# License: Apache 2.0 :http://www.apache.org/licenses/LICENSE-2.0                 #
#                                                                                 #
###################################################################################
import setuptools, setup
import sys

if sys.version_info < (3, 5, 0):
    print('Tried to install with an unsupported version of Python.'
          'Project requires Python 3.5.0 or greater')
    sys.exit(1)


entries = {'console_scripts': ['pyexe=src.main.module.main:main']}

setup(
    name='py-project',
    version='0.1.0',
    description='Python project',
    author='Michael Brockus',
    author_email='michaelbrockus@squidfarts.com',
    python_requires='>=3.5',
    license='Apache-2.0',
    include_package_data=True,
    zip_safe=True,
    entry_points=entries,
    packages=['src.main', 'src.main.module']
)