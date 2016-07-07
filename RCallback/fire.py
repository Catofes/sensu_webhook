import RUtils
import urllib2
import falcon
import json


class RFire:
    def __init__(self):
        pass

    def on_post(self, req, resp, event):
        if 'key' not in req.params.keys():
            raise RUtils.RError(2)
        if req.params['key'] != RUtils.RConfig().fire_key:
            raise RUtils.RError(2)
        try:
            data = json.dumps({'check': event})
            request = urllib2.Request('http://127.0.0.1/request', data)
            response = urllib2.urlopen(request)
            response_data = response.read()
            if response.code != 200:
                resp.result = falcon.HTTP_500
                return
        except Exception:
            resp.result = falcon.HTTP_500
