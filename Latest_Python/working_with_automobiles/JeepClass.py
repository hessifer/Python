"""Jeep class extending Automobile with 4x4-specific features."""

from AutomobileClass import Automobile


class Jeep(Automobile):
    """Jeep vehicle with front locker capability."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._front_lockers_engaged = False

    def engage_front_lockers(self) -> bool:
        """
        Engage the front differential lockers for improved traction off-road.
        Returns True if lockers were engaged, False if already engaged.
        """
        if self._front_lockers_engaged:
            return False
        self._front_lockers_engaged = True
        return True

    def disengage_front_lockers(self) -> bool:
        """
        Disengage the front differential lockers.
        Returns True if lockers were disengaged, False if already disengaged.
        """
        if not self._front_lockers_engaged:
            return False
        self._front_lockers_engaged = False
        return True

    @property
    def are_front_lockers_engaged(self) -> bool:
        """Return whether the front lockers are currently engaged."""
        return self._front_lockers_engaged
