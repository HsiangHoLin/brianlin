import datetime
import webapp2
import jinja2
import os
import models
import logging

from google.appengine.api import users

template_env = jinja2.Environment(autoescape = True, extensions = ['jinja2.ext.autoescape'], loader=jinja2.FileSystemLoader(os.getcwd()))

models.set_default_admin('mymaydayya@gmail.com')
models.set_default_admin('test@example.com') # TODO
models.set_notfound_component()

class MainPage(webapp2.RequestHandler):
    def get(self):
        show_admin = False
        admin_info = None
        logout_url = users.create_logout_url('/')
        components = None

        path = self.request.path
        if path == '/admin_page' or path[:12] == '/admin_page/':
            admin_info = models.check_self_admin();
            if admin_info:
                show_admin = True

        if path == '/admin_page':
            path = '/'
        elif path[:12] == '/admin_page/':
            path = path[11:]

        tokens = path.split('/')

        if tokens[1] == '':
            sidebars = []
            try:
                cursor = None
                q = models.Page.query(models.Page.group == 'sidebar').order(models.Page.index)
                for i in range(3):
                    sidebar, cursor, more = q.fetch_page(10, start_cursor=cursor)
                    sidebars.append(sidebar)
                    if not more:
                        for j in range(2-i):
                            sidebars.append(None)
                        break;

            except:
                pass

            template = template_env.get_template('index.html')
            context = {
                'admin_info': admin_info,
                'show_admin': show_admin,
                'logout_url': logout_url,
                'navbar_pages': models.get_pages_by_group('navbar'),
                'sidebar_pages': models.get_pages_by_group('sidebar'),
                'function_pages': models.get_pages_by_group('function'),
                'components': models.get_component_query(models.MAIN_ID),
                'page_id': models.MAIN_ID,
                'this_url': self.request.url, 
                'sidebar_a': sidebars[0],
                'sidebar_b': sidebars[1],
                'sidebar_c': sidebars[2],         
            }
            self.response.out.write(template.render(context))
        else:
            page_id = models.NOTFOUND_ID
            page = models.get_page_by_slug(tokens[1])
            if page:
                page_id = page.key.id()

            template = template_env.get_template('base.html')
            context = {
                'admin_info': admin_info,
                'show_admin': show_admin,
                'logout_url': logout_url,
                'navbar_pages': models.get_pages_by_group('navbar'),
                'sidebar_pages': models.get_pages_by_group('sidebar'),
                'components': models.get_component_query(page_id),
                'page_id': page_id,
                'this_url': self.request.url,
            }
            self.response.out.write(template.render(context))


application = webapp2.WSGIApplication([(r'/.*', MainPage)], debug=True)



