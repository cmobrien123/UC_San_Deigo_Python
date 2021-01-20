#### Dictionaries of all of the different movies ###
fantasy     ={'Lord of the Rings':'Lord of the Rings: Group destroys ring to save middle earth','Star Wars':'Star Wars: Intergalatic adventure to defeat galatic empire'}
drama       ={'Godfather':'Godfather: Ambitious young man becomes the leader of mafia group', 'Casablanca':'Casablanca: World War 2 love story'}
comedy      ={'Kicking and Screaming':'Kicking and Screaming: Dad goes overboard coaching son\'s soccer team', 'Dodgeball':'Dodgeball: Friends competes in dodgeball competition to save local gym'}
#### movie ratings ####
movie_ratings       ={'Lord of the Rings':100,'Star Wars':60,'Godfather':70,'Casablanca':40,'Kicking and Screaming':10,'Dodgeball':40}
movie_price         ={'Lord of the Rings':10,'Star Wars':5,'Godfather':5,'Casablanca':25,'Kicking and Screaming':15,'Dodgeball':25}

def rating_comparison(movie):  ##compares the movie rating to other movies (above or below average)
    ratings=movie_ratings.values()
    ratings_average=sum(ratings)/len(ratings)
    if movie_ratings[movie] > ratings_average:
        print('') #blank line
        print('Movie rating:')
        print(movie_ratings[movie])
        print('This movie is rated above average')
        print('') #blank line
    else:
        print('') #blank line
        print('Movie rating:')
        print(movie_ratings[movie])
        print('This movie is rated below average')
        print('') #blank line

def fair_price_for_movie(movie):   ## calcs if movie is a fair price based on the max price of any movie and ratings
    ratings=movie_ratings.values()
    ratings_average=sum(ratings)/len(ratings)
    prices=movie_price.values()
    price_max=max(prices)
    fair_price=(movie_ratings[movie]*price_max)/100 #crude calc of fair price
    if fair_price>movie_price[movie]:
        return 1
    else:
        return 0

fair_price_for_movie("Star Wars")



##### Start of Code (clean up a bit from last time after reviewing example)#####

ask_again=1
while ask_again==1:
    ##Home Screen##
    print('='*20)
    val=input('Home Screen: Please enter a movie genre: fantasy, comedy, drama   :')
    print('='*20)
    print('') #blank line
    print(val.keys())
    print('') #blank line
    movie_name=input('Enter movie name (with \' \') to see movie description:  ')
    print('') #blank line
    print('Movie description: ')
    print(val[movie_name])
    print('') #blank line
    starting_price = movie_price[movie_name]
    print('movie price (In dollars):')
    print(starting_price)   ## the actual price
    x=fair_price_for_movie(movie_name)   ## fair value
    if x==1:
        print('Movie is considered a great deal based on ratings')
        print('') #blank line'
    else:
        print('Movie is not considered a great deal based on ratings')
        print('') #blank line
    rate=input('Enter \'Buy\' to purchase movie or \'Rate\' to see movie reviews (out of 100)   :')
    if rate is 'Buy':
        print('') #blank line
        print('Thank you for your purchase!  ')
        ask_again==0
        break
    else:
        rating_comparison(movie_name)
        question=input('Enter Buy to watch movie or Return to look for a different movie:  ')
        if question is 'Buy':
            print('') #blank line
            print('Thank you for your purchase!  ')
            ask_again==0
            break
