#!/usr/bin/env python

import Config
from Pager import Pager
from DbFile import DbFile
from Transaction import *

if __name__ == '__main__':
    db = DbFile(Config.pager["pageSize"],
                Config.pager["initNumPages"])
    pager = Pager(db)

    n_tx = 3
    for i in range(n_tx):
        tx = gen_tx()
        tx = aggr_tx(pager, tx)
        pager.commit_transaction(tx)
