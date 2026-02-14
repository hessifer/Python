"""Pytest tests for AutomobileClass.Automobile."""

import pytest
from AutomobileClass import Automobile

@pytest.fixture
def car():
    return Automobile("Toyota", "Camry", 2023)

@pytest.fixture
def car_with_partial_tank():
    return Automobile("Toyota", "Camry", 2023, fuel_capacity=15.0, fuel_level=5.0)

@pytest.fixture
def car_with_full_tank():
    return Automobile("Toyota", "Camry", 2023, fuel_capacity=15.0, fuel_level=15.0)

@pytest.fixture
def car_with_negative_mileage():
    return Automobile("Toyota", "Camry", 2023, mileage=-100.0)

@pytest.fixture
def car_with_positive_mileage():
    return Automobile("Toyota", "Camry", 2023, mileage=100.0)

class TestAutomobileInit:
    """Tests for Automobile.__init__ and default attributes."""

    def test_init_required_args(self):
        """Required make, model, year are set correctly."""
        car = Automobile("Toyota", "Camry", 2023)
        assert car.make == "Toyota"
        assert car.model == "Camry"
        assert car.year == 2023

    def test_init_defaults(self):
        """Default optional attributes match spec."""
        car = Automobile("Honda", "Civic", 2022)
        assert car.color == "white"
        assert car.vin == ""
        assert car.mileage == 0.0
        assert car.fuel_capacity == 0.0
        assert car.fuel_level == 0.0
        assert car.doors == 4
        assert car.transmission == "automatic"
        assert car.fuel_type == "gasoline"
        assert car.is_engine_running is False

    def test_init_custom_args(self):
        """Custom optional attributes are stored correctly."""
        car = Automobile(
            "Ford", "Mustang", 2024,
            color="red",
            vin="1HGBH41JXMN109186",
            mileage=15000.5,
            fuel_capacity=16.0,
            fuel_level=8.0,
            doors=2,
            transmission="manual",
            fuel_type="gasoline",
        )
        assert car.color == "red"
        assert car.vin == "1HGBH41JXMN109186"
        assert car.mileage == 15000.5
        assert car.fuel_capacity == 16.0
        assert car.fuel_level == 8.0
        assert car.doors == 2
        assert car.transmission == "manual"
        assert car.fuel_type == "gasoline"


class TestEngine:
    """Tests for start_engine, stop_engine, and is_engine_running."""

    def test_start_engine_returns_true_when_off(self, car):
        """Starting when off returns True and engine is running."""
        assert car.start_engine() is True
        assert car.is_engine_running is True

    def test_start_engine_returns_false_when_already_running(self, car):
        """Starting when already running returns False."""
        car.start_engine()
        assert car.start_engine() is False
        assert car.is_engine_running is True

    def test_stop_engine_returns_true_when_running(self, car):
        """Stopping when running returns True and engine is off."""
        car.start_engine()
        assert car.stop_engine() is True
        assert car.is_engine_running is False

    def test_stop_engine_returns_false_when_already_off(self, car):
        """Stopping when already off returns False."""
        assert car.stop_engine() is False
        assert car.is_engine_running is False

    def test_start_stop_cycle(self, car):
        """Multiple start/stop cycles behave correctly."""
        assert car.start_engine() is True
        assert car.stop_engine() is True
        assert car.start_engine() is True
        assert car.start_engine() is False
        assert car.stop_engine() is True
        assert car.stop_engine() is False


class TestRefuel:
    """Tests for refuel()."""

    def test_refuel_adds_up_to_capacity(self, car_with_partial_tank):
        """Refuel adds only up to capacity and returns amount added."""
        added = car_with_partial_tank.refuel(20.0)
        assert added == 10.0
        assert car_with_partial_tank.fuel_level == 15.0

    def test_refuel_partial_adds_correctly(self, car_with_partial_tank):
        """Refuel with less than space adds that amount."""
        added = car_with_partial_tank.refuel(3.0)
        assert added == 3.0
        assert car_with_partial_tank.fuel_level == 8.0

    def test_refuel_zero_adds_nothing(self, car_with_partial_tank):
        """Refuel with 0 adds 0."""
        added = car_with_partial_tank.refuel(0)
        assert added == 0.0
        assert car_with_partial_tank.fuel_level == 5.0

    def test_refuel_negative_adds_nothing(self, car_with_partial_tank):
        """Refuel with negative amount adds 0 (capped by max(0, space))."""
        added = car_with_partial_tank.refuel(-5.0)
        assert added == 0.0
        assert car_with_partial_tank.fuel_level == 5.0

    def test_refuel_full_tank_returns_zero(self, car_with_full_tank):
        """When tank is full, refuel returns 0."""
        added = car_with_full_tank.refuel(10.0)
        assert added == 0.0
        assert car_with_full_tank.fuel_level == 15.0


class TestAddMileage:
    """Tests for add_mileage()."""

    def test_add_mileage_positive(self, car_with_positive_mileage):
        """Positive miles are added to mileage."""
        car_with_positive_mileage.add_mileage(500.5)
        assert car_with_positive_mileage.mileage == 600.5

    def test_add_mileage_zero(self, car_with_positive_mileage):
        """Adding 0 leaves mileage unchanged."""
        car_with_positive_mileage.add_mileage(0)
        assert car_with_positive_mileage.mileage == 100.0

    def test_add_mileage_negative_ignored(self, car_with_positive_mileage):
        """Negative miles do not change mileage."""
        car_with_positive_mileage.add_mileage(-100.0)
        assert car_with_positive_mileage.mileage == 100.0


class TestStringRepresentations:
    """Tests for get_info(), __str__, and __repr__."""

    def test_get_info_format(self):
        """get_info returns year make model (color, transmission, fuel_type)."""
        car = Automobile("Toyota", "Camry", 2023, color="blue", transmission="manual", fuel_type="hybrid")
        info = car.get_info()
        assert "2023" in info
        assert "Toyota" in info
        assert "Camry" in info
        assert "blue" in info
        assert "manual" in info
        assert "hybrid" in info

    def test_str_equals_get_info(self):
        """str(automobile) equals get_info()."""
        car = Automobile("Honda", "Civic", 2022)
        assert str(car) == car.get_info()

    def test_repr_contains_make_model_year_mileage(self):
        """repr() contains make, model, year, mileage for debugging."""
        car = Automobile("Ford", "F-150", 2021, mileage=45000.0)
        r = repr(car)
        assert "Automobile(" in r
        assert "Ford" in r
        assert "F-150" in r
        assert "2021" in r
        assert "45000" in r
