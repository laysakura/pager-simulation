from Singleton import Singleton
from Page import *

class DbFile(object):
    """
    Represents a database file (like foo.sqlite)
    """
    __metaclass__ = Singleton

    def __init__(self, page_size, init_n_pages):
        self.page_sz = page_size
        self.page_list = [Page(i, page_size) for i in range(init_n_pages)]  # page_id -> Page
        self.free_page_list = [page_size for i in range(init_n_pages)] # page_id -> representative space value

    def get_page(self, page_id):
        return self.page_list[page_id]
