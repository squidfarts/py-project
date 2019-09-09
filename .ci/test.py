#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: test.py                                                                   #
#                                                                                 #
# AUTHOR: Michael Brockus.                                                        #
#                                                                                 #
# CONTACT: <mailto:michael@squidfarts.com>                                        #
#                                                                                 #
# NOTICES:                                                                        #
#                                                                                 #
# License: Apache-2.0                                                             #
#                                                                                 #
###################################################################################
from os.path import join as join_paths
import subprocess, os


subprocess.check_call(['pytest', join_paths('src', 'test', 'cases', 'test.py')])

os.chdir(join_paths('src', 'main', 'module'))
subprocess.check_call(['codecov', 'run', 'main.py'])