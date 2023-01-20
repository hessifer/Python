class Physics:
    @staticmethod
    def calculate_net_force(mass, acceleration):
        if mass < 0 or acceleration < 0:
            return 0.0
        try:
            result = mass * acceleration
        except Exception:
            return 0.0
        return result

    @staticmethod
    def calculate_acceleration(mass, net_force):
        if mass < 0 or net_force < 0:
            return 0.0
        try:
            result = net_force / mass
        except ZeroDivisionError:
            return 0.0
        except Exception:
            return 0.0
        return result

    @staticmethod
    def calculate_mass(net_force, acceleration):
        if net_force < 0 or acceleration < 0:
            return 0.0
        try:
            result = net_force / acceleration
        except ZeroDivisionError:
            return 0.0
        except Exception:
            return 0.0
        return result
