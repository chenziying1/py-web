import random

class card():
    RANKS = ["A","2","3","4","5","6","7","8","9","10","J","q","k"]
    SUITS = ["梅","方","红","黑"]

    def __init__(self,rank,suit,face_up=True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = self.suit + self.rank
        else:
            rep = 'xx'
        return rep

    def pic_order(self):
        if self.rank=='A':
            FaceNum=1
        elif self.rank=='J':
            FaceNum=11
        elif self.rank=='Q':
            FaceNum=12
        elif self.rank=='K':
            FaceNum=13
        else:
            FaceNum = int(self.rank)

        if self.suit == "梅":
            suit = 1
        elif self.suit == "方":
            suit = 2
        elif self.suit == "红":
            suit = 3
        else:
            suit = 4
        return (suit-1)*13+FaceNum

    def flip(self):
        self.is_face_up=not self.is_face_up

class Hand():
    def __init__(self):
        self.cards=[]

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "无牌"
        return rep

    def clear(self):
        self.cards=[]

    def add(self, card):
        self.cards.append(card)

    def give(self,other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Poke(Hand):
    def populate(self):
        for suit in card.SUITS:
            for rank in card.RANKS:
                self.add(card(rank,suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self,hands,per_hand=13):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.cards.remove(top_card)
                    hand.add(top_card)
                else:
                    print("牌已发完")

print("the game start!")
players=[Hand(),Hand(),Hand(),Hand()]
pokel = Poke()
pokel.populate()
pokel.shuffle()
pokel.deal(players,13)
n=1
for hand in players:
    print("牌手",n,end=":")
    print(hand)
    n=n+1
input("\nexit")