# Copyright (c) 2025 Ikuma Fukumoto
# This file is part of [your-project-name], released under the MIT License.
# See LICENSE file in the project root for full license information.

import http.cookiejar
from datetime import datetime, timedelta
import os
from importlib.resources import files
from typing import Optional
from colorama import Fore, init
from atcodertools.fileutils.artifacts_cache import get_cache_file_path
from atcodertools.client.atcoder import AtCoderClient, load_cookie_to

from atl.cookie import get_cookie_from_browser
init(autoreset=True)

class AtCoderToolsLogin:
    def __init__(self, browser: Optional[str] = None, profile: Optional[str] = None) -> None:
        self.browser: Optional[str] = browser
        self.profile: Optional[str] = profile
        self.at_default_cookie_file: str = "cookie.txt"
        self.atl_default_cookie_path = files("atl.cookie").joinpath("cookie.txt")
        client = AtCoderClient()
        self._client: AtCoderClient = client

    def login(self) -> None:
        # all of messages are in this function

        if self._check_logging_in():
            print(f"{Fore.GREEN}You are already logged in to AtCoder tools.")
            return
        else:
            print(f"{Fore.RED}You are not logged in to AtCoder tools.")
        
        # load atcoder-tools-login's default cookie file
        cookie_jar = http.cookiejar.LWPCookieJar(self.atl_default_cookie_path)
        cookie_jar.load(ignore_discard=True, ignore_expires=True)

        # update cookie expiration
        self._update_cookie_expiration(cookie_jar)

        # get REVEL_SESSION from browser if browser is specified
        if self.browser :
            cookie_value: str = get_cookie_from_browser(self.browser, self.profile)
            if cookie_value is None:
                print(f"{Fore.RED}Failed to get REVEL_SESSION from {self.browser}.")
                return

        # get REVEL_SESSION from user input
        else:
            cookie_value: str = input(
                f"Please enter the REVEL_SESSION manually.\n"
                f"if you need explanation, please visit {Fore.CYAN}https://kaiyou9.com/acc_and_oj_login_failed/{Fore.RESET}\n"
                f"REVEL_SESSION Cookie: "
            )
        
        # update REVEL_SESSION in cookie_jar
        self._update_cookie_REVEL_SESSION(cookie_jar, cookie_value)

        # save cookie_jar to atcoder-tools's default cookie file
        ac_tools_cookie_dir = get_cache_file_path("cookie.txt")
        cookie_jar.save(ac_tools_cookie_dir, ignore_discard=True, ignore_expires=True)
        os.chmod(ac_tools_cookie_dir, 0o600)
        print(f"{Fore.GREEN}Cookie updated successfully.")

        # check if the cookie is valid
        if self._check_logging_in():
            print(f"{Fore.GREEN}You are now logged in to AtCoder tools.")
        else:
            print(f"{Fore.RED}Failed to log in to AtCoder tools with the provided cookie.")
            print("Please check the REVEL_SESSION value and try again.")
            return
        
    def _check_logging_in(self) -> bool:
        load_cookie_to(self._client._session)
        # return False
        return self._client.check_logging_in()     

    def _update_cookie_expiration(self, cookie_jar: http.cookiejar.LWPCookieJar) -> None:
        # Calculate the date 6 months from now
        six_months_later = datetime.now() + timedelta(days=180)

        # Update the expiration of all cookies in the cookie_jar
        for cookie in cookie_jar:
            cookie.expires = int(six_months_later.timestamp())

    def _update_cookie_REVEL_SESSION(self, cookie_jar: http.cookiejar.LWPCookieJar, cookie_value: str) -> None:
        """
        Function to update the REVEL_SESSION cookie
        :param cookie_jar: http.cookiejar.LWPCookieJar object
        :param cookie_value: The value of the REVEL_SESSION to update
        """
        for cookie in cookie_jar:
            if cookie.name == "REVEL_SESSION":
                cookie.value = cookie_value
                break
