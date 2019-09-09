#!/user/bin/env python3
###################################################################################
#                                                                                 #
# NAME: py-project.py                                                             #
#                                                                                 #
# AUTHOR: Michael Brockus.                                                        #
#                                                                                 #
# CONTACT: <mailto:michael@squidfarts.com>                                        #
#                                                                                 #
# NOTICES:                                                                        #
#                                                                                 #
# License: Apache 2.0 :http://www.apache.org/licenses/LICENSE-2.0                 #
#                                                                                 #
###################################################################################
from src.main.module.main import main
import sys


if __name__ == "__main__":
    sys.exit(main(sys.argv))
