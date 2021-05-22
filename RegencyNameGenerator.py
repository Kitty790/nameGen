# This is a English Regency Peerage Name Generator
# made for fun

import random


# main(): Runs the main program and displays the menu
# and determines which functions to call
def main():
    # welcome banner
    print('Welcome to the English Regency Peerage Name Generator!')
    again = 'y'
    # while loop to continue program until user quits
    while again == 'y' or again == 'Y':
        # displays menu
        print('Options:')
        print('To generate a realistically styled name press 1')
        print('To generate a Wattpad/trashy romance style name press 2')
        # collects user's choice of realistic or trash
        choice = input('Enter your choice here 1/2: ')
        # input validation loop
        while choice != '1' and choice != '2':
            choice = input('ERROR! Enter 1/2 only: ')
        # if = realistic name
        if choice == '1':
            sex = pick_gender()  # calls pick_gender()
            # nested if-else to determine whether to call
            # male or female titles
            if sex == 'M' or sex == 'm':
                male_titles()
            else:
                female_titles()
        # else = trash name
        else:
            sex = pick_gender()  # calls pick_gender
            # nested if-else to determine whether to call
            # male or female trash titles
            if sex == 'M' or sex == 'm':
                male_titles_trash()
            else:
                female_titles_trash()
        # determines whether to rerun program or quit
        again = input('Would you like to generate another name? Y/N: ')


# pick_gender(): collects user input on whether they would like
# to generate a male or female name and sends input back to main()
def pick_gender():
    gender = input('Would you like to generate a male or female name? M/F: ')
    # input validation loop
    while gender not in ['M', 'm', 'F', 'f']:
        gender = input('ERROR! Enter M/F only: ')
    return gender  # returns gender to main()


# male_titles(): Generates a realistic male title
def male_titles():
    # realistic noble titles list
    titles = ['Duke', 'Marquess', 'Viscount', 'Earl', 'Baron', 'The Honorable Mr.']
    title = random.choice(titles)  # chooses random title
    # if-else statement to determine whether to call male_names() or land_title_male()
    if title == 'The Honorable Mr.':
        print(title, end=' ')
        male_names()  # calls male_names()
    else:
        print(title, 'of', end=' ')
        land_title_male()  # calls land_title_male()


# male_names(): generates a realistic male first name
def male_names():
    # realistic male first names list
    names = ['Edward', 'William', 'Charles', 'John', 'Henry', 'George', 'James', 'Thomas',
             'Robert', 'Richard', 'Hugh', 'Philip', 'Alexander', 'Arthur', 'Francis', 'David',
             'Frederick', 'Christopher', 'Stephen', 'Patrick', 'Matthew', 'Cecil', 'Benjamin',
             'Edmund', 'Lawrence', 'Reginald', 'Ralph']
    name = random.choice(names)  # picks random name
    print(name, end=' ')
    last_names()  # calls last_names()


# female_titles(): generates a realistic female title
def female_titles():
    # realistic female noble titles list
    titles = ['Duchess', 'Marchioness', 'Viscountess', 'Countess', 'Baroness', 'The Honorable Miss',
              'The Honorable Mrs.']
    title = random.choice(titles)  # chooses random title
    # if-else to determine whether to call female_names() or land_title_female()
    if title == 'The Honorable Mrs.' or title == 'The Honorable Miss':
        print(title, end=' ')
        female_names()  # calls female_names()
    else:
        print(title, 'of', end=' ')
        land_title_female()  # calls land_title_female()


# female_names(): generates a realistic female first name
def female_names():
    # realistic female first names list
    names = ['Jane', 'Anne', 'Ann', 'Elizabeth', 'Mary', 'Eliza', 'Eleanor', 'Catherine', 'Marie',
             'Helen', 'Harriet', 'Charlotte', 'Frances', 'Margaret', 'Dorothea', 'Marian', 'Alice',
             'Sophia', 'Sarah', 'Isabella', 'Emma', 'Abigail', 'Agnes', 'Beatrice', 'Martha', 'Lucy',
             'Georgiana', 'Susan']
    name = random.choice(names)  # chooses random name
    print(name, end=' ')
    last_names()  # calls last_names()


# land_title_male(): generates a realistic land title
def land_title_male():
    # realistic land titles list
    titles = ['Hastings', 'Lancaster', 'Manchester', 'Whitworth', 'Southampton', 'Northampton',
              'Cornwall', 'Dudley', 'Huntingdon', 'York', 'Yorkshire', 'Basingstoke', 'Canterbury',
              'Greenfield', 'Liverpool', 'Camden', 'Nottingham', 'Coventry', 'Hampshire', 'Jersey',
              'Grantham', 'Essex', 'Blackpool', 'Grey', 'Sussex', 'Dudley', 'Nottingham', 'Bath',
              'Somerset', 'Wellington', 'Lennox', 'Norfolk', 'Suffolk', 'Leinster', 'Gloucester',
              'Clarence', 'Lancaster', 'Newcastle', 'Portland', 'Leeds', 'Avondale', 'Bath', 'Salisbury',
              'Kent', 'Fife', 'Cambridge', 'Oxford', 'Edinburgh', 'Westminster', 'Wilton']
    title = random.choice(titles)  # chooses random land title
    print(title, ', Lord', sep='', end=' ')
    male_names()  # calls male_names


