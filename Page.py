class Page(object):
    def __init__(self, page_id, size):
        """
        size must be the same among all pages
        """
        self.page_id = page_id
        self.size = size

    def get_start_addr(self):
        return self.page_id * self.size
