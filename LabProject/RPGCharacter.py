full_dot = '●'
empty_dot = '○'

def create_character(name, STR , INT, CHA):
    if not isinstance(name, str):
        return 'The character name should be a string'
    elif not name:
        return 'The character should have a name'
    elif len(name) > 10:
        return 'The character name is too long'
    elif ' ' in name:
        return 'The character name should not contain spaces'
    elif not isinstance(STR, int) or not isinstance(INT, int) or not isinstance(CHA, int):
        return 'All stats should be integers'
    elif STR < 1 or INT < 1 or CHA < 1:
        return 'All stats should be no less than 1'
    elif STR > 4 or INT > 4 or CHA > 4:
        return 'All stats should be no more than 4'
    elif STR + INT + CHA != 7:
        return 'The character should start with 7 points'
    else:
        strength = STR*full_dot + (10-STR)*empty_dot
        intelligence = INT*full_dot + (10-INT)*empty_dot
        charisma = CHA*full_dot + (10-CHA)*empty_dot
        return f'{name}\nSTR {strength}\nINT {intelligence}\nCHA {charisma}'

print(create_character('ren', 4, 2, 1))