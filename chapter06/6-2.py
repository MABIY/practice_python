favorite_numbers = {
    'mandy': 42,
    'micah': 23,
    'gus': 7,
    'hank': 1_000_000,
    'maggie': 0,
}

def favorite_num(name:str,num):
    print(f"{name.title()}'s favorite number is {num}")

favorite_num('mandy',favorite_numbers['mandy'])
favorite_num('micah',favorite_numbers['micah'])
favorite_num('gus',favorite_numbers['gus'])
favorite_num('hank',favorite_numbers['hank'])
favorite_num('maggie',favorite_numbers['maggie'])
