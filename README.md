# AI Final Project
## Final Report Blog Post
### Problem Statement
Blackjack is a simple gambling game enjoyed by many. Unfortunately while playing blackjack, the odds are stacked against you. To combat this, some blackjack players count cards. By counting cards in a specific way, a player can know when they have an edge over the house. One question that arises from this process is: "how much should I bet when I know I have the edge?". This project aims to answer that question by using reinforcement learning (Q-Learning) to simulate blackjack and find the most advantageous betting amounts given the current game state. 

### Related Solutions
A few card counting simulators already exist. These tools let card counters simulate play with different betting amounts to see what works best. These simulators allow the manipulation of several game variables. My project will cover a smaller scope compared to existing card counter simulations as certain game variables have been restricted (e.g. the game_deck is composed of 1 deck for simplicity). Below are two links to card counting simulators I looked at before working on my project.
* https://www.qfit.com/blackjack-simulator.htm
* https://www.blackjackapprenticeship.com/features/

### Natural Language Description of State Space
The state space of the blackjack game in this project can be represented by all of the possible combinations of cards in the dealer's hand, player's hand, and the count. The blackjack game within this project is played with 1 deck. The cards in the deck are labeled 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, or A. Due to the suit of a card having no real impact on gameplay, suits are omitted. The Dealer and Player are given two cards as soon as a hand starts. Four cards that could be one of thirteen different cards can be represented as 13^4. The state's count can be 1 through 6 . Negative/0 counts are seen as 1, this is because the betting action for a negative count is the same as the action for a count of 1. Counts above 6 are seen as 6, this is due to betting actions for counts higher than 6 being the same as the action for a count of 6. 13^4 * 6 is a rough estimation of the state space for the blackjack problem in this project. This estimation underrepresents the true state space of blackjack. Player's can "hit" and receive another card, this expands the state space.


### Mathematical Description of States, Transitions, Actions and Observations
#### States
This tuple represents the state variables that will be required while implementing reinforcement learning to find a preferable betting amount given a blackjack state. 

    gameState = (player_hand, dealer_hand, count)


#### Transitions
Transitions in this project are seen when a player places a bet, hits, or stands. Placing a bet and getting a new hand deals 4 cards which each have the ability to shift the state. The placed bet directly impacts the reward of a given sequence of hits and stands. 

Dealt cards will decrease the size of the game deck and increase the size of a player or dealer hand.

    deal_cards(current_hand, current_deck) -> len(current_hand) += 1 and len(game_deck) -= 1


In addition, the chance of getting any one card while transitioning to a new state is:


    1/len(game_deck)


#### Actions
Player's are prompted with 6 possible betting actions: 1, 2, 3, 4, 5, or 6. This action is chosen randomly or found in a Q table by the Q-Learning algorithm. Hit or Stand actions are then performed by a simple reflex agent that references a table with perfect blackjack play. Betting actions are evaluated based on their reward. Once a reward is found, by choosing a bet action and designating hit/stand behavior via the reflex agent, it is fed into the Q table (with a calculation) for reference while selecting future betting actions.

Below is an article that explains basic strategy (perfect play)

https://www.math4all.es/the-mathematics-of-blackjack/

#### Observations
The main observation present in this project is the collection of cards that have been previously dealt (without a shuffle). Keeping track of these cards is how you can determine when you have an edge over the house. An aggregate of observations can be used to calculate a true count, which will dictate the current state for Q-learning updates.

* 1 is added for the total number of cards that fall between 2-6  
* 0 is added for the total number of cards that fall between 7-9  
* 1 is subtracted for the total number of cards that fall between 10-A  
* The total is then divided by the number of decks remaining: this number is the true count
* Note: While playing with one deck the running count equals the true count. 1 deck games were utilized for simplicity and to limit the time required for training.

### Implementation
Implementation required four separate python files. blackjack.py is the file where the game logic resides. I built the code in this file by following a Youtube video that detailed a process to create a simple blackjack game with pygame. I made changes and added code based on things I thought I would need to implement my Q-Learning model. The next file is blackjackState.py, this file can be used to create state objects and find all of the possible successors from a given state. The blackjackAgent.py file holds a simple reflex agent and lookup tables that are utilized by the Q-learning algorithm to find optimal moves. Finally, the blackjackRL.py file housed my Q-learning model. 
BlackjackRL... 
* makes calls to blackjack.py to create a game instance for training, it will then
* choose a betting action randomly or via the Q table
* uses a reflex agent to execute a series of hits and stands once a bet has been placed
* Finally, it will use the Q value for the previous state, the new state, and the projected reward to calculate a new Q value for the Q table

Note: Unfortunately I could not effectively pull all of the necessary information from my blackjack instance to execute the Q-Learning model correctly. I believe this is due to the approach I took while setting up my blackjack.py file. To yield more meaningful results, a further endeavour could be rebuilding blackjack.py to ensure the correct update and retrieval of state variables.

### Software and hardware Requirements
I used a Dell XPS to run the project's code. Visual Studio Code was used for coding. The only additional software I used was pygame, below is a link pygame's "Getting Started" page.

    https://www.pygame.org/wiki/GettingStarted

### Motivation
I generally don't like gambling due to the fact that, in most cases, the odds are stacked against you. I recently got into watching some youtube videos about card counting teams. These are groups of card counters with extremely large bankrolls playing highstakes blackjack and turning an incredible profit. The prospect of this is interesting to me and led me to choose a blackjack based project. 

### Accomplishments
* Made modifications to a blackjack.py file in order to allow an agent to make gameplay decisions. Q-Learning is in charge of betting actions and the reflex agent is in charge of hits/stands
* Implemented a state model that allows the projection of possible successor states (disjointed from the Q-Learning model)
* Implemented a reflex agent that will return hit/stand actions based on a lookup table that holds the statistically correct decision for hand combinations
* Implemented a Q-Learning model that is supposed to learn what betting action for a given state is beneficial

### Success Vs Failure
Originally I saw success as a fully implemented optimal Q-Learning Algorithm that would return the best bets for a given state. Due to time constraints this goal was not achieved. My idea of success shifted as I worked on this project. At the time of writing my report I see success as the improvement of my ability to understand the components needed to execute reinforcement learning. I believe if I were to travel back in time with the knowledge I gained from working on this project I would be able to reach my original benchmark for success. 

### Instructions for running code
blackjack.py
* running this file will give you a GUI that represents the game.
* Upon its launch you will be able to change your bet by clicking "7" (7 was chosen as its seen as a lucky number)
* Once your bet is set you can start the game with "Deal Hand"
* Cards will be dealt and you can choose to hit or stand
* If you prefer to use your keyboard 1 can be pressed for hit and 0 can be pressed for stand
* The outcome of your action will be displayed on the screen and in the terminal
* You can adjust your bet
blackjackState.py
* Running this file will return an output detailing the possible successor states for a test state provided in main
blackjackAgent.py
* Running this file will return an output detailing the correct hit/stand action to take given the test state provided in main
blackjackRL
* Running this should populate the a Q table in the file
* Currently running this file will result in an error due to 
