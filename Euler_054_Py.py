#Ariel Tynan
#Euler Problem 054, Poker hands, solved in Python
#Started and completed 6 March 2022

def create_Card(val,suit):
    newCard = [val,suit]
    return newCard

def build_Hand(hand,card):
    hand.append(card)
    return hand

def stack_Hands(stack,hand):
    stack.append(hand)
    return stack

def convert_Nums(card):
    if card[0] == 'T':
        card[0] = 10
    elif card[0] == 'J':
        card[0] = 11
    elif card[0] == 'Q':
        card[0] = 12
    elif card[0] == 'K':
        card[0] = 13
    elif card[0] == 'A':
        card[0] = 14
    return card

def find_Dups(hand): #fuction heavily modified from Geeks for geeks
    dups = []
    flat = [item for sublist in hand for item in sublist]
    for f in flat:
        if f in ['2','3','4','5','6','7','8','9','T','J','Q','K','A']: #not based in suit. Pairs, trips, quads
            if flat.count(f) == 2: #adds pairs
                dupSet = [f,2]
                if dupSet not in dups:
                    dups.append(dupSet)
            if flat.count(f) == 3: #adds trips
                dupSet = [f,3]
                if dupSet not in dups:
                    dups.append(dupSet)
            if flat.count(f) == 4: #adds quads
                dupSet = [f,4]
                if dupSet not in dups:
                    dups.append(dupSet)
        else: #check for flushes
            if flat.count(f) == 5:
                flush = True #modify for global
                #print("There is a flush")
    return(dups) #dups = [amount,value]

def score_Hand(hand):
    #Score made up of 9 hand bytes
    score = [0,0,0,0,0,0,0,0,0,0] #hand score init

    flush = False #Flush
    straight = False #Straight
    pair1 = False #One pair
    pair2 = False #Two pair
    trips = False #Three of a kind
    FH = False #Full House
    quads = False #Four of a kind
    SF = False #Straight Flush
    RF = False #Royal Flush\
    highCards = []

    #flush check
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]: #all cards, same suite
        flush = True
        #print("There is a FLUSH!")

    #straight check
    cards = ['A','2','3','4','5','6','7','8','9','T','J','Q','K','A']
    #print(find_Dups(hand))
    for i in range(0,5):
        while str(hand[i][0]) in cards: #Accounts for duplicates, while loops accounts for Aces
            cards[cards.index(str(hand[i][0]))] = 0
    #print(cards)
    for i in range(len(cards)-4):
        if cards[i] == cards[i + 1] == cards[i + 2] == cards[i + 3] == cards[i + 4] == 0:
            straight = True
            #print("There is a straight!")

    #Find high cards
    for i in range(13,0,-1): #J = 11, Q = 12, K = 13, A = 14
        if cards[i] == 0:
            highCards.append(i+1) #order of cards highest to lowest, based on index
    #Convert highcard face cards to numbers
    
    #Check dups
    dups = find_Dups(hand)
    for i in range(len(dups)):
        if dups[i][1] == 2 and pair1 == False:
            #print("There is a pair")
            pair1 = True
        elif dups[i][1] == 3 and pair1 == False:
            #print("Three of a kind")
            trips = True
        elif dups[i][1] == 2 and pair1 == True:
            #print("There are two pairs")
            pair2 = True
            #pair1 = False
        elif dups[i][1] == 2 and pair1 == True:
            #print("Full House")
            FH = True
            #trips = False
        elif dups[i][1] == 4:
            quads = True

    #Convert dup face values to numbers
    for i in range(0,len(dups)):
        dups[i] = convert_Nums(dups[i])

    #Sort dups
    sorted(dups,reverse = True, key = lambda x:x[-1])

    cardList = ['Aces','Twos','Threes','Fours','Fives','Sixes','Sevens','Eights','Nines','Tens','Jacks','Queens','Kings','Aces'] #used for printing

    #Finding max hand/combo hands, and scoring
    if straight == True and flush == True and cards[9] == cards[13] == 0: #If Royal Flush
        RF = True
        score[0] = 1
        print("ROYAL FLUSH")
    elif straight == True and flush == True:
        SF = True 
        score[1] = highCard[0] #straight is worth highest card
        #Find top card in straight
        print("STRAIGHT FLUSH", cardList[highCards[0]-1], "high")
    elif quads == True:
        score[2] = 10000*dups[0][0] + 100*highCards[0] + highCards[1] #only two valid HC spots 
        #Store value in dups
        #FIND KICKER
        print("FOUR OF A KIND,", cardList[int(dups[0][0])-1])#, ", with", cardList[highCards[0]-1], "kicker.")
    elif FH == True:
        #Store values in dups for trips and pair
        score[3] = 100*dups[1][0] + dups[0][0] #trips, pair
        print("FULL HOUSE",cardList[int(dups[1][0])-1],"full of", cardList[int(dups[0][0])-1])
    elif flush == True:
        #Order cards in flush
        score[4] = highCards[0] #flush is worth highest card
        print("Flush", cardList[highCards[0]-1], "high")
    elif straight == True:
        #Find op card in straight
        score[5] = highCards[0] #straight is worth highest card
        print("Straight", cardList[highCards[0]-1], "high.")
    elif trips == True:
        #Store value in dups
        score[6] = 1000000*int(dups[0][0]) + 10000*highCards[0] + 100*highCards[1] #+ highCards[2] #three HCs
        print("Three of a kind,", cardList[int(dups[0][0])-1])#, ", with", cardList[highCards[0]-1], "kicker.") 
    elif pair2 == True:
        #Store values of pairs in dups
        score[7] = 100000000*int(dups[1][0]) + 1000000*int(dups[0][0]) + 10000*highCards[0] + 100*highCards[1] + highCards[2] #three HCs
        print("Two pair,",cardList[int(dups[1][0])-1],"and", cardList[int(dups[0][0])-1])#, ", with", cardList[highCards[0]-1], "kicker.")
    elif pair1 == True:
        #Store value of pair in dups
        score[8] = 100000000*int(dups[0][0]) + 1000000*int(highCards[0]) + 10000*highCards[1] + 100*highCards[2] + highCards[3]#four HCs
        print("A pair of", cardList[int(dups[0][0])-1])#, ", with", cardList[highCards[0]-1], "kicker.")
    else:
        #print(highCards)
        score[9] = 100000000*highCards[0] + 1000000*highCards[1] + 10000*highCards[2] + 100*highCards[3] + highCards[4]
        print("High Card", highCards)
    return score

