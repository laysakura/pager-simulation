from Singleton import Singleton

class DbFile(object):
    """
    Represents a database file (like foo.sqlite)
    """
    __metaclass__ = Singleton

    def __init__(self, page_size, init_n_pages):
        self.page_sz = page_size
        self.n_pages = init_n_pages
