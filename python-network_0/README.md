# API advanced / cURL

Bash scripts using `curl` to interact with a web server. Each script takes a URL
as its first argument and is tested against the web server running on port 5000.

| File | Description |
| --- | --- |
| `0-body_size.sh` | Displays the size of the response body in bytes |
| `1-body.sh` | Sends a GET request and displays the body of a 200 response only |
| `2-delete.sh` | Sends a DELETE request and displays the response body |
| `3-methods.sh` | Displays all HTTP methods the server accepts for the URL |
| `4-header.sh` | Sends a GET request with the header `X-HolbertonSchool-User-Id: 98` |
| `5-post_params.sh` | Sends a POST request with the `email` and `subject` variables |

## Usage

```
./0-body_size.sh 0.0.0.0:5000
```

## Environment

* Ubuntu 20.04 LTS
* Bash