p1All = [] #list containing all (1000) hands of player 1
p2All = [] #list containing all (1000) hands of player 2

#Card made up of
    #Value: 2,3,4,5,6,7,8,9,T,J,Q,K,A
    #Suit: H,S,D,C

#Read in file
with open('p054_poker.txt') as f:
    if open:
        print("File has opened successfully.")
    output = f.read().replace('\n',' ')
    output = output.replace(" ","")

n = int(1000*2*5*2) #1000 hands x 2 players x 5 cards/hand x 2 elements/card
for i in range(0,n,10):
    p1Hand = []
    for j in range(0,10,2): #5 cards per hand
        #print("Card ", i + j + 1, create_Card(output[i+j],output[i+j+1]))
        hand = build_Hand(p1Hand,create_Card(output[i+j],output[i+j+1]))
    if i % 20 == 0:
        stack_Hands(p1All,hand)
    else:
        stack_Hands(p2All,hand)

#p1All[hand][card][val/suit]
#Find value of each hand
p1Wins = 0
for i in range(0,1000,1): #1000 pairs of hands
    print("\n","Hand: ",i+1)
    
    #print("P1: ", score_Hand(p1All[i]), "P2: ", score_Hand(p2All[i]))
    if score_Hand(p1All[i]) > score_Hand(p2All[i]):
        p1Wins = p1Wins + 1
        print("Player 1 wins")
    else:
        print("Player 2 wins")
print("\n","Total Player 1 Wins: ", p1Wins)





    #Poker scoring

    #Tier one: Main hand (one byte)
        #RF,SF,4oaK,FH,F,S,ToaK,TP,OP,HC
        #10,9,8,7,6,5,4,3,2,1 
    #Tier two: Main hand val (one byte)
        #A,K,Q,J,T,9,8,7,6,5,4,3,2
    #Tier three: HC val (five bytes)