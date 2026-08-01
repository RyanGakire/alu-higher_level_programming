# Python - Network #1

Scripts that consume HTTP APIs, first with `urllib`, then with `requests`.

| File | Package | Description |
| --- | --- | --- |
| `0-hbtn_status.py` | urllib | Fetches the intranet status page and displays the body |
| `1-hbtn_header.py` | urllib | Displays the `X-Request-Id` response header |
| `2-post_email.py` | urllib | POSTs an `email` parameter and displays the body |
| `3-error_code.py` | urllib | Displays the body, or `Error code:` on an HTTPError |
| `4-hbtn_status.py` | requests | Fetches the intranet status page and displays the body |
| `5-hbtn_header.py` | requests | Displays the `X-Request-Id` response header |
| `6-post_email.py` | requests | POSTs an `email` parameter and displays the body |
| `7-error_code.py` | requests | Displays the body, or `Error code:` for status >= 400 |
| `8-json_api.py` | requests | Searches a user and displays `[<id>] <name>` |
| `10-my_github.py` | requests | Displays a GitHub user id using Basic Authentication |

## Usage

```
./1-hbtn_header.py https://intranet.hbtn.io
./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
./10-my_github.py <username> <personal_access_token>
```

## Environment

* Ubuntu 14.04 LTS
* python3 (version 3.4.3)
* PEP 8 style (version 1.7)
