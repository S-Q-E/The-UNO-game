import random


def buildDeck():
    """
    The function generate UNO deck
    :return: deck
    """
    deck = []
    colours = ['Red', 'Green', 'Blue', 'Yellow']
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Draw Two", "Reverse", "Skip"]
    wilds = ["Wild", "Wild Draw Four"]
    for colour in colours:
        for value in values:
            cardVal = f"{colour} {value}"
            deck.append(cardVal)
            if value != 0:
                deck.append(cardVal)
    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])
    return deck


def shuffle_deck(deck):
    """
    Shuffle given deck of cards which passed into it
    :param deck -> list
    :return: deck -> list
    """
    for cardPos in range(len(deck)):
        randPos = random.randint(0, 107)
        deck[cardPos], deck[randPos] = deck[randPos], deck[cardPos]
    return deck


def show_hand(player: int, player_hand: list):
    """
    This function print to the screen your hand
    :param player: number of player,
    :param player_hand: list
    :return: None
    """
    print(f"PLAYER' {player + 1} TURN")
    print(f"*" * 10, "Your hand", "*" * 10)
    print("*" * 25)
    y = 1
    for card in player_hand:
        print(f"[{y}] {card}")
        y += 1
    print("")


def canPlay(colour, value, player_hand):
    """
    Check whether a player is available to play a card, or not
    :param discard_card: str
    :param player_hand: list
    :return: boolean
    """
    for card in player_hand:
        if "Wild" in card:
            return True
        elif colour in card or value in card:
            return True
    return False


def draw_cards(numCards):
    """
    Draw card function that draws a specific number of cards
    off the top of the deck
    :param numCards: integer
    :return: list
    """

    cardsDrawn = []
    for x in range(numCards):
        cardsDrawn.append(unoDeck.pop(0))
    return cardsDrawn


unoDeck = buildDeck()
unoDeck = shuffle_deck(unoDeck)
unoDeck = shuffle_deck(unoDeck)
discards = []

players = []
colours = ['Red', 'Green', 'Blue', 'Yellow']
numplayers = int(input("How many players?  "))
while numplayers < 2 or numplayers > 4:
    numplayers = int(input("Invalid. Please enter a number between 2-4. How many players?"))
for player in range(numplayers):
    players.append(draw_cards(5))


players_turn = 0
play_direction = 1
playing = True
discards.append(unoDeck.pop(0))
split_card = discards[0].split(" ", 1)
current_color = split_card[0]
if current_color != "Wild":
    card_val = split_card[1]
else:
    card_val = "Any"


while playing:
    show_hand(players_turn, players[players_turn])
    print(f"Card on top of discard pile: {discards[-1]}")
    if canPlay(current_color, card_val, players[players_turn]):
        cardChosen = int(input("Which card you want to play? "))
        while not canPlay(current_color, card_val, [players[players_turn][cardChosen-1]]):
            cardChosen = int(input("invalid card! Which card you want to play? "))
        print(f"You played {players[players_turn][cardChosen-1]}")
        discards.append(players[players_turn].pop(cardChosen-1))
        # Check players won
        if len(players[players_turn]) == 0:
            playing = False
            winner = f"Congratulations! Player {players_turn + 1}"
        else:
            # Check special cards
            split_card = discards[-1].split(" ", 1)
            current_color = split_card[0]
            if len(split_card) == 1:
                card_val = "Any"
            else:
                card_val = split_card[1]
            if current_color == "Wild":
                for x in range(len(colours)):
                    print(f"[{x + 1}] {colours[x]}")
                new_color = int(input("What color would you like to choose"))
                while new_color < 1 or new_color > 4:
                    new_color = int(input("Invalid option. What color would you like to choose"))
                current_color = colours[new_color - 1]
            if card_val == 'Reverse':
                play_direction = play_direction * -1
            elif card_val == 'Skip':
                players_turn += play_direction
                if players_turn >= numplayers:
                    players_turn = 0
                elif players_turn < 0:
                    players_turn = numplayers - 1
            elif card_val == 'Draw Two':
                player_draw = players_turn + play_direction
                if player_draw == numplayers:
                    player_draw = 0
                elif players_turn < 0:
                    player_draw = numplayers - 1
                players[players_turn].extend(draw_cards(2))
                # players_turn += play_direction
            elif card_val == "Draw Four":
                player_draw = players_turn + play_direction
                if player_draw == numplayers:
                    player_draw = 0
                elif players_turn < 0:
                    player_draw = numplayers - 1
                players[player_draw].extend(draw_cards(4))
    else:
        print("You can't play. You have to draw a card")
        players[players_turn].extend(draw_cards(1))

    players_turn += play_direction
    if players_turn >= numplayers:
        players_turn = 0
    elif players_turn < 0:
        players_turn = numplayers - 1

print("Game Over!")
print(winner)

