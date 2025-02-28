import random
import blackjackart as art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def init_deck():
    player_total = 0
    agent_total = 0

    for i in range(0,2):
        player.append(random.choice(cards))
        agent.append(random.choice(cards))
        player_total += player[i]
        agent_total += agent[i]
    print(f"Your cards: {player}, current score: {player_total}")
    print(f"Computer's first card: {agent[0]}")

def get_deal():
    hit_stand = "y"
    while hit_stand == "y":
        hit_stand = input(f"Type 'y' to get another card, type 'n' to pass:")
        if hit_stand == "y":
            player.append(random.choice(cards))
            if sum(player)>21:
                for i in range(0,len(player)):
                    if player[i]==11:
                        player[i]=1

            print(f"Your cards: {player}, current score: {sum(player)}")
            if sum(player) > 21:
                print(f"Computer's first card: {agent[0]}, final score: {agent[0]}")
                print("You went over. You loose!")
                return 1
        else:
            print(f"Your final hand: {player}, Final score: {sum(player)}")
            return 0

def agent_deal():
    agent_run = 'yes'
    while agent_run == 'yes':
        if sum(agent)<17:
            agent.append(random.choice(cards))
            if sum(agent)>21:
                for i in range(0,len(agent)):
                    if agent[i]==11:
                        agent[i]=1
            if sum(agent) > 21:
                print(f"Computer's final hand: {agent}, final score: {sum(agent)}")
                print("Opponent went over. You win!")
                return 1
        else:
            print(f"Computer's final hand: {agent}, Final score: {sum(agent)}")
            return 0

play_yes_no = 'y'
while play_yes_no == 'y':
    print("\n" * 20)
    print(f"{art.logo}")
    player = []
    agent = []
    init_deck()
    player_retrun = get_deal()
    if player_retrun == 0:
        agent_retrun = agent_deal()
    if sum(player)> sum(agent) and sum(player) <= 21:
        print("You Win !")
    elif sum(player)< sum(agent) and sum(agent) <= 21:
        print("You loose !")
    elif sum(player) == sum(agent):
        print("Draw")
    play_yes_no = input(f"Do you want to play a game of Blackjack? Type 'y' or 'n' :")

