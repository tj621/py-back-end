class Control:
    '''the object of tri-state actuators and bi-state'''

    def __init__(self):
        self.__roof_vent_south = "off"
        self.__roof_vent_north = "off"
        self.__side_vent = "off"
        self.__shade_screen_out = "off"
        self.__shade_screen_in = "off"
        self.__thermal_screen = "off"
        self.__cooling_pad = "off"
        self.__fogging = "off"
        self.__heating = "off"
        self.__co2 = "off"
        self.__lighting_1 = "off"
        self.__lighting_2 = "off"
        self.__irrigation = "off"

    def get_roof_vent_south(self):
        return self.__roof_vent_south

    def get_roof_vent_north(self):
        return self.__roof_vent_north

    def get_side_vent(self):
        return self.__side_vent

    def get_shade_screen_out(self):
        return self.__shade_screen_out

    def get_shade_screen_in(self):
        return self.__shade_screen_in

    def get_thermal_screen(self):
        return self.__thermal_screen

    def get_cooling_pad(self):
        return self.__cooling_pad

    def get_fogging(self):
        return self.__fogging

    def get_heating(self):
        return self.__heating

    def get_co2(self):
        return self.__co2

    def get_lighting_1(self):
        return self.__lighting_1

    def get_lighting_2(self):
        return self.__lighting_2

    def get_irrigation(self):
        return self.__irrigation

    def set_roof_vent_south(self, value):
        self.__roof_vent_south = value

    def set_roof_vent_north(self, value):
        self.__roof_vent_north = value

    def set_side_vent(self, value):
        self.__side_vent = value

    def set_shade_screen_out(self, value):
        self.__shade_screen_out = value

    def set_shade_screen_in(self, value):
        self.__shade_screen_in = value

    def set_thermal_screen(self, value):
        self.__thermal_screen = value

    def set_cooling_pad(self, value):
        self.__cooling_pad = value

    def set_fogging(self, value):
        self.__fogging = value

    def set_heating(self, value):
        self.__heating = value

    def set_co2(self, value):
        self.__co2 = value

    def set_lighting_1(self, value):
        self.__lighting_1 = value

    def set_lighting_2(self, value):
        self.__lighting_2 = value

    def set_irrigation(self, value):
        self.__irrigation = value
