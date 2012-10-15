#!/usr/bin/env python

import Config
from Pager import Pager
from DbFile import DbFile
from Transaction import *
import random

if __name__ == '__main__':
    db = DbFile(Config.pager["pageSize"],
                Config.pager["initNumPages"])
    pager = Pager(db)

    random.seed(1)
    n_tx = 3000
    for i in range(n_tx):
        tx = gen_tx()
        tx = aggr_tx(pager, tx)
        pager.commit_transaction(tx)
