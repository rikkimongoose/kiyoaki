#!/usr/bin/python 
# -*- coding: utf-8 -*- 

import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from kiyoaki import *

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.out.write("""
          <html>
            <body>
              <h1>Kiyaki %s</h1>
              The natural languages generation toolkit. The source is availible <a href="http://github.com/rikkimongoose/kiyoaki">at GitHub</a>.<br /><br />
              <p>Generated surname is:</p>
              <pre>%s</pre>
              <hr />
              <p>The software is licensed with LGPL license. &copy; <a href="http://rikkimongoose.ru/">Rikki Mongoose</a>, 2013.</p>
            </body>
          </html>""" % (KiyoakiCore.get_ver(), KiyoakiCore.generate()))

application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
