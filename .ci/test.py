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
import subprocess


subprocess.check_call(['pytest', join_paths('src', 'test', 'cases', 'test.py')])
subprocess.check_call(['codecov', 'run', join_paths('src', 'main', 'module', 'main.py')])
subprocess.check_call(['codecov', 'run', join_paths('src', 'test', 'cases', 'test.py')])