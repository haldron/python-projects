#util module for containing needed functions

#function to check if user input is within range
def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

#function to print which option selected by user
def print_hand(hand, name='Guest'):
    hands = ['Rock', 'Paper', 'Scissors']
    print(name + ' picked: ' + hands[hand])

#function to judge who wins
def judge(player, computer):
    if player == computer:
        return 'Draw'
    elif player == 0 and computer == 1:
        return 'Lose'
    elif player == 1 and computer == 2:
        return 'Lose'
    elif player == 2 and computer == 0:
        return 'Lose'
    else:
        return 'Win'