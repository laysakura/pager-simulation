from Record import Record
import random
import my_random
import Config


class Transaction(object):
    """
    Here, `Transaction' means a bulk of requests to pager
    """
    def __init__(self):
        self.op_list = []

    def add_insert_op(self, record):
        """
        @param
        record_str can be aggregated
        """
        assert(isinstance(record, Record))

        op = {
            'type': 'insert',
            'record': record,
            }
        self.op_list.append(op)

    def add_select_op(self, page_id, page_offset, length):
        """
        @note
        Fetch op. comes one page by page.
        For instance,
            SELECT * FROM T;
        causes:
        1. Read metadata for T and find root page of it
        2. Traverse B-tree for T
        3. request a page for a tree node

        @retuns
        Requested data.
        Note that it sometimes returns multiple records
        (when transaction is aggregated)
        """
        pass

    def add_delete_op(self):
        pass


def gen_tx():
    tx = Transaction()
    d_length = int(
        random.gauss(Config.record['meanLength'],
                     Config.record['variantLength'])) # TODO: OK for Gaussian?
    if d_length < 1:
        d_length = 1
    data = my_random.randstr(d_length)
    tx.add_insert_op(Record(data))
    return tx

def aggr_tx(pager, tx):
    return tx
