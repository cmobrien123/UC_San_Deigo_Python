class Card:
    def __init__(self, suite, number):
        self.suite= suite
        self.number= number
    def get_display_string(self):
        #Defining the Suite#
        card_suite = 'blank'
        if self.suite == 1:
            card_suite = 'Dimonds '
        elif self.suite == 2:
            card_suite = 'Hearts '
        elif self.suite == 3:
            card_suite = 'Spades '
        elif self.suite == 4:
            card_suite = 'Clubs '
        else:
            pass
        #Defining the Number#
        ace=1
        jack=11
        queen=12
        king=13
        card_number = self.number
        if self.number == ace:
            card_number = 'Ace'
        elif self.number == jack:
            card_number = 'Jack'
        elif self.number == queen:
            card_number = 'Queen'
        elif self.number == king:
            card_number = 'King'
        else:
            pass
        #converting to strings and making final output
        final_card_name=str(card_number)
        final_card_suite=str(card_suite)
        c_name=final_card_name+' of '+final_card_suite
        return c_name
