class Record(object):
    def __init__(self, data):
        assert(isinstance(data, str))
        self.data = data
        # Meta data
        self.list_next = None  # list maintainer for split record

    def extend_dbfile(self, n_pages_to_add):
        self.dbfile.n_pages += n_pages_to_add

    def commit_transaction(self, tx):
        """
        Number of seeks can be estimated by len(tx)
        """
        pass

    def get_size(self):
        return len(self.data)


def split_record(record, head_size):
    """
    @returns
    (head, tail)

    >>> h, t = split_record(Record('abc'), 2)
    >>> h.data
    'ab'
    >>> t.data
    'c'
    >>> h.list_next == t
    True
    """
    head = record
    tail = Record(record.data[head_size:])

    head.size = head_size
    head.data = record.data[:head_size]

    head.list_next = tail

    return (head, tail)


def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
