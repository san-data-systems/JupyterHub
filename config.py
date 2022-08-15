import os, pwd, subprocess

c.JupyterHub.authenticator_class = 'jupyterhub.auth.APIAuthenticator'
c.JupyterHub.base_url = '/{}'.format(os.environ['PROJECT'])
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8888
def pre_spawn_hook(spawner):
    username = spawner.user.name
    try:
        pwd.getpwnam(username)
    except KeyError:
        subprocess.check_call(['useradd', '-ms', '/bin/bash', username])

c.Spawner.pre_spawn_hook = pre_spawn_hook
c.Authenticator.allowed_users = set((os.environ['USERS']).split(","))
c.Authenticator.post_auth_hook = None