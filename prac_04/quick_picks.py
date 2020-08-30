import random

RANDOM_PICKS = []

quick_picks = int(input("How many quick picks? "))
picks_list = []
for pick in range(quick_picks):
    for number in range(0, 6):
        random_number = random.randint(1, 46)
        if random_number in RANDOM_PICKS:
            random_number = random.randint(1, 46)
            RANDOM_PICKS.append(random_number)
        else:
            RANDOM_PICKS.append(random_number)
    RANDOM_PICKS.sort()
    print(RANDOM_PICKS)
    RANDOM_PICKS.clear()
