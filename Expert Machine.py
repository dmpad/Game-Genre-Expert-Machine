#David Padalino     Expert Machine
import sys

def firstQuestion():
    print('Please type y for yes or n for no for all questions.')
    print('')
    print('Are you trying to solve a logic problem? (y or n)')
    a1 = input()

    if a1.lower() == 'y':
        print('This is a puzzle game.')
        print('Games in this genre: Portal, Peggle')
    else:
        print('Do you shoot a deadly weapon?')
        a2 = input()

        if a2.lower() == 'y':
            shooter()
        else:
            print('Is this game simulating something?')
            a3 = input()

            if a3.lower() == 'y':
                simulator()
            else:
                print('Is the purpose of this game the story?')
                a4 = input()

                if a4.lower() == 'y':
                    story()
                else:
                    print('The genre you are describing might not be specified in this system.')


def shooter():
    print('Are you watching your character?')
    a5 = input()

    if a5.lower() == 'y':
        print('This is a Third-Person Shooter')
        print('Games in this genre: Grand Theft Auto, Saints Row')
    else:
        fps()

def fps():
    print('Are you in a war setting?')
    a6 = input()

    if a6.lower() == 'y':
        print('This is a Military Shooter')
        print('Games in this genre: Call of Duty, Medal of Honor')
    else:
        print('Are you in a place with futuristic technology?')
        a7 = input()

        if a7.lower() == 'y':
            print('This is a Science Fiction First-Person Shooter')
            print('Games in this genre: Prey, Half-Life')
        else:
            print('Are you in a destroyed world?')
            a8 = input()

            if a8.lower() == 'y':
                print('This is a Post-Apocalyptic First-Person Shooter')
                print('Games in the genre: Fallout, Borderlands')
            else:
                print('This is a First-Person Shooter')
                print('Games in this genre: Call of Duty, Overwatch')


def simulator():
    print('Does the game have shooting people as its main mechanic?')
    a9 = input()

    if a9.lower() == 'y':
        print('This is a Military Shooter')
        print('Games in this genre: Call of Duty, Medal of Honor')
    else:
        print('This is a Simulator')
        print('Games in this genre: Farming Simulator, Euro Trucker Simulator')

def story():
    print('Is the primary (or only) mechanic making story decisions?')
    a10 = input()

    if a10.lower() == 'y':
        print('This is a Visual Novel')
        print('Games in this genre: Doki Doki Literature Club, The Wolf Among Us')
    else:
        RPG()

def RPG():
    print('Do you play one turn at a time?')
    a11 = input()

    if a11.lower() == 'y':
        turnBased()
    else:
        print('Are you in a war setting?')
        a12 = input()

        if a12.lower() == 'y':
            print('This is a Military RPG')
            print('Games in this genre: Warface, Mount and Blade: Warband')
        else:
            print('Are you in a place with futuristic technology?')
            a13 = input()

            if a13.lower() == 'y':
                print('This is a Science Fiction RPG')
                print('Games in this genre: BioShock, System Shock')
            else:
                print('Are you in a destroyed world?')
                a14 = input()

                if a14.lower() == 'y':
                    print('This is a Post-Apocalyptic RPG')
                    print('Games in this genre: Fallout, Mad Max')
                else:
                    print('Are you in a fantasy setting?')
                    a15 = input()

                    if a15.lower == 'y':
                        print('This is a Fantasy RPG')
                        print('Games in this genre: Final Fantasy, Diablo')
                    else:
                        print('This game is an RPG')
                        print('Games in this genre: Skyrim, Fallout')

        print('Is the game online?')
        a16 = input()

        if a16.lower() == 'y':
            print('Does the game take place in a large server of people?')
            a17 = input();

            if a17.lower() == 'y':
                print('This game is also an MMO')
                print('Games in this genre: World of Warcraft, Star Trek Online')
            else:
                print('This game is also a Co-op game')
                print('Games in this genre: Borderlands, Tales of Xillia')

def turnBased():
    print('Are you in a war setting?')
    a18 = input()

    if a18.lower() == 'y':
        print('This is a Turn-Based Military RPG')
        print('Games in this genre: Civilization, Hearts of Iron')
    else:
        print('Are you in a place with futuristic technology?')
        a19 = input()

        if a19.lower() == 'y':
            print('This game is a Turn-Based Science Fiction RPG')
            print('Games in this genre: Xcom, Endless Space')
        else:
            print('This is a Turn-Based RPG')
            print('Games in this genre: Xcom, Civilization')

def main():
    a20 = 'y'
    while a20 == 'y':
        firstQuestion()

        print('')
        print('')
        print('Would you like to ask again?')
        a20 = input()
    sys.exit()

main()
