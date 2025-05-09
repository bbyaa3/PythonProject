def filter_by_state(data, state='EXECUTED'):
    """
    фильтрует список словарей по заданному значению
    :param data: список словарей
    :param state: значение по которому фильтруется (по умолчанию EXECUTED)
    :return: отфильтрованный список
    """
    return [item for item in data if item.get('state') == state]

def sort_by_date(data, reverse=True):
    """
    сортирует список словарей по ключу date, либо возрастания или убывания
    :param data: список словарей
    :param reverse: если True то по убыванию, а если False то по возрастанию
    :return: отсортированный список словарей по дате
    """
    return  sorted(data, key=lambda x: x.get('date'),reverse=reverse)
print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))