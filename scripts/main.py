import datetime
import webapp2
import jinja2
import os
import logging

template_env = jinja2.Environment(autoescape = True, extensions = ['jinja2.ext.autoescape'], loader=jinja2.FileSystemLoader(os.getcwd()))

class MainPage(webapp2.RequestHandler):
    def get(self):

        path = self.request.path
        tokens = path.split('/')

        if len(tokens) > 2:
            self.response.write("Not Found")
        else:
            try:
                template = template_env.get_template('public/' + tokens[1] + '.html')
                self.response.write(template.render())
            except:
                self.response.write("Not Found: " + tokens[1])

application = webapp2.WSGIApplication([(r'/.*', MainPage)], debug=True)



