import os
from typing import Callable, Dict, Iterable, Optional, List

from functions import filter_query, unique_query, limit_query, map_query, sort_query, regex_query

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

CMS_TO_FUNCTIONS: Dict[str, Callable] = {
    'filter': filter_query,
    'unique': unique_query,
    'limit': limit_query,
    'map': map_query,
    'sort': sort_query,
    'regex': regex_query,
}


def read_file(file_name: str) -> Iterable[str]:
    with open(file_name) as file:
        for line in file:
            yield line


def build_query(cmd: str, value: str, file_name: str, data: Optional[Iterable[str]]) -> List[str]:
    if data is None:
        prepared_data: Iterable[str] = read_file(DATA_DIR + os.sep + file_name)
    else:
        prepared_data = data

    return list(CMS_TO_FUNCTIONS[cmd](value=value, data=prepared_data))
