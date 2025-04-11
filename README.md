
# atcoder-toolsでログイン可能に

`atcoder-tools`では、`AtCoder`のreCAPTCHA導入により現在の仕様ではログインできない場合があります。
ログイン済みブラウザのcookieを設定することで本問題は解決できますが、2025/04/09時点で`atcoder-tools`にそのような機能は実装されていません。
より厳密には、cookieを保存する内部処理は存在しますが、ユーザがコマンドラインからこれを更新する手段が存在しません。
本リポジトリでは、`atcoder-tools`内部のcookieを強制的に更新する方法を提供します。

## Install with pip

```bash
pip install git+https://https://github.com/FukumotoIkuma/atcoder-tools_login
```

## How to use

You have 3 options to use atcoder-tools-login, load cooke from Chrome, firefox, or input manually.

---

### Method1. Load cookie from Chrome browser


1. Login to [AtCoder](https://atcoder.jp).
2. Run atcoder-tools-login by next command.  

    ```bash
    atl chrome
    ```

    if you login some AtCoder Accounts on Chrome, please see step4, or use Method 3.
3. Enter your keychain password twice (defaults to login password).  
if you don't wanna input keychain password, please use method 3.

4. Check your user profile by visiting [Chrome://version](Chrome://version) and check `Profile Path` to know your profile.  
for example, mac os, you will find `/Users/user/Library/Application Support/Google/Chrome/Default`, and this profile is `Default`.

5. Run atcoder-tools-login by next command. and back to step 3.

    ```bash
    atl chrome {Profile}
    ```

---

### Method2. Load cookie from FireFox browser

1. Login to [AtCoder](https://atcoder.jp).
2. Run atcoder-tools-login by next command.  

    ```bash
    atl firefox
    ```

    if you login some AtCoder Accounts on FireFox, please see step4, or use Method 3.
3. Enter your keychain password twice (defaults to login password).  
if you don't wanna input keychain password, please use method 3.

4. Check your user profile by visiting [about:support](about:support) and check `Profile Path` to know your profile.  
for example, mac os, you will find `/Users/user/Library/Application Support/FireFox/Profiles/xxxxxxxx.default-release`, and this profile is `xxxxxxxx.default-release`.

5. Run atcoder-tools-login by next command. and back to step 3.

    ```bash
    atl firefox {Profile}
    ```

---

### Method3. Input cookie by yourself

1. Login to [AtCoder](https://atcoder.jp).
2. Copy the REVEL_SESSION value from the cooki  e
(Instructions for Chrome and FireFox are below)
3. Run atcoder-tools-login by next command.  

    ```bash
    atl
    ```

4. Paste REVEL_SESSION value

---

### How to copy Cookie on Chrome

1. Login to [AtCoder](https://atcoder.jp).

2. open dev-tools  
see [here](https://developer.chrome.com/docs/devtools/open#chrome-menu)

3. open cookies  
see [here](https://developer.chrome.com/docs/devtools/application/cookies)

4. copy REVEL_SESSION value

---

### How to copy Cookie on FireFox

wait for update

## Don't wanna use atcoder-tools-login?

Don't worry, you can do everything manually.

1. Open atcoder-tools's cookie file.  
`~/.local/share/atcoder-tools/cookie.txt`

2. Paste this cookie.

    ```.txt
    #LWP-Cookies-2.0
    Set-Cookie3: REVEL_FLASH=""; path="/"; domain="atcoder.jp"; path_spec; secure; discard; HttpOnly=None; version=0
    Set-Cookie3: REVEL_SESSION=""; path="/"; domain="atcoder.jp"; path_spec; secure; expires="2025-10-06 10:09:30Z"; HttpOnly=None; version=0
    ```

3. Overwrite `expires="2025-10-06 10:09:30Z";`.
about 6 month later.

4. Copy REVEL_SESSION value from AtCoder(see above).

5. Overwrite `REVEL_SESSION="";`.
