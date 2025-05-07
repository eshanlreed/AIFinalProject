#Utilized https://www.youtube.com/watch?v=e3YkdOXhFpQ to build the base of the game
#I expanded the game to better work with Q-Learning
import copy
import random
import pygame

# Game constants
pygame.init()
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
one_deck = 4 * cards
decks = 1
WIDTH = 600
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Pygame Blackjack")
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 44)
smallerfont = pygame.font.Font('freesansbold.ttf', 36)

class BlackjackGame:
    def __init__(self):
        self.game_deck = copy.deepcopy(decks * one_deck)
        #wins, losses, pushes
        self.records = [0, 0, 0]
        self.count = 0
        self.balance = 100
        self.bet = 1
        self.reset_hand()

    #Resets hand specific variables
    def reset_hand(self):
        self.player_score = 0
        self.dealer_score = 0
        self.my_hand = []
        self.dealer_hand = []
        self.outcome = 0
        self.reveal_dealer = False
        self.hand_active = False
        self.add_score = False
        self.initial_deal = False
        self.active = False
        self.results = ['', 'Player Busted :(', 'Player Wins :)', 'Dealer Wins :(', 'Push!']
        self.episode_over = len(self.game_deck) == 0
        
    #resets game variables
    def reset_game(self):
        self.count = 0
        self.game_deck = copy.deepcopy(decks * one_deck)
        self.records = [0, 0, 0]
        self.reset_hand()
    
    #pass in player/dealer hand to calculate hand score & check aces
    def calculate_score(self, hand):
        hand_score = 0
        aces_count = hand.count('A')
        for card in hand:
            if card in ['J', 'Q', 'K']:
                hand_score += 10
            elif card == 'A':
                hand_score += 11
            else:
                hand_score += int(card)
        
        while hand_score > 21 and aces_count > 0:
            hand_score -= 10
            aces_count -= 1
        return hand_score
    
    # deal cards by selecting randomly from the deck. 1 at a time
    def deal_cards(self, current_hand, num=1):
        #Deal cards from remaining deck
        for _ in range(num):
            if len(self.game_deck) == 0:
                self.episode_over = True
                return current_hand
            card = random.choice(self.game_deck)
            current_hand.append(card)
            self.game_deck.remove(card)
            self.updateCount(card)
        return current_hand
    
    #updates the count based on what cards have been dealt
    def updateCount(self, card):
        if card == '2' or card == '3' or card == '4' or card == '5' or card == '6':
            self.count += 1
        if card == '10' or card == 'J' or card == 'Q' or card == 'K' or card == 'A':
            self.count -= 1

    #cycles bets through 1, 2, 3, 4, 5, 6
    def changeBet(self):
        if self.bet < 6:
            self.bet += 1
        elif self.bet >= 6:
            self.bet = 1

    #sets a bet exactly
    def setBet(self, bet):
        self.bet = bet

    #dealHand simulates the clicking of deal hand
    def dealHand(self):
        if not self.active:
            self.reset_hand()
            self.active = True
            self.initial_deal = True
            #deal right away
            self.my_hand = self.deal_cards(self.my_hand, 2)
            self.dealer_hand = self.deal_cards(self.dealer_hand, 2)
            #deals cards if there are cards left to deal
            if not self.episode_over:
                self.player_score = self.calculate_score(self.my_hand)
                self.hand_active = True
                self.add_score = True
            else:
                self.active = False

    #newHand simulate sthe clicking of new hand
    def newHand(self):
        self.reset_hand()
        self.active = True
        self.initial_deal = True
        #deal right away
        self.my_hand = self.deal_cards(self.my_hand, 2)
        self.dealer_hand = self.deal_cards(self.dealer_hand, 2)
        #deals cards if there are cards left to deal
        if not self.episode_over:
            self.player_score = self.calculate_score(self.my_hand)
            self.hand_active = True
            self.add_score = True
        else:
            self.active = False
          
    #executes hits/stands and progresses the game
    def step(self, action):
        if self.episode_over:
            print("Deck exhausted! Game over.")
            return
        
        reward = 0
        done = False

        #hit
        if action == 1:
            self.my_hand = self.deal_cards(self.my_hand)
            if self.episode_over:
                print("Deck exhausted during hit!")
                return
            
            self.player_score = self.calculate_score(self.my_hand)
            print(f"New Player Hand: {self.my_hand} (Score: {self.player_score})")
            
            #player bust
            if self.player_score > 21:
                self.hand_active = False
                self.reveal_dealer = True
                self.outcome = 1
                reward = -1 * self.bet
                done = True
                print("PLAYER BUSTED!")
                if self.add_score:
                    self.balance -= self.bet
                    self.records[1] += 1
                    self.add_score = False
                
        #stand
        elif action == 0:
            self.hand_active = False
            self.reveal_dealer = True
            self.dealer_score = self.calculate_score(self.dealer_hand)
            print(f"Dealer reveals hand: {self.dealer_hand} (Score: {self.dealer_score})")
            
            # Dealer hits until >= 17 or deck exhausted
            while self.dealer_score < 17 and not self.episode_over:
                self.dealer_hand = self.deal_cards(self.dealer_hand)
                if self.episode_over:
                    print("Deck exhausted during dealer's turn!")
                    break
                self.dealer_score = self.calculate_score(self.dealer_hand)
                print(f"Dealer hits: {self.dealer_hand[-1]} | New score: {self.dealer_score}")
            
            # Determine outcome
            if self.player_score > 21:
                self.balance -= self.bet
                self.outcome = 1
                reward = -1 * self.bet
                print("Player busted - dealer wins")
            elif self.dealer_score > 21:
                self.balance += self.bet
                self.outcome = 2
                reward = 1 * self.bet
                print("Dealer busted - player wins")
            elif self.player_score > self.dealer_score:
                self.balance += self.bet
                self.outcome = 2
                reward = 1 * self.bet
                print(f"Player wins {self.player_score} vs {self.dealer_score}")
            elif self.player_score < self.dealer_score:
                self.balance -= self.bet
                self.outcome = 3
                reward = -1 * self.bet
                print(f"Dealer wins {self.dealer_score} vs {self.player_score}")
            else:
                self.outcome = 4
                reward = 0
                print(f"Push at {self.player_score}")
                
            done = True
            if self.add_score:
                if self.outcome == 1 or self.outcome == 3:
                    self.records[1] += 1
                elif self.outcome == 2:
                    self.records[0] += 1
                else:
                    self.records[2] += 1
                self.add_score = False
        
        #Print action results - for debugging
        print("\nACTION RESULT:")
        print(f"Player Hand: {self.my_hand} (Score: {self.player_score})")
        print(f"Dealer Hand: {self.dealer_hand} (Score: {self.dealer_score})")
        print(f"Reward: {reward} | Done: {done}")
        print(f"Cards remaining: {len(self.game_deck)}")
        print(f"Records: Wins={self.records[0]} Losses={self.records[1]} Pushes={self.records[2]}")
        upCard = self.dealer_hand[1]
        pScore = self.player_score
        tcount = self.count 
        state = (upCard, pScore, tcount)
        handDone = False
        if action == 0:
            handDone = True
        
        #return state, reward, self.hand_active
        return state, reward, handDone
    
    #updates the drawn objects on screen
    def render(self):
        screen.fill('black')
        
        #draw scores
        screen.blit(font.render(f'Score[{self.player_score}]', True, 'white'), (350, 400))
        if self.reveal_dealer:
            screen.blit(font.render(f'Score[{self.dealer_score}]', True, 'white'), (350, 100))
        
        #draw cards remaining
        screen.blit(smallerfont.render(f'Cards left: {len(self.game_deck)}', True, 'white'), (20, 10))

        #draw count
        screen.blit(smallerfont.render(f'Count: {self.count}', True, 'white'), (400, 10))
        #draw balance
        screen.blit(smallerfont.render(f'Bal: {self.balance}', True, 'white'), (400, 40))
        #draw bet
        screen.blit(smallerfont.render(f'Bet: {self.bet}', True, 'white'), (400, 650))
        
        #draw cards
        for i in range(len(self.my_hand)):
            pygame.draw.rect(screen, 'white', [70 + (70 * i), 460 + (5 * i), 120, 220], 0, 5)
            screen.blit(font.render(self.my_hand[i], True, 'black'), ((75 + 70 * i), (465 + 5*i)))
            screen.blit(font.render(self.my_hand[i], True, 'black'), ((75 + 70 * i), (635 + 5*i)))
            pygame.draw.rect(screen, 'red', [70 + (70 * i), 460 + (5 * i), 120, 220], 5, 5)

        for i in range(len(self.dealer_hand)):
            pygame.draw.rect(screen, 'white', [70 + (70 * i), 160 + (5 * i), 120, 220], 0, 5)
            if i != 0 or self.reveal_dealer:
                screen.blit(font.render(self.dealer_hand[i], True, 'black'), ((75 + 70 * i), (165 + 5*i)))
                screen.blit(font.render(self.dealer_hand[i], True, 'black'), ((75 + 70 * i), (335 + 5*i)))
            else:
                screen.blit(font.render('???', True, 'black'), ((75 + 70 * i), (165 + 5*i)))
                screen.blit(font.render('???', True, 'black'), ((75 + 70 * i), (335 + 5*i)))
            pygame.draw.rect(screen, 'red', [70 + (70 * i), 160 + (5 * i), 120, 220], 5, 5)
        
        #draw buttons and game info
        buttons = self.draw_buttons()
        pygame.display.flip()
        return buttons
    
    #draws buttons visually onto the screen
    def draw_buttons(self):
        button_list = []
        if not self.active:
            deal = pygame.draw.rect(screen, 'white', [150, 20, 300, 100], 0, 5)
            pygame.draw.rect(screen, 'green', [150, 20, 300, 100], 3, 5)
            deal_text = font.render('DEAL HAND', True, 'black')
            screen.blit(deal_text, (165, 50))
            button_list.append(deal)
        else:
            hit = pygame.draw.rect(screen, 'white', [0, 700, 300, 100], 0, 5)
            pygame.draw.rect(screen, 'green', [0, 700, 300, 100], 3, 5)
            hit_text = font.render('HIT ME', True, 'black')
            screen.blit(hit_text, (55, 735))
            button_list.append(hit)

            stand = pygame.draw.rect(screen, 'white', [300, 700, 300, 100], 0, 5)
            pygame.draw.rect(screen, 'green', [300, 700, 300, 100], 3, 5)
            stand_text = font.render('STAND', True, 'black')
            screen.blit(stand_text, (355, 735))
            button_list.append(stand)

            score_text = smallerfont.render(f'Wins: {self.records[0]}   Losses: {self.records[1]}   Pushes: {self.records[2]}', True, 'white')
            screen.blit(score_text, (15, 840))
        
        if self.outcome != 0:
            screen.blit(font.render(self.results[self.outcome], True, 'white'), (15, 40))
            deal = pygame.draw.rect(screen, 'white', [150, 220, 300, 100], 0, 5)
            pygame.draw.rect(screen, 'green', [150, 220, 300, 100], 3, 5)
            pygame.draw.rect(screen, 'black', [153, 223, 294, 94], 3, 5)
            deal_text = font.render('NEW HAND', True, 'black')
            screen.blit(deal_text, (165, 250))
            button_list.append(deal)
        
        return button_list

