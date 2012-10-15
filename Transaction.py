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
        # Split record if it exceeds page boundary (or even space?)
        op = {
            'type': 'insert',
            'data': record,
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
    tx.add_insert_op("abcdefg")
    return tx

def aggr_tx(pager, tx):
    return tx
