"""Example script using the Automobile class from AutomobileClass."""

from AutomobileClass import Automobile


def main() -> None:
    # Create a car instance
    my_car = Automobile(
        make="Toyota",
        model="Camry",
        year=2024,
        color="silver",
        mileage=15000.0,
        fuel_capacity=15.8,
        fuel_level=12.0,
        doors=4,
        transmission="automatic",
        fuel_type="gasoline",
    )

    print("My car:", my_car.get_info())
    print()

    # Start the engine
    if my_car.start_engine():
        print("Engine started.")
    else:
        print("Engine was already running.")
    print(f"Engine running: {my_car.is_engine_running}")
    print()

    # Refuel a bit
    added = my_car.refuel(2.0)
    print(f"Refueled {added} gallons. Fuel level: {my_car.fuel_level}")
    print()

    # Simulate a short drive
    my_car.add_mileage(25.5)
    print(f"After drive: mileage = {my_car.mileage}")
    print()

    # Stop the engine
    my_car.stop_engine()
    print("Engine stopped.")
    print(f"Engine running: {my_car.is_engine_running}")
    print()

    # String representations
    print("str:", str(my_car))
    print("repr:", repr(my_car))


if __name__ == "__main__":
    main()
