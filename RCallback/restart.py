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
            p = subprocess.Popen(['/etc/init.d/sensu-api', 'restart'])
            p = subprocess.Popen(['/etc/init.d/sensu-server', 'restart'])
        except Exception:
            resp.result = falcon.HTTP_500

