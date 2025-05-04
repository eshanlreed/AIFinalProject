import blackjack
import blackjackState


class BlackjackAgent:

    #basic strategy - hard totals
    #lookup is done with [['dealer upcard'], ['player score']]]
    hardTotalDic = {}
    #dealer upcard -> 2
    # dealer upcard -> 2
    hardTotalDic[('2', '17')] = "stand"
    hardTotalDic[('2', '16')] = "stand"
    hardTotalDic[('2', '15')] = "stand"
    hardTotalDic[('2', '14')] = "stand"
    hardTotalDic[('2', '13')] = "stand"
    hardTotalDic[('2', '12')] = "hit"
    hardTotalDic[('2', '11')] = "hit"
    hardTotalDic[('2', '10')] = "hit"
    hardTotalDic[('2', '9')] = "hit"
    hardTotalDic[('2', '8')] = "hit"
    # dealer upcard -> 3
    hardTotalDic[('3', '17')] = "stand"
    hardTotalDic[('3', '16')] = "stand"
    hardTotalDic[('3', '15')] = "stand"
    hardTotalDic[('3', '14')] = "stand"
    hardTotalDic[('3', '13')] = "stand"
    hardTotalDic[('3', '12')] = "hit"
    hardTotalDic[('3', '11')] = "hit"
    hardTotalDic[('3', '10')] = "hit"
    hardTotalDic[('3', '9')] = "hit"
    hardTotalDic[('3', '8')] = "hit"
    # dealer upcard -> 4
    hardTotalDic[('4', '17')] = "stand"
    hardTotalDic[('4', '16')] = "stand"
    hardTotalDic[('4', '15')] = "stand"
    hardTotalDic[('4', '14')] = "stand"
    hardTotalDic[('4', '13')] = "stand"
    hardTotalDic[('4', '12')] = "stand"
    hardTotalDic[('4', '11')] = "hit"
    hardTotalDic[('4', '10')] = "hit"
    hardTotalDic[('4', '9')] = "hit"
    hardTotalDic[('4', '8')] = "hit"
    # dealer upcard -> 5
    hardTotalDic[('5', '17')] = "stand"
    hardTotalDic[('5', '16')] = "stand"
    hardTotalDic[('5', '15')] = "stand"
    hardTotalDic[('5', '14')] = "stand"
    hardTotalDic[('5', '13')] = "stand"
    hardTotalDic[('5', '12')] = "stand"
    hardTotalDic[('5', '11')] = "hit"
    hardTotalDic[('5', '10')] = "hit"
    hardTotalDic[('5', '9')] = "hit"
    hardTotalDic[('5', '8')] = "hit"
    # dealer upcard -> 6
    hardTotalDic[('6', '17')] = "stand"
    hardTotalDic[('6', '16')] = "stand"
    hardTotalDic[('6', '15')] = "stand"
    hardTotalDic[('6', '14')] = "stand"
    hardTotalDic[('6', '13')] = "stand"
    hardTotalDic[('6', '12')] = "stand"
    hardTotalDic[('6', '11')] = "hit"
    hardTotalDic[('6', '10')] = "hit"
    hardTotalDic[('6', '9')] = "hit"
    hardTotalDic[('6', '8')] = "hit"
    # dealer upcard -> 7
    hardTotalDic[('7', '17')] = "stand"
    hardTotalDic[('7', '16')] = "hit"
    hardTotalDic[('7', '15')] = "hit"
    hardTotalDic[('7', '14')] = "hit"
    hardTotalDic[('7', '13')] = "hit"
    hardTotalDic[('7', '12')] = "hit"
    hardTotalDic[('7', '11')] = "hit"
    hardTotalDic[('7', '10')] = "hit"
    hardTotalDic[('7', '9')] = "hit"
    hardTotalDic[('7', '8')] = "hit"
    # dealer upcard -> 8
    hardTotalDic[('8', '17')] = "stand"
    hardTotalDic[('8', '16')] = "hit"
    hardTotalDic[('8', '15')] = "hit"
    hardTotalDic[('8', '14')] = "hit"
    hardTotalDic[('8', '13')] = "hit"
    hardTotalDic[('8', '12')] = "hit"
    hardTotalDic[('8', '11')] = "hit"
    hardTotalDic[('8', '10')] = "hit"
    hardTotalDic[('8', '9')] = "hit"
    hardTotalDic[('8', '8')] = "hit"
    # dealer upcard -> 9
    hardTotalDic[('9', '17')] = "stand"
    hardTotalDic[('9', '16')] = "hit"
    hardTotalDic[('9', '15')] = "hit"
    hardTotalDic[('9', '14')] = "hit"
    hardTotalDic[('9', '13')] = "hit"
    hardTotalDic[('9', '12')] = "hit"
    hardTotalDic[('9', '11')] = "hit"
    hardTotalDic[('9', '10')] = "hit"
    hardTotalDic[('9', '9')] = "hit"
    hardTotalDic[('9', '8')] = "hit"
    # dealer upcard -> 10
    hardTotalDic[('10', '17')] = "stand"
    hardTotalDic[('10', '16')] = "hit"
    hardTotalDic[('10', '15')] = "hit"
    hardTotalDic[('10', '14')] = "hit"
    hardTotalDic[('10', '13')] = "hit"
    hardTotalDic[('10', '12')] = "hit"
    hardTotalDic[('10', '11')] = "hit"
    hardTotalDic[('10', '10')] = "hit"
    hardTotalDic[('10', '9')] = "hit"
    hardTotalDic[('10', '8')] = "hit"
    # dealer upcard -> A
    hardTotalDic[('A', '17')] = "stand"
    hardTotalDic[('A', '16')] = "hit"
    hardTotalDic[('A', '15')] = "hit"
    hardTotalDic[('A', '14')] = "hit"
    hardTotalDic[('A', '13')] = "hit"
    hardTotalDic[('A', '12')] = "hit"
    hardTotalDic[('A', '11')] = "hit"
    hardTotalDic[('A', '10')] = "hit"
    hardTotalDic[('A', '9')] = "hit"
    hardTotalDic[('A', '8')] = "hit"

    #basic strategy - soft totals
    #lookup is done with [['dealer upcard'], ['player score without ace']]]
    #only considers hands with an A and total < 9 (without counting the ace)
    softTotalDic = {}
    #dealer upcard -> 2
    softTotalDic[('2', '9')] = "stand"
    softTotalDic[('2', '8')] = "stand"
    softTotalDic[('2', '7')] = "stand"
    softTotalDic[('2', '6')] = "hit"
    softTotalDic[('2', '5')] = "hit"
    softTotalDic[('2', '4')] = "hit"
    softTotalDic[('2', '3')] = "hit"
    softTotalDic[('2', '2')] = "hit"
    #dealer upcard -> 3
    softTotalDic[('3', '9')] = "stand"
    softTotalDic[('3', '8')] = "stand"
    softTotalDic[('3', '7')] = "stand"
    softTotalDic[('3', '6')] = "hit"
    softTotalDic[('3', '5')] = "hit"
    softTotalDic[('3', '4')] = "hit"
    softTotalDic[('3', '3')] = "hit"
    softTotalDic[('3', '2')] = "hit"
    #dealer upcard -> 4
    softTotalDic[('4', '9')] = "stand"
    softTotalDic[('4', '8')] = "stand"
    softTotalDic[('4', '7')] = "stand"
    softTotalDic[('4', '6')] = "hit"
    softTotalDic[('4', '5')] = "hit"
    softTotalDic[('4', '4')] = "hit"
    softTotalDic[('4', '3')] = "hit"
    softTotalDic[('4', '2')] = "hit"
    #dealer upcard -> 5
    softTotalDic[('5', '9')] = "stand"
    softTotalDic[('5', '8')] = "stand"
    softTotalDic[('5', '7')] = "stand"
    softTotalDic[('5', '6')] = "hit"
    softTotalDic[('5', '5')] = "hit"
    softTotalDic[('5', '4')] = "hit"
    softTotalDic[('5', '3')] = "hit"
    softTotalDic[('5', '2')] = "hit"
    #dealer upcard -> 6
    softTotalDic[('6', '9')] = "stand"
    softTotalDic[('6', '8')] = "stand"
    softTotalDic[('6', '7')] = "stand"
    softTotalDic[('6', '6')] = "hit"
    softTotalDic[('6', '5')] = "hit"
    softTotalDic[('6', '4')] = "hit"
    softTotalDic[('6', '3')] = "hit"
    softTotalDic[('6', '2')] = "hit"
    #dealer upcard -> 7
    softTotalDic[('7', '9')] = "stand"
    softTotalDic[('7', '8')] = "stand"
    softTotalDic[('7', '7')] = "stand"
    softTotalDic[('7', '6')] = "hit"
    softTotalDic[('7', '5')] = "hit"
    softTotalDic[('7', '4')] = "hit"
    softTotalDic[('7', '3')] = "hit"
    softTotalDic[('7', '2')] = "hit"
    #dealer upcard -> 8
    softTotalDic[('8', '9')] = "stand"
    softTotalDic[('8', '8')] = "stand"
    softTotalDic[('8', '7')] = "stand"
    softTotalDic[('8', '6')] = "hit"
    softTotalDic[('8', '5')] = "hit"
    softTotalDic[('8', '4')] = "hit"
    softTotalDic[('8', '3')] = "hit"
    softTotalDic[('8', '2')] = "hit"
    #dealer upcard -> 9
    softTotalDic[('9', '9')] = "stand"
    softTotalDic[('9', '8')] = "stand"
    softTotalDic[('9', '7')] = "hit"
    softTotalDic[('9', '6')] = "hit"
    softTotalDic[('9', '5')] = "hit"
    softTotalDic[('9', '4')] = "hit"
    softTotalDic[('9', '3')] = "hit"
    softTotalDic[('9', '2')] = "hit"
    #dealer upcard -> 10
    softTotalDic[('10', '9')] = "stand"
    softTotalDic[('10', '8')] = "stand"
    softTotalDic[('10', '7')] = "hit"
    softTotalDic[('10', '6')] = "hit"
    softTotalDic[('10', '5')] = "hit"
    softTotalDic[('10', '4')] = "hit"
    softTotalDic[('10', '3')] = "hit"
    softTotalDic[('10', '2')] = "hit"
    #dealer upcard -> A
    softTotalDic[('A', '9')] = "stand"
    softTotalDic[('A', '8')] = "stand"
    softTotalDic[('A', '7')] = "hit"
    softTotalDic[('A', '6')] = "hit"
    softTotalDic[('A', '5')] = "hit"
    softTotalDic[('A', '4')] = "hit"
    softTotalDic[('A', '3')] = "hit"
    softTotalDic[('A', '2')] = "hit"

    #sums a given hand, will consider As as 11 due to the fact that soft aces are caught by the reflex agent
    def sumHand(self, hand):
        total = 0
        for card in hand:
            if card == '2':
                total += 2
            if card == '3':
                total += 3
            if card == '4':
                total += 4
            if card == '5':
                total += 5
            if card == '6':
                total += 6
            if card == '7':
                total += 7
            if card == '8':
                total += 8
            if card == '9':
                total += 9
            if card == 'K' or card == 'Q' or card == 'J' or card == '10':
                total += 10
            if card == 'A':
                total += 11
        return total
        
    #implement an agent for basic strategy
    def getAction(self, state: blackjackState.BlackjackState):
        playerHand = state.player_hand.copy()
        dealerHand = state.dealer_hand.copy()
        dealerUpCard = dealerHand[0]
        print(dealerUpCard)
        if 'A' in playerHand:
            print("YUP ACE HERE")
            withoutAce = playerHand.copy()
            withoutAce.remove('A')
            withoutAceTotal = self.sumHand(withoutAce)
            if withoutAceTotal < 10:
                return self.softTotalDic[(dealerUpCard, str(withoutAceTotal))]
            
        handTotal = self.sumHand(player_hand)
        return self.hardTotalDic[(dealerUpCard, str(handTotal))]

if __name__ == "__main__":
    #test code to ensure propper lookup
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    reveal_dealer = False
    hand_active = True
    player_hand = ["A", "9"]
    dealer_hand = ["A", "7"]
    test = blackjackState.BlackjackState(deck, reveal_dealer, hand_active, player_hand, dealer_hand)
    agent = BlackjackAgent()
    action = agent.getAction(test)
    print(action)






