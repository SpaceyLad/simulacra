import os
"""
How to add the key to the machine registry (Windows).

1. Change the key value with something unique and long.

2. In the virtual enviroment, run the following:

Linux
export JWT_SECRET_KEY="change_me"

Windows Powershell
$env:JWT_SECRET_KEY = "change_me"

3. Run the web gui and log in as a test user. If you get an "invalid token" error message, something is wrong.

4. When it works, delete the key from this setup. It should stay hidden on the server.

3.2. Plan B: Hardcode the secret key with the line under this one. This is not recommended and should not be used in production.

secret_key = "change_me"
"""

# username:password
users = {
    "admin": "admin",
    "test": "test"
}

# username:group
groups = {
    "admin": "admin",
    "test": "user"
}

secret_key = os.environ.get('JWT_SECRET_KEY')
secret_key = "change_me"