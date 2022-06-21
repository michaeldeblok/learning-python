# def format_name(f_name, l_name):
#     print(f_name.title())
#     print(l_name.title())

# format_name('angela','ANGELA')    


def format_name(f_name, l_name):
    if f_name == "" or l_name == "" :
        return "you didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    # print(f'{formatted_f_name} {formatted_l_name}')
    return f'{formatted_f_name} {formatted_l_name}'

#format_name('AnGelA','YU')
print(format_name(input('What is your first name? ')))
input('What is your last name? ')