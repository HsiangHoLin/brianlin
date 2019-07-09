from google.appengine.api import mail
import webapp2
import models
import time
import logging
import jinja2
import os

class FormHandler(webapp2.RequestHandler):
    def post(self):
        redirect_page = "http://practicalevangelism.net/sent-fail"
        try:
            tokens = self.request.path.split('/')
            index = 0
            text = None
            if tokens[1] == 'send':
                # /send/
                try:
                    admin = 'mymaydayya@gmail.com'
                    name = self.request.get('name')
                    email = self.request.get('email')
                    message = self.request.get('message')
                    if len(name) == 0 or len(email) == 0 or len(message) == 0:
                        redirect_page = "http://practicalevangelism.net/sent-error"
                    else:
                        my_email = 'practicalevangelism.net@gmail.com'
                        subject = '[PracticalEvangelism] ' + email
                        message = name + " (" + email + "): \n" + message
                        mail.send_mail(admin, my_email, subject, message)
                        redirect_page = "http://practicalevangelism.net/sent-ok"
                except:
                    pass
        except ValueError:
            # User entered a value that wasn't an integer. Ignore for now.
            pass

        time.sleep(1)
        self.redirect(redirect_page)

application = webapp2.WSGIApplication([('/send/', FormHandler)], debug=True)
