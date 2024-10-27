"""import random

def play():

    user = input("What's your choice? 'r' for rocks, 'p' for papers, 's' for scissors\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return "It\'s a tie"

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'


def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

result = play()
print(result)
"""


import random

def play():
    user = input("What's your choice? 'r' for rocks, 'p' for papers, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    print(f"Computer chose: {computer}")

    if user == computer:
        return "It's a tie"

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

# Call the play function to start the game
result = play()
print(result)
