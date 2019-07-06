#!/usr/bin/env python
import logging
import os
import subprocess
import sys
import glob
import re

import time
import datetime
import pytz
import math

import base64
from binascii import a2b_base64
from decimal import Decimal

from itertools import chain

import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import tornado.log
import tornado.escape

import json, csv, urllib
import numpy as np

class WebSocketHandler(tornado.websocket.WebSocketHandler):

    def on_message(self, message):
        msg = tornado.escape.json_decode( message )

        if msg['msgID'] == '1':
            files = []
            directory = sys.argv[1]
            for f in os.listdir(directory):
                if f[-4:] in [".png", ".jpg"]:
                    files.append(directory + f)
            
            files = sorted(files)

            parcel = {'msgID': "1",
                      'fileList': str(files)}

            self.write_message(tornado.escape.json_encode(parcel))

        elif msg['msgID'] == '2':
            fp = open(msg['fname'], "w")
            fp.close()

        elif msg['msgID'] == '3':
            fp = open(msg['fname'], "a")
            fp.write(msg['msg'])
            fp.close()

    def on_close(self):
        pass


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/websocket', WebSocketHandler),
            (r'/(.*)', tornado.web.StaticFileHandler, {'path': '.', 'default_filename': ''}),
        ]
 
        settings = {
            'template_path': 'templates'
        }
        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    listen_address = ''
    listen_port = 8080

    '''
    try:
        if len(sys.argv) == 2:
            listen_port = int(sys.argv[1])
        elif len(sys.argv) == 3:
            listen_address = sys.argv[1]
            listen_port = int(sys.argv[2])
        assert 0 <= listen_port <= 65535
    except (AssertionError, ValueError):
        raise ValueError('Port must be a number between 0 and 65535')
    '''

    args = sys.argv
    args.append("--log_file_prefix=myapp.log")
    tornado.log.enable_pretty_logging()
    tornado.options.parse_command_line(args)
    
    ws_app = Application()
    http_server = tornado.httpserver.HTTPServer(ws_app)
    http_server.listen(listen_port)

    # Logging
    logging.info('Listening on %s:%s' % (listen_address or '[::]' if ':' not in listen_address else '[%s]' % listen_address, listen_port))
    # [James]
    # Uncomment these lines to suppress normal webserver output
    #logging.getLogger('tornado.access').disabled = True
    #logging.getLogger('tornado.application').disabled = True
    #logging.getLogger('tornado.general').disabled = True

    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
