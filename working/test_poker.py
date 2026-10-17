import poker

def test_deck_cards():
    deck = poker.Deck()
    assert len(deck.cards) == 52

def test_get_cards():
    deck = poker.Deck()
    hand = deck.get_cards(5)
    assert len(hand) == 5
    assert len(deck.cards) == 48

def test_three_of_a_kind():
    # remember that in class Card: def __init__(self, suit=1, rank=2)
    # I want to take 5 cards
    hand = [poker.Card(1, 4), poker.Card(2, 4), poker.Card(3, 10), poker.Card(3, 4), poker.Card(2, 11)]
    assert poker.three_of_a_kind(hand) == True
