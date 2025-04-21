# AIFinalProject
### Natural Language Description of State Space
The state space of blackjack can be represented by all of the possible combinations of cards in the dealer and player's hand (as well as the game deck). The blackjack game within this project is played with 4 decks. The cards in each deck are labeled as 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, or A. Due to the suit of a card having no real impact on gameplay, suits are omitted. The Dealer and Player are given two cards as soon as a hand starts. Four cards that could be one of thirteen different cards can be represented as 13^4. In reality, 13^4 is an underestimate of the state space of blackjack. Player's can "hit" and receive another card, this expands the state space.


### Mathematical Description of States, Transitions, Actions and Observations
#### States
This tuple represents the state variables that will be required while implementing reinforcement learning to find a preferable betting amount while counting cards and playing blackjack. Note: I may need to make additions to the state while building out the rest of this project  


    gameState = (player_hand, dealer_hand, game_deck, count)


#### Transitions
Transitions in this project are seen when a player requests a new hand or when they hit. Requesting a new hand deals 4 cards which each have the ability to shift the state. Dealt cards will decrease the size of the game deck and increase the size of a player or dealer hand.


    deal_cards(current_hand, current_deck) -> len(current_hand) += 1 and len(game_deck) -= 1


In addition, the chance of getting any one card while transitioning to a new state is:


    1/len(game_deck)


#### Actions
Player's are prompted with 3 different actions: hit, stand, and play again. Hitting allows the player to gain another card, standing reveals the dealer's hold card, and playing again will deal 4 new cards. Actions will be taken based on basic strategy. Basic strategy dictates the statistically correct move to make based on a starting state. The article below explains basic strategy.


https://www.math4all.es/the-mathematics-of-blackjack/


#### Observations
The main observation present in this project is the collection of cards that have been previously dealt (without a shuffle). Keeping track of these cards is how you can predict the values of cards dealt in the future. An aggregate of observations can be used to calculate a true count, which will dictate how an agent plays blackjack.


* 1 is added for the total number of cards that fall between 2-6  
* 0 is added for the total number of cards that fall between 7-9  
* 1 is subtracted for the total number of cards that fall between 10-A  
* The total is then divided by the number of decks remaining: this number is the true count


 

