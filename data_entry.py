from datetime import datetime



def get_date(prompt, allow_dafault=False):
    date_str = input(prompt)
    if allow_dafault and not date_str:
        return datetime.today().strtime("%d-%m-%Y")
    
    try:
        valid_date = datetime.strptime(date_str, )



def get_amount():
    pass

def get_category():
    pass

def get_description():
    pass