from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    '''
    Маскирует номера счета.

    Аргументы:
    account_info (str): состоит из счета или название карты и номер

    Возвращает:
    str: маскированный номер счета или карты
    '''

    if account_info[:5].lower() == "счет":
        return account_info[:6] + get_mask_account(int(account_info[6:]))
    else:
        return account_info[:-12] + get_mask_card_number(int(account_info[-12:]))


def get_date(date: str) -> str:
    '''
    Преобразует дату из формата YYYY-MM-DD в DD.MM.YYYY

    Аргументы:
    date (str): Дата в формате YYYY-MM-DD

    Возвращает:
    str: Дата в формате DD.MM.YYYY
    '''

    date_formate = f"{date[8:10]}.{date[5:7]}.{date[:4]}"
    return date_formate
