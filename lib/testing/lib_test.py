#!/usr/bin/env python3

import pytest
from car import Car
from vehicle import Vehicle

class TestVehicle:
    '''Class "Vehicle" in vehicle.py'''

    @pytest.fixture
    def my_vehicle(self):
        return Vehicle(48, 4)

    def test_is_class(self):
        '''is really a class.'''
        assert(object in Vehicle.__bases__)

    def test_has_wheel_size(self, my_vehicle):
        '''instantiates with attribute "wheel_size".'''
        assert my_vehicle.wheel_size == 48

    def test_has_wheel_number(self, my_vehicle):
        '''instantiates with attribute "wheel_number".'''
        assert my_vehicle.wheel_number == 4

    def test_goes_vroom(self, my_vehicle):
        '''has a method "go()" that goes "vrrrrrrrooom!"'''
        assert my_vehicle.go() == "vrrrrrrrooom!"

    def test_fills_tank(self, my_vehicle):
        '''has a method "fill_up_tank" that returns "filling up!"'''
        assert my_vehicle.fill_up_tank() == "filling up!"

class TestCar:
    '''Class "Car" in car.py'''

    @pytest.fixture
    def my_car(self):
        return Car(36, 4)

    def test_is_subclass(self):
        '''is really a subclass of Vehicle.'''
        assert(Vehicle in Car.__bases__)

    def test_has_wheel_size(self, my_car):
        '''instantiates with attribute "wheel_size".'''
        assert my_car.wheel_size == 36

    def test_has_wheel_number(self, my_car):
        '''instantiates with attribute "wheel_number".'''
        assert my_car.wheel_number == 4

    def test_goes_vroom(self, my_car):
        '''has a method "go()" that goes "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"'''
        assert my_car.go() == "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"

    def test_fills_tank(self, my_car):
        '''has a method "fill_up_tank" that returns "filling up!"'''
        assert my_car.fill_up_tank() == "filling up!"