def main():
    game = BlackjackGame()
    run = True
    
    while run:
        timer.tick(fps)
        
        if game.initial_deal and game.active:
            game.initial_deal = False
        
        buttons = game.render()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            #these key presses are used to test step() manually
            if event.type == pygame.KEYDOWN:
                # Press 1 to test HIT
                if event.key == pygame.K_1:  
                    print("\nTesting HIT action:")
                    state, reward, done = game.step(1)
                    print(f"Reward: {reward}, Done: {done}")
                # Press 0 to test STAND
                elif event.key == pygame.K_0:  
                    print("\nTesting STAND action:")
                    state, reward, done = game.step(0)
                    print(f"Reward: {reward}, Done: {done}")
                # Press 7 to cycle the bet
                elif event.key == pygame.K_7:  
                    game.changeBet()

            #calls step if a user interacts with the game
            if event.type == pygame.MOUSEBUTTONUP:
                if not game.active:
                    if buttons[0].collidepoint(event.pos):
                        game.dealHand()
                        #game.active = True
                        #game.initial_deal = True
                else:
                    #hit
                    if buttons[0].collidepoint(event.pos) and game.player_score < 21 and game.hand_active:
                        game.step(1)
                    #stand
                    elif buttons[1].collidepoint(event.pos) and not game.reveal_dealer:
                        game.step(0)
                    elif len(buttons) == 3:
                        if buttons[2].collidepoint(event.pos):
                            game.reset_hand()
                            game.newHand()
                            #game.active = True
                            #game.initial_deal = True
        
        if game.hand_active and game.player_score >= 21:
            game.step(0)

    pygame.quit()

if __name__ == "__main__":
    main()