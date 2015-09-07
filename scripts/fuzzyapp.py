import datetime
import webapp2
import jinja2
import os
import logging
import json

import fuzzyengine

template_env = jinja2.Environment(autoescape = True, extensions = ['jinja2.ext.autoescape'], loader=jinja2.FileSystemLoader(os.getcwd()))

engine = fuzzyengine.init()
engine.load('wordlist/list.txt')

class fuzzyHandler(webapp2.RequestHandler):
    def get(self):
        try:
            value = self.request.GET['q']
            result = engine.search(value)
            j_result = json.dumps(result[:5])
        except:
            j_result = json.dumps([""])
        self.response.write(j_result)

application = webapp2.WSGIApplication([(r'/.*', fuzzyHandler)], debug=True)



