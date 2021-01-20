
#### Dictionaries of all of the different movies and their ratings ###


fantasy={'Lord of the Rings':'Lord of the Rings: Group destroys ring to save middle earth', 'Star Wars':'Star Wars: Intergalatic adventure to defeat galatic empire'}
drama={'Godfather':'Godfather: Ambitious young man becomes the leader of mafia group', 'Casablance':'Casablanca: World War 2 love story'}
comedy={'Kicking_Screaming':'Kicking and Screaming: Dad goes overboard coaching son\'s soccer team', 'Dodgeball':'Dodgeball: Friends competes in dodgeball competition to save local gym'}
movie_ratings={'Lord of the Rings':'8/10','Star Wars':'6/10','Godfather':'7/10','Casablanca':'4/10','Kicking_Screaming':'10/10','Dodgeball':'3/10'}

### ###

def what_movie(genre):
    ag=1
    while ag==1:
        print(genre.keys())
        print("") #space
        desr=input('Enter movie name to see movie description:  ')
        print("") #space
        # print(desr)
        print("") #space
        print(genre[desr])
        print("") #space
        rate=input('Enter Buy to purchase movie or return to go back to home screen  ')
        if rate is 'Buy':
            print("") #space
            print('Thank you for your purchase!  ')
            ag=0
            return ag
        else:
            print("") #space
            print("Returning to home screen")
            ag=0
# end of the function #

genre=input('Home Screen: Please enter a movie genre: fantasy, comedy, drama: ')
what_movie(genre)