# land_title_female(): generates a realistic land title
def land_title_female():
    # realistic land titles list
    titles = ['Hastings', 'Lancaster', 'Manchester', 'Whitworth', 'Southampton', 'Northampton',
              'Cornwall', 'Dudley', 'Huntingdon', 'York', 'Yorkshire', 'Basingstoke', 'Canterbury',
              'Greenfield', 'Liverpool', 'Camden', 'Nottingham', 'Coventry', 'Hampshire', 'Jersey',
              'Grantham', 'Essex', 'Blackpool', 'Grey', 'Sussex', 'Dudley', 'Nottingham', 'Bath',
              'Somerset', 'Wellington', 'Lennox', 'Norfolk', 'Suffolk', 'Leinster', 'Gloucsester',
              'Clarence', 'Lancaster', 'Newcastle', 'Portland', 'Leeds', 'Avondale', 'Bath', 'Salisbury',
              'Kent', 'Fife', 'Cambridge', 'Oxford', 'Edinburgh', 'Westminster', 'Wilton']
    title = random.choice(titles)  # chooses random land title
    print(title, ', Lady', sep='', end=' ')
    female_names()  # calls female_names()


# last_names(): generates a realistic last name for both females and males
def last_names():
    # realistic last names list
    names = ['Whitworth', 'Hastings', 'Fitzroy', 'Grey', 'LeFroy', 'Dudley', 'Laveaux', 'Hamilton', 'Percy',
             'FitzGerald', 'Egerton', 'Wellesley', 'Montagu', 'Graham', 'Campbell', 'Somerset', 'Cavendish',
             'Lennox', 'Howard', 'Scott', 'Cadogan', 'Harris', 'FitzGibbon', 'Byng', 'Boscawen', 'Willoughby',
             'Hawke', 'Foley', 'Cust', 'Norton', 'Rodney', 'Bagot', 'de Grey', 'de Walden', 'Seymour',
             'Gordon', 'Lennox', 'Spencer', 'Douglas', 'Russell', 'Beauclerk', 'Manners', 'Grosvenor',
             'Mountbatten', 'Stanley', 'Talbot', 'Herbert', 'Fiennes', 'Bertie', 'Finch', 'Fane', 'Ashley',
             'Lumley', 'Capell', 'Coventry', 'Bentinck', 'Hastings', 'Courtenay', 'Lindsay', 'Sutherland',
             'Leslie', 'Montgomerie', 'Sinclair', 'Stuart', 'Lyon', 'Drummond', 'Erskine', 'Scrymgeour',
             'Charteris', 'Primrose', 'St John', 'Melville', 'Murray', 'Ogilvie']
    name = random.choice(names)  # chooses random surname
    print(name)


# male_titles_trash(): generates a trash male title
def male_titles_trash():
    # trash male titles list
    titles = ['Duke', 'Marquess', 'Viscount', 'Earl', 'Baron']
    title = random.choice(titles)  # chooses random title
    print(title, 'of', end=' ')
    land_titles_trash_male()  # calls land_titles_trash_male()


# male_names_trash(): generates a trashy male first name
def male_names_trash():
    # trashy male first names list
    names = ['Drake', 'Jordan', 'Callum', 'Ryan', 'Josh', 'Caden', 'Bryan', 'Sullivan', 'Kai',
             'Jason', 'Quentin', 'Kyle', 'Chris', 'Riley', 'Wayne', 'Dwayne', 'Louis', 'Lou',
             'Josiah', 'Oak', 'Austin', 'Connor', 'Caleb', 'Levi', 'Beau', 'Jesse', 'Nate',
             'Kodi', 'Zachariah', 'Kirk', 'Doug', 'Willoughby', 'Chad', 'Kendall', 'Gerald',
             'Franklin', 'Woodrow', 'Abraham', 'Geordie', 'Leofrick', 'Lee', 'Harvey', 'Ulysses',
             'Sherman', 'Mickey', 'Walt', 'Elijah', 'Fletcher', 'Ike', 'Dathan', 'Dominic', 'Dace',
             'Ulysses', 'Mac', 'Derrick', 'Scott', 'Guy', 'Sherman', 'Trey', 'Tad', 'Cade', 'Tristan',
             'Damien', 'Jared', 'Donald', 'Dan', 'Chris', 'Liam', 'Zayn', 'Ian', 'Xavier', 'Giorgio',
             'Percy', 'Narcissus', 'Harry', 'Kendall', 'Jordan', 'Casey', 'Percy', 'Merlin', 'Aberforth']
    name = random.choice(names)  # chooses random name
    print(name, end=' ')
    last_names_trash()  # calls last_names_trash()


