

class BlackjackState:  

    #constructor for a blackjack state
    def __init__(self, deck, reveal_dealer, hand_active, player_hand, dealer_hand):
        self.deck = deck
        self.reveal_dealer = reveal_dealer
        self.hand_active = hand_active
        self.player_hand = player_hand
        self.dealer_hand = dealer_hand
    
    #return available actions based on current gamestate
    def getAvailableActions(self):
        active = self.hand_active
        if active:
            return ["hit", "stand"]
        else:
            return []
    
    #Returns viable successor states
    def getSuccessors(self, action):
        possDealerHands = []
        possPlayerHands = []
        succs = []
        currDeck = self.deck
        if self.hand_active:
            if action == "stand":
                #dealer's turn state
                ret = BlackjackState(self.deck, True, False, self.player_hand, self.dealer_hand)
                succs.append(ret)
                return succs
            #returns states with all possible player hands based on the current deck
            if action == "hit":
                for card in currDeck:
                    pHand = self.player_hand.copy()
                    pHand.append(card)
                    newDeck = self.deck.copy()
                    newDeck.remove(card)
                    ret = BlackjackState(newDeck, self.reveal_dealer, self.hand_active, pHand, self.dealer_hand)
                    succs.append(ret)

        else:
            #returns states with all possible dealer hands based on the current deck
            for card in currDeck:
                dHand = self.dealer_hand.copy()
                dHand.append(card)
                newDeck = self.deck.copy()
                newDeck.remove(card)
                ret = BlackjackState(newDeck, self.reveal_dealer, self.hand_active, self.player_hand, dHand)
                succs.append(ret)
        return succs
        
        
#main function for testing
if __name__ == "__main__":
    #sample inputs
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    reveal_dealer = False
    hand_active = True
    player_hand = ["2", "10"]
    dealer_hand = ["A", "7"]
    test = BlackjackState(deck, reveal_dealer, hand_active, player_hand, dealer_hand)
    #prints available actions
    print(test.getAvailableActions())
    #gathers and then prints the available successors
    succs = test.getSuccessors("hit")
    for succ in succs:
        print("deck: ")
        print(succ.deck)
        print("reveal dealer: ")
        print(succ.reveal_dealer)
        print("hand active: ")
        print(succ.hand_active)
        print("player hand: ")
        print(succ.player_hand)
        print("dealer hand: ")
        print(succ.dealer_hand)

        

