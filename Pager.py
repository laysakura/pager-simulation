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
            if op['type'] == 'insert':
                self._commit_insert_tx(op)
            elif op['type'] == 'delete':
                self._commit_delete_tx(op)
            else:
                assert(False)

    def _commit_insert_tx(self, op):
        record = op['record']
        print("inserting: " + record.data)

        # If necessary (record size is larger than page size),
        # split record if it exceeds page boundary (or even space?)

        # Find page to insert record

        # If no page found, extend dbfile

        # Find best_id!!
        best_id = 0

        self.dbfile.get_page(best_id).add_record(record)

    def get_free_page_list(self):
        return self.dbfile.free_page_list
