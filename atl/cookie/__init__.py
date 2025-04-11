# Copyright (c) 2025 Ikuma Fukumoto
# This file is part of [your-project-name], released under the MIT License.
# See LICENSE file in the project root for full license information.

import platform
import glob
import os
import browsercookie
from typing import Optional, List

def _chrome(profile: str = "*") -> str:
    # get the path to the user's chrome cookie file
    user_home = os.path.expanduser("~")

    if platform.system() == 'Windows':
        return  os.path.join(user_home, 'AppData', 'Local', 'Google', 'Chrome', 'User Data', profile, 'Cookies')
    elif platform.system() == 'Darwin':  # macOS
        return  os.path.join(user_home, 'Library', 'Application Support', 'Google', 'Chrome', profile, 'Cookies')
    elif platform.system() == 'Linux':
        return  os.path.join(user_home, '.config', 'google-chrome', profile, 'Cookies')
    else:
        raise Exception("Unsupported OS")
    
def _firefox(profile: str = "*") -> str:
    user_home = os.path.expanduser("~")

    if platform.system() == 'Windows':
        return os.path.join(user_home, 'AppData', 'Roaming', 'Mozilla', 'Firefox', 'Profiles', profile, 'cookies.sqlite')
    elif platform.system() == 'Darwin':  # macOS
        return os.path.join(user_home, 'Library', 'Application Support', 'Mozilla', 'Firefox', 'Profiles', profile, 'cookies.sqlite')
    elif platform.system() == 'Linux':
        return os.path.join(user_home, '.mozilla', 'firefox', profile, 'cookies.sqlite')
    else:
        raise Exception("Unsupported OS")


def get_cookie_from_browser(browser: str, profile: str = "*") -> Optional[str]:
    """
    Get the atCoder cookie from the browser.
    Args:
        browser (str): The browser to get the cookie from. Can be 'chrome', 'firefox', or 'edge'.
        profile (str): The browser profile to use. Defaults to '*'.
    Returns:
        Optional[str]: The atCoder cookie.
    """
    func = {
        'chrome': {"path": _chrome, "browser": browsercookie.chrome},
        'firefox': {"path": _firefox, "browser": browsercookie.firefox},
    }
    if browser not in func.keys():
        raise Exception("Unsupported browser. Only 'chrome' and 'firefox' are supported.")
    pattern: str =  func[browser]["path"](profile=profile)

    paths: List[str] = glob.glob(pattern) if profile == '*' else [pattern]
    
    cj = func[browser]["browser"](paths)

    # filter the cookies to get the REVEL_SESSION cookie
    atcoder_cookies: List[browsercookie.Cookie] = [
        cookie for cookie in cj if cookie.domain in [".atcoder.jp", "atcoder.jp"] and cookie.name == "REVEL_SESSION"
    ]
    if len(atcoder_cookies) == 0:
        return None
    else:
        return atcoder_cookies[0].value


