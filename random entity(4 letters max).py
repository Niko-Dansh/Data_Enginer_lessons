import random, string

def random_entity_4max():
    choice_type = random.choice([None,bool,str,int,float])

    if choice_type is None:
        return None
    elif choice_type is bool:
        return random.choice([True,False])
    elif choice_type is str:
        i = 4
        str_4 = ''
        while i > 0:
            str_4 += random.choice(string.ascii_letters)
            i -= 1
        return str_4
    elif choice_type is int:
        return random.randint(1,9999)
    elif choice_type is float:
        return round(random.uniform(0.0,99.99),2)
