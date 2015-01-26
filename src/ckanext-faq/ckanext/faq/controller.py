from ckan.lib.base import BaseController
import ckan.plugins as p

c = p.toolkit.c
render = p.toolkit.render

class FAQController(BaseController):

    def index(self):
        return render('faq/index.html')
