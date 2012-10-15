from Record import *
import Config


class Page(object):
    def __init__(self, page_id, size):
        """
        size must be the same among all pages
        """
        self.data = {
            # start_addr: record,
            }
        # Meta data
        self.page_id = page_id
        self.size = size
        self.free_list = {
            # start_addr: 'vacant_size',
            # Sorted by vacant_size
            0: self.size,
            }

    def get_start_addr(self):
        return self.page_id * self.size

    def get_representative_vacant_space(self):
        v = sorted(self.free_list.items(), key=lambda x:x[1])[0][1]
        return v

    def add_record(self, record):
        self.get_representative_vacant_space()

        assert(isinstance(record, Record))
        # Change
        # - free_list (both for Page and dbfile)
        # - data
        demand_size = record.get_size()

        start_addr, vacant_size = self.alloc_record_space(demand_size)

        # Put data
        self.data[start_addr] = record

        # Shrink free space
        new_vacant_size = vacant_size - demand_size
        new_start_addr = start_addr + demand_size
        del self.free_list[start_addr]
        if new_vacant_size > 0:
            self.free_list[new_start_addr] = new_vacant_size

        # Sort free-list again
        # TODO: better sort (or insertion) algorithm
        # TODO: Sort here!

        print("Added record '%s'\ninto Page#%d, offset#%d\n"
              % (record.data, self.page_id, start_addr))

    def alloc_record_space(self, record):
        """
        @returns
        best offset within page
        """
        if Config.page['allocAlgorithm'] == "first fit":
            assert(False)  # TODO:
        elif Config.page['allocAlgorithm'] == "best fit":
            return self.alloc_best_fit(record)

    def alloc_best_fit(self, demand_size):
        """
        @returns
        best offset within page
        """
        # TODO: unsorted!! so it is first fit...
        # TODO: binary search
        for start_addr, vacant_size in self.free_list.items():
            # Sorted by smaller -> larger order
            if demand_size <= vacant_size:
                return start_addr, vacant_size

        # TODO: code for LARGE record
        assert(False)
