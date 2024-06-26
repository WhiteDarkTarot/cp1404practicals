from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_cost = 0

    print("Let's drive!")
    user_choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()
    while user_choice != 'q':
        if user_choice == 'c':
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif user_choice == 'd':
            if current_taxi:
                distance_to_drive = float(input("Drive how far? "))
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_cost += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_cost:.2f}")
        user_choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()

    print(f"Total trip cost: ${total_cost:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
