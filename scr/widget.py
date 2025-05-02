from masks import get_mask_card_number, get_mask_account

def mask_account_card(account_info):
    if account_info[:5].lower() == 'счет':
        return account_info[:6] + get_mask_account(account_info[6:])
    else:
        return account_info[:-12] + get_mask_card_number(account_info[-12:])

def get_date(date):
    date_formate = f'{date[8:10]}.{date[5:7]}.{date[:4]}'
    return date_formate

