import webapp2
import models
import time
import logging
from google.appengine.api import mail

class FormHandler(webapp2.RequestHandler):
    def post(self):
        redirect_page = '/admin_page'
        try:
            tokens = self.request.path.split('/')
            index = 0
            text = None
            if tokens[2] == 'page':
                # /admin_page/page/action/page_group/[page_key_id]
                page_group = tokens[4]
                if tokens[3] == 'add':
                    index = int(self.request.get('page-index'))
                    text = self.request.get('page-text')
                    if tokens[4] == 'function':
                        text = "function page"
                    slug = self.request.get('page-slug')
                    if len(text) > 0 and len(slug) > 0:
                        models.set_page(page_group, index, text, slug)
                elif tokens[3] == 'delete':
                    key_id = tokens[5]
                    models.delete_page(key_id)
                elif tokens[3] == 'update':
                    key_id = tokens[5]
                    index = self.request.get('page-index')
                    text = self.request.get('page-text')
                    slug = self.request.get('page-slug')
                    models.update_page(key_id, index, text, slug)
            elif tokens[2] == 'component':
                # /admin_page/component/action/page_key_id/[self_key_id]                
                page_key_id = int(tokens[4])

                p = models.get_page_by_id(page_key_id)
                if p:
                    redirect_page = redirect_page + '/' + p.slug

                if tokens[3] == 'add':
                    index = int(self.request.get('component-index'))
                    head = self.request.get('component-head')
                    body = self.request.get('component-body')
                    html = self.request.get('component-html')
                    models.set_page_component(page_key_id, index, head, body, html)
                if tokens[3] == 'update':
                    key_id = tokens[5]
                    index = self.request.get('component-index')
                    head = self.request.get('component-head')
                    body = self.request.get('component-body')
                    html = self.request.get('component-html')
                    models.update_component(key_id, index, head, body, html)
                if tokens[3] == 'delete':
                    key_id = tokens[5]
                    models.delete_component(key_id)

        except ValueError:
            # User entered a value that wasn't an integer. Ignore for now.
            pass

        time.sleep(1)
        self.redirect(redirect_page)

application = webapp2.WSGIApplication([(r'/form.*', FormHandler)], debug=True)
