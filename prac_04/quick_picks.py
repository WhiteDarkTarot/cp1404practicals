import random

NUM_QUICK_PICKS = 5
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6


def generate_quick_picks(num_picks):
    quick_picks = []
    for _ in range(num_picks):
        quick_pick = random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUMBERS_PER_PICK)
        quick_pick.sort()
        quick_picks.append(quick_pick)
    return quick_picks


def display_quick_picks(quick_picks):
    for i, quick_pick in enumerate(quick_picks, start=1):
        print(" ".join(f"{num:2}" for num in quick_pick))


def main():
    num_quick_picks = int(input("How many quick picks? "))
    quick_picks = generate_quick_picks(num_quick_picks)
    display_quick_picks(quick_picks)


if __name__ == "__main__":
    main()