# female_titles_trash(): generates female trash titles
def female_titles_trash():
    # trash female titles list
    titles = ['Duchess', 'Marchioness', 'Viscountess', 'Countess', 'Baroness']
    title = random.choice(titles)  # chooses random title
    print(title, 'of', end=' ')
    land_titles_trash_female()  # calls land_titles_trash_female()


# female_names_trash(): generates a trashy female first name
def female_names_trash():
    # trashy female first names list
    names = ['Ashlee', 'Lacy', 'Kaylee', 'Jasmine', 'Nova', 'Xenia', 'Lola', 'Katie', 'Madison',
             'Ellie', 'Bianca', 'Kaitlin', 'Britney', 'Giovanna', 'Jessica', 'Allison', 'Deirdre',
             'Alyssa', 'Hermione', 'Lavender', 'Kylie', 'Kendall', 'Chloe', 'Kimberly',
             'Courtney', 'Wilma', 'Astrix', 'Honeysuckle', 'Destiny', 'Sapphire', 'Emerald', 'Opal',
             'Pearl', 'Garnet', 'Ruby', 'Amethyst', 'Topaz', 'Eglantine', 'Rosetta', 'Sylvia', 'Scarlett',
             'Aurelia', 'Claire', 'Aurora', 'Fidelia', 'Blue', 'Winnie', 'Mel', 'Kaylee', 'Phoebe',
             'Kelsey', 'June', 'Claire', 'Britnee', 'Poppy', 'Sunny', 'Leyla', 'Denise', 'Chelsey',
             'Danielle', 'Delphine', 'Selene', 'Celeste', 'Scarlett', 'April', 'May', 'Hope', 'Mercy',
             'Patience', 'Camelia', 'Magnolia', 'Coriander', 'Primrose', 'Rosemary', 'Pansy', 'Daisy',
             'Sybil', 'Edith', 'Violet', 'Lavender', 'Posie', 'Penny', 'Bella', 'Persephone', 'Athena']
    name = random.choice(names)  # chooses random name
    print(name, end=' ')
    last_names_trash()  # calls last_names_trash()


# land_titles_trash_male(): generates a trashy land title
def land_titles_trash_male():
    # trashy land titles list
    titles = ['Crockett', 'Laveaux', 'Kimberly', 'Pillsbury', 'Derbyham', 'Winslet', 'Birkhamshire',
              'Pellham', 'Springfield', 'Yorkham', 'Lustershire', 'Gluttonham', 'White Hill',
              'Kirkham', 'Ferncaster', 'Easthampton', 'Featheringham', 'Dirkshire', 'Cadbury',
              'Pellingham', 'Berk', 'Bridgeport', 'Withersford', 'Heartford', 'Rostershire', 'Chadford',
              'Denham', 'Abbotshire', 'Rivendell', 'Hillsbury', 'Durtford', 'Tonham', 'Farthington',
              'LeBeaux', 'Farthingham', 'Farthingshire']
    title = random.choice(titles)  # chooses random land title
    print(title, ', Lord', sep='', end=' ')
    male_names_trash()  # calls male_names_trash


# land_titles_female_trash(): generates a trashy land title
def land_titles_trash_female():
    # trashy land titles list
    titles = ['Crockett', 'Laveaux', 'Kimberly', 'Pillsbury', 'Derbyham', 'Winslet', 'Birkhamshire',
              'Pellham', 'Springfield', 'Yorkham', 'Lustershire', 'Gluttonham', 'White Hill',
              'Kirkham', 'Ferncaster', 'Easthampton', 'Featheringham', 'Dirkshire', 'Cadbury',
              'Pellingham', 'Berk', 'Bridgeport', 'Withersford', 'Heartford', 'Rostershire', 'Chadford',
              'Denham', 'Abbotshire', 'Rivendell', 'Hillsbury', 'Durtford', 'Dentingham', 'LeBeaux',
              'Farthington', 'Farthingham', 'Farthingshire']
    title = random.choice(titles)  # chooses random land title
    print(title, ', Lady', sep='', end=' ')
    female_names_trash()  # calls female_names_trash()


# last_names_trash(): generates a trashy last name for both males and females
def last_names_trash():
    # trashy surnames list
    names = ['Tanner', 'Smith', 'Fielding', 'Potter', 'Cooper', 'Shepherd', 'Paisley', 'Chadford', 'Beauford',
             'Drew', 'Gregory', 'Crownhart', 'Heartford', 'Praiseworthy', 'Speare', 'O\'Donnell', 'McAvoy',
             'Archer', 'Fletcher', 'Lennon', 'Chanterelle', 'Mcyntire', 'Beresford', 'Garvey', 'Turner',
             'Carter', 'Denham', 'Baker', 'Glover', 'Atwell', 'Stark', 'Inkwell', 'Fraser', 'McDonald',
             'O\'Riley', 'McDougal', 'O\'Connor', 'Brewster', 'Chappell', 'McCartney', 'Harrison', 'Brown',
             'Birch', 'Oakley', 'Grant', 'Sherman', 'Jackson', 'Quill', 'Peregrine', 'Farthington']
    name = random.choice(names)  # chooses random surname
    print(name)


# calls main()
main()
