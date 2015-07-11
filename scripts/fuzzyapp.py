import datetime
import webapp2
import jinja2
import os
import logging
import json

import fuzzyengine

template_env = jinja2.Environment(autoescape = True, extensions = ['jinja2.ext.autoescape'], loader=jinja2.FileSystemLoader(os.getcwd()))

fuzzyengine.init()

with open('wordlist/list.txt', 'r') as f:
    for line in f:
        fuzzyengine.build(line)

class fuzzyHandler(webapp2.RequestHandler):
    def get(self):
        try:
            value = self.request.GET['q']
            result = fuzzyengine.search(value)
            j_result = json.dumps(result[:5])
        except:
            j_result = json.dumps([""])
        self.response.write(j_result)

application = webapp2.WSGIApplication([(r'/.*', fuzzyHandler)], debug=True)



