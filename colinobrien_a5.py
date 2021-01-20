
#### Dictionaries of all of the different movies and their ratings ###

fantasy={'Lord of the Rings':'Lord of the Rings: Group destroys ring to save middle earth','Star Wars':'Star Wars: Intergalatic adventure to defeat galatic empire'}
drama={'Godfather':'Godfather: Ambitious young man becomes the leader of mafia group', 'Casablanca':'Casablanca: World War 2 love story'}
comedy={'Kicking and Screaming':'Kicking and Screaming: Dad goes overboard coaching son\'s soccer team', 'Dodgeball':'Dodgeball: Friends competes in dodgeball competition to save local gym'}
movie_ratings={'Lord of the Rings':'8/10','Star Wars':'6/10','Godfather':'7/10','Casablanca':'4/10','Kicking and Screaming':'10/10','Dodgeball':'3/10'}

### ###


ask_again=1
while ask_again==1:
    ##Home Screen##
    val=input('Home Screen: Please enter a movie genre: fantasy, comedy, drama (note: must use \'\' around text):  ')

    if val is 'fantasy':
        print(fantasy.keys())
        desr=input('Enter movie name to see movie description:  ')
        print(fantasy[desr])
        rate=input('Enter Buy to purchase movie, Rate to see movie reviews or Return to go back to home screen  ')
        if rate is 'Buy':
            print('Thank you for your purchase!  ')
            ask_again==0
            break
        elif rate is 'Rate':
            print(movie_ratings[desr])
            question=input('Enter Buy to watch movie or Return to look for a different movie:  ')
            if question is 'Buy':
                print('Thank you for your purchase!  ')
                ask_again==0
                break
        else:
            print("")
    elif val is 'drama':
        print(drama.keys())
        desr=input('Enter movie name to see movie description:  ')
        print(drama[desr])
        rate=input('Enter Buy to purchase movie, Rate to see movie reviews or Return to go back to home screen  ')
        if rate is 'Buy':
            print('Thank you for your purchase!  ')
            ask_again==0
            break
        elif rate is 'Rate':
            print(movie_ratings[desr])
            question=input('Enter Buy to watch movie or Return to look for a different movie:  ')
            if question is 'Buy':
                print('Thank you for your purchase!')
                ask_again==0
                break
    elif val is 'comedy':
        print(comedy.keys())
        desr=input('Enter movie name to see movie description:  ')
        print(comedy[desr])
        rate=input('Enter Buy to purchase movie, Rate to see movie reviews or Return to go back to home screen  ')
        if rate is 'Buy':
            print('Thank you for your purchase!')
            ask_again==0
            break
        elif rate is 'Rate':
            print(movie_ratings[desr])
            question=input('Enter Buy to watch movie or Return to look for a different movie:  ')
            if question is 'Buy':
                print('Thank you for your purchase!')
                ask_again==0
                break
        else:
            print("")
    else:
        print('We don\'t have that, try again. (you may need to be including the quotes (ex. \'drama\', not just drama) for this program to work)')
