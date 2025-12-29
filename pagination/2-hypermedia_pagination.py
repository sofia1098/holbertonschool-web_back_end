#!/usr/bin/env python3
""" Simple function for pagination. """
import csv
from typing import List
from math import ceil


def index_range(page: int, page_size: int) -> tuple:
    """Funcion que retorna una tupla con el comienzo y final."""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of the dataset."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Return A dict with the data of the page."""
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = ceil(total_intems / page_size)
        next_page = page + 1 if page < total_pages else None
        prev = page - 1 if page > 1 else None

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev,
            "total_pages": total_pages,
        }
