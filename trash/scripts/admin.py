import datetime
import webapp2
import jinja2
import os
import models

from google.appengine.api import users

template_env = jinja2.Environment( loader=jinja2.FileSystemLoader(os.getcwd()))

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('index.html')
        #context = {
        #    'current_time': current_time,
        #    'user': user,
        #    'login_url': login_url,
        #    'logout_url': logout_url,
        #    'userprefs': userprefs,
        #}
        #self.response.out.write(template.render(context))
        self.response.out.write("hello")

application = webapp2.WSGIApplication([('/', MainPage)], debug=True)



