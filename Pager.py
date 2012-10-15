from Singleton import Singleton
import Config

class Pager(object):
    __metaclass__ = Singleton

    def __init__(self, dbfile):
        self.dbfile = dbfile

    def extend_dbfile(self, n_pages_to_add):
        self.dbfile.n_pages += n_pages_to_add

    def commit_transaction(self, tx):
        """
        Number of seeks can be estimated by len(tx)
        """
        for op in tx.op_list:
            print(op)
