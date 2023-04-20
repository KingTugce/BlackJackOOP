import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in ["Spades", "Clubs", "Hearts", "Diamonds"] for value in range(1, 14)]
    
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)
    
    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += self.card_value(card)
        
        if card.value == 1:
            self.aces += 1
    
    def card_value(self, card):
        if card.value in [11, 12, 13]:
            return 10
        elif card.value == 1:
            return 11
        else:
            return card.value
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        
        for i in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())
        
    def play(self):
        print("Welcome to Blackjack!")
        print("Player: ", self.player_hand.cards, self.player_hand.value)
        print("Dealer: ", [self.dealer_hand.cards[0], "X"])
        
        while True:
            action = input("Do you want to [H]it or [S]tand? ").lower()
            
            if action == "h":
                self.player_hand.add_card(self.deck.deal())
                self.player_hand.adjust_for_ace()
                print("Player: ", self.player_hand.cards, self.player_hand.value)
                
                if self.player_hand.value > 21:
                    print("Bust! You lose.")
                    break
            elif action == "s":
                while self.dealer_hand.value < 17:
                    self.dealer_hand.add_card(self.deck.deal())
                    self.dealer_hand.adjust_for_ace()
                
                print("Player: ", self.player_hand.cards, self.player_hand.value)
                print("Dealer: ", self.dealer_hand.cards, self.dealer_hand.value)
                
                if self.dealer_hand.value > 21:
                    print("Dealer busts! You win.")
                    break
                elif self.dealer_hand.value > self.player_hand.value:
                    print("You lose.")
                    break
                elif self.dealer_hand.value < self.player_hand.value:
                    print("You win!")
                    break
                else:
                    print("It's a tie!")
                    break
                    
if __name__ == '__main__':
    game = Game()
    game.play()
