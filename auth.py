class APIAuthenticator(Authenticator):

    async def authenticate(self, handler, data):
        """Checks against a global password if it's been set. If not, allow any user/pass combo"""
        import requests, os
        url = "{}/api/v1/login".format(os.environ['API'])
        if data['username'] == "" and data['password'] == "":
            return None
        payload = {"username": data["username"],"password": data["password"]}
        response = requests.post(url, json=payload)
        if response.status_code == 201:
            return data['username']
        else:
            None

