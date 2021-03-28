import random 

deck = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']  #single deck of cards 
card_value = [2,3,4,5,6,7,8,9,10,10,10,10,[1,11]]  #used/referenced to get the value of the cards. 

eight_deck = []    #eight deck of cards for the house 


users_hand = [0,0]    #array will hold all user dealt cards 
houses_hand = [0,0]   #will hold the houses dealt cards 
temp_hand = [0,0]

i = 0  #iterator to create 8 deck of cards 
#while loop creates and 8 deck of card
while i < 8:
    copy_deck = deck  
    eight_deck.extend(copy_deck)
    i=i+1

#initial shuffle
random.shuffle(eight_deck)

#card counter keeps trap of card order in shuffled deck
card_counter = 0

#keeps track of the numerical value of the users hand 
user_hand_value = 0 

#houses hand value
house_hand_value = 0

    
#def shuffle():
    
def nextCardInDeck():  #keeps track of next card to be dealt from the houses 8 deck
    global card_counter
    card_counter = card_counter+1
    
def initialDeal():    #initiates the handout of cards from the dealer  
    global users_hand
    
    users_hand[0] = eight_deck[card_counter]
    nextCardInDeck()
    
    houses_hand[0] = eight_deck[card_counter]
    nextCardInDeck()

    users_hand[1] = eight_deck[card_counter]
    nextCardInDeck()

    houses_hand[1] = eight_deck[card_counter]

    '''
    code to show user his hand and the first card of the deals hand with the second card faced down
    '''


def userDealOneCard():            #a user decision -hit
    global user_hand_value
    nextCardInDeck()
    hit = eight_deck[card_counter]
    hitIndex = deck.index(hit)
    if(user_hand_value != 0):
        user_hand_value = user_hand_value + int(card_value[hitIndex])
    print('hit = ',hit)
    print(user_hand_value)

    users_hand.append(hit)  #adds hit to active users_hand 
    print(users_hand)
        
def quickEvaluate():
    if(user_hand_value > 21):
        return True
    else:
        return False


def userDecision():
    userInput = int(input('Type 1 = Hit :  2 = Stay : 3 = Double : 4 = Surrender: ')) #decision prompt for the user 

    #hit 
    if(userInput == 1):
        userDealOneCard()
        didBreak = quickEvaluate() #checks if user's hand is above 21 
        if(didBreak == True):
            print('Over 21, try again!')
            return False  #returns false if user busts and true if user wins 
        else:
            userDecision()
    
    #stay
    elif(userInput == 2):
        return True 
        #do nothing 
    
    #double
    elif(userInput == 3):
        userDealOneCard()
        didBreak = quickEvaluate()
        if(didBreak == True):
            print('Over 21, try again!')
            return False  #returns false if user busts and true if user stays under 21
        else:
            return True
        
    #surrender
    elif(userInput == 4):
        #forfiet hand and lose half of wager
        return False
    
def housesDecision():
    global house_hand_value

    while(house_hand_value < 17):
        #keep hitting until over 16 or bust
        nextCardInDeck()
        hit = eight_deck[card_counter]
        hitIndex = deck.index(hit)
        house_hand_value = house_hand_value + int(card_value[hitIndex])

    if(house_hand_value > 21):
        return False
    else:
        return True
        
        

def houseCheckForBlackjack():
    global house_hand_value 
    
    house_card_one_index = deck.index(houses_hand[0]) #house card 1 
    house_card_one = int(card_value[house_card_one_index])

    house_card_two_index = deck.index(houses_hand[1]) #house card 2 
    house_card_two = int(card_value[house_card_two_index])

    house_hand_value = house_card_one + house_card_two  #sum of the houses initial deal 
    if(house_hand_value == 21):
        return True
    else:
        return False 

def initialEvaluateUser():
    global user_hand_value
    
    bust = 22
    win = 21
    user_hand_value = 0
    user_hand_multi = []

    card_one = users_hand[0]
    card_one_index = deck.index(card_one)
    card_two = users_hand[1]
    card_two_index = deck.index(card_two)


    #if card 1 is an Ace and checks if card 2 is 
    if (card_one == 'A'):
        if(card_two == 'A'):
            user_hand_multi = [2,12]
        else:
            if(card_value[card_two_index] > 9):  #checks if a card of value of 10 is paired with an Ace 
                print('blackjack_1')
                user_hand_value = 21
                return True             #returns true is blackjack is obtained 
            else:
                temp1 = 1 + card_value[card_two_index]   #values of an Ace can be either 1 or 11
                temp2 = 11 + card_value[card_two_index]  
                user_hand_multi = [temp1,temp2]
    #if card one is not an Ace, checks is card 2 is 
    elif (card_two == 'A'):
        if(card_value[card_one_index] > 9):
            print('blackjack_2')
            user_hand_value = 21
            return True         #returns true if blackjack is obtained. 
        else:
            temp1 = 1 + card_value[card_two_index]
            temp2 = 11 + card_value[card_two_index]
            user_hand_multi = [temp1,temp2]
    #If niether card is an Ace
    else:
        user_hand_value = card_value[card_one_index] + card_value[card_two_index]

    
    if (user_hand_value == 0):
        print(user_hand_multi)

    else:
        print(user_hand_value)

    return False
        


def driver():
    print(eight_deck)

    initialDeal()

    print("house1 = " + houses_hand[0])
    print("house2 = " + houses_hand[1])
    print('users hand: ', users_hand )


    if(houseCheckForBlackjack() == True):
        print('House Wins, House Blackjack')

    else:
        userHasBlackjack = initialEvaluateUser()

        if (userHasBlackjack == True ):
            print('You won! 21!')
        else:
            u_decision = userDecision()
            if(u_decision == True):   #if userDecision is True (then hand is active) if False (the user bust)
                h_decision = houseDecision()
                if(h_decision == False):
                    print('You win! Play again!')
                else:
                    print('You lose, try again')
            
            elif(u_decision == False):  #runs if user busts
              print('You lose, Try again!')

    


driver()
