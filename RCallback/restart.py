import RUtils
import subprocess
import falcon


class RRestart:
    def __init__(self):
        pass

    def on_post(self, req, resp):
        if 'key' not in req.params.keys():
            raise RUtils.RError(2)
        if req.params['key'] != RUtils.RConfig().restart_key:
            raise RUtils.RError(2)
        try:
            if subprocess.call('cd /etc/sensu/conf.d; git pull;', shell=True):
                raise Exception
            if subprocess.call('/etc/init.d/sensu-api restart', shell=True):
                raise Exception
            if subprocess.Popen('/etc/init.d/sensu-server restart', shell=True):
                raise Exception
        except Exception:
            resp.status = falcon.HTTP_500
