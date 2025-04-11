# Copyright (c) 2025 Ikuma Fukumoto
# This file is part of [your-project-name], released under the MIT License.
# See LICENSE file in the project root for full license information.


import sys
from atl import AtCoderToolsLogin

def main():
    if len(sys.argv) > 2:
        browser = sys.argv[1]
        profile = sys.argv[2]
    elif len(sys.argv) > 1:
        browser = sys.argv[1]
        # TODO: firefox default profile
        profile = "*"
    else:
        browser, profile = None, None


    atl_login = AtCoderToolsLogin(browser=browser, profile=profile)
    atl_login.login()

if __name__ == "__main__":
    main()