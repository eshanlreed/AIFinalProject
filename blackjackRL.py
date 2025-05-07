#https://www.youtube.com/watch?v=MSrfaI1gGjI
import numpy as np
import random
from blackjack import BlackjackGame 
from blackjackAgent import BlackjackAgent
from blackjackState import BlackjackState


game = BlackjackGame

alpha = .9
discount = 1
exploration = 1
explorationDecay = .9995
minExploration = .01
maxEpisodes = 1000
maxSteps = 100

#state variables that impact state space are.. dealer's upcard (13 choices), player's hand total (can be 4-22), possible count (1-6)
#the available actions are bets sized 1 through 6. Betting is the main action over hit/stand due to the reflex agent handling hit/stand
#3432 combinations - the q table has 3432 spots for entries - lots of training to do!
qTable = {}
#qTable = np.zeros((13 * 22 * 6), (int))

def chooseAction(state):
    if random.uniform(0, 1) < exploration:
        randomBet = random.randint(1, 6)
        return randomBet
    else:
        #qTableBet = np.argmax(qTable[state, :])
        qTableBet = np.max(qTable[state]) if state in qTable else 0.0
        return qTableBet
    
for episode in range(maxEpisodes):
    game.reset_game(game)
    #state is (upcard, playerScoreTotal, count)
    reward = 0
    if not game.dealer_hand:
        upcard = 0
    else:
        upcard = game.dealer_hand[1]
    count = game.count
    pScore = game.player_score
    if game.player_score > 21:
        pScore = 22
    state = (upcard, pScore, count)

    done = False

    for step in range(maxSteps):
        #choose bet (action)
        betAction = chooseAction(state)
        #set bet (with action)
        game.setBet(game, betAction)
        #progress game to new hand or first hand
        if game.initial_deal == False:
            game.dealHand(game)
            print("NEW DEAL REACHED")
        else:
            #print("NEW HAND REACHED")
            game.newHand(game)
        nextState = state
        print(game.hand_active)
        while game.hand_active:
            #reflex agent
            agent = BlackjackAgent()
            #auxillary state
            auxState = BlackjackState(game.game_deck, game.reveal_dealer, game.hand_active, game.my_hand, game.dealer_hand)
            #lookup propper action (hit/stand)
            move = agent.getAction(auxState)
            #apply action with agent
            nextState, reward, done = game.step(move)

        oldVal = qTable.get((state, betAction), 0)
        nextMax = np.max(qTable[nextState]) if nextState in qTable else 0.0
        #nextMax = np.max(qTable[nextState, :])

        qTable[state, betAction] = (1 - alpha) * oldVal + alpha * (reward + discount * nextMax)

        state = nextState

        if done:
            break

    exploration = max(minExploration, exploration * explorationDecay)


    

    