from Singleton import Singleton
import Config
import operator


class Pager(object):
    __metaclass__ = Singleton

    def __init__(self, dbfile):
        self.dbfile = dbfile

    def extend_dbfile(self, n_pages_to_add):
        self.dbfile.n_pages += n_pages_to_add

    def get_free_list(self):
        return self.dbfile.free_page_list

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

        # If necessary (record size is larger than page size),
        # split record if it exceeds page boundary (or even space?)

        # Find page to insert record

        # If no page found, extend dbfile

        # Find best_id!!
        best_page_id = 777

        # TODO: Add best fit algorithm
        # First
        demand_size = record.get_size()
        for page_id, repr_vacant_size in enumerate(self.get_free_list()):
            # Sorted by smaller -> larger order
            if demand_size <= repr_vacant_size:
                best_page_id = page_id
                break

        print("demand_size=%d, page#%d.size()=%d"
              % (demand_size, best_page_id, repr_vacant_size))
        self.dbfile.get_page(best_page_id).add_record(record)
        # shrink repr_vacant_size
        print(best_page_id)
        self.dbfile.free_page_list[best_page_id] = max(self.dbfile.get_page(best_page_id).free_list.iteritems(), key=operator.itemgetter(1))[1]

    def get_free_page_list(self):
        return self.dbfile.free_page_list
