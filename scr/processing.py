from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    фильтрует список словарей по заданному значению
    :param data: список словарей
    :param state: значение по которому фильтруется (по умолчанию EXECUTED)
    :return: отфильтрованный список
    """
    return [item for item in data if item.get("state", "") == state]


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    сортирует список словарей по ключу date, либо возрастания или убывания
    :param data: список словарей
    :param reverse: если True то по убыванию, а если False то по возрастанию
    :return: отсортированный список словарей по дате
    """
    return sorted(data, key=lambda x: x.get("date", ""), reverse=reverse)
