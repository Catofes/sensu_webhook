# -*- coding: UTF-8 -*-
import traceback
from wsgiref import simple_server

import RCallback
import falcon

import RRoute.middleware
import RUtils


class Route:
    @staticmethod
    def error_handle(ex, req, resp, params):
        if isinstance(ex, falcon.HTTPError):
            raise ex
        else:
            traceback.print_exc()
            raise RUtils.RError(0)

    def __init__(self):
        self.app = falcon.API(middleware=[
            middleware.RequireJSON(),
            middleware.JSONTranslator(),
        ]
        )
        self.app.add_error_handler(Exception, handler=Route.error_handle)
        restart = RCallback.RRestart()
        fire = RCallback.RFire()
        self.app.add_route('/restart', restart)
        self.app.add_route('/fire/{event}', fire)

    def run(self):
        httpd = simple_server.make_server('0.0.0.0', 8421, self.app)
        httpd.serve_forever()
