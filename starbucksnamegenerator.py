# this is a starbucks name generator
# it will ask the user for their name
# and modify it to look like an authentic Starbucks name


def main():
    print('Welcome to the Starbucks Name Generator!')
    username = input('Please enter your name: ')
    generate_name(username)


def generate_name(username):
    for i in range(len(username)):
        if username[i] == 'a':
            username = username.replace(username[i], 'ah')
        elif username[i] == 'i':
            username = username.replace(username[i], 'y')
        elif username[i] == 'e':
            username = username.replace(username[i], 'ee')
        elif username[i] == 'o':
            username = username.replace(username[i], 'oh')
        elif username[i] == 'y':
            username = username.replace(username[i], 'ie')
        elif username[i] == 'u':
            username = username.replace(username[i], 'oo')
        elif username[i] == 'k':
            username = username.replace(username[i], 'c')
        elif username[i] == 'x':
            username = username.replace(username[i], 'cs')
        elif username[i] == 'v':
            username = username.replace(username[i], 'f')
        else:
            username = username
    print('Your Starbucks Name is:', username)


main()
