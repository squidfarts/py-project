#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: install.py                                                                #
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
import subprocess
import sys, os

subprocess.check_call(["pip3", "install", "codecov", "pytest"])