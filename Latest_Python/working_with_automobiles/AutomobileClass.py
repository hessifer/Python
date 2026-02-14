"""Base automobile class with common attributes and methods."""


class Automobile:
    """Base class representing a generic automobile."""

    def __init__(
        self,
        make: str,
        model: str,
        year: int,
        color: str = "white",
        vin: str = "",
        mileage: float = 0.0,
        fuel_capacity: float = 0.0,
        fuel_level: float = 0.0,
        doors: int = 4,
        transmission: str = "automatic",
        fuel_type: str = "gasoline",
    ) -> None:
        """Initialize automobile with common attributes."""
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.vin = vin
        self.mileage = mileage
        self.fuel_capacity = fuel_capacity
        self.fuel_level = fuel_level
        self.doors = doors
        self.transmission = transmission
        self.fuel_type = fuel_type
        self._engine_running = False

    def start_engine(self) -> bool:
        """Start the engine. Returns True if started, False if already running."""
        if self._engine_running:
            return False
        self._engine_running = True
        return True

    def stop_engine(self) -> bool:
        """Stop the engine. Returns True if stopped, False if already off."""
        if not self._engine_running:
            return False
        self._engine_running = False
        return True

    @property
    def is_engine_running(self) -> bool:
        """Return whether the engine is currently running."""
        return self._engine_running

    def refuel(self, amount: float) -> float:
        """
        Add fuel. Returns the amount actually added (capped by capacity).
        Negative amounts add nothing and return 0.
        """
        if amount <= 0:
            return 0.0
        space = self.fuel_capacity - self.fuel_level
        added = min(amount, max(0, space))
        self.fuel_level += added
        return added

    def add_mileage(self, miles: float) -> None:
        """Update the odometer by the given number of miles."""
        if miles >= 0:
            self.mileage += miles

    def get_info(self) -> str:
        """Return a string summary of the automobile."""
        return (
            f"{self.year} {self.make} {self.model} "
            f"({self.color}, {self.transmission}, {self.fuel_type})"
        )

    def __str__(self) -> str:
        """String representation of the automobile."""
        return self.get_info()

    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return (
            f"Automobile(make={self.make!r}, model={self.model!r}, "
            f"year={self.year}, mileage={self.mileage})"
        )
