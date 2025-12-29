#!/usr/bin/env python3
""" Simple function for pagination. """


def index_range(page: int, page_size: int) -> tuple:
    """Funcion que retorna una tupla con el comienzo y final."""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
