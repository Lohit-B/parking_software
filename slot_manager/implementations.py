from datetime import datetime, timedelta
from uuid import uuid4
import math
from enum import Enum
from exceptions import InvalidVehicleCategoryException 

from .abstractions import *


class VehicleCategory(Enum):
	LIGHT = 1
	MID = 2
	HEAVY = 3

class Vehicle():
	def __init__(self, category, title):
		self.title = title
		self.category = category

class ParkingSlot(Slot):
	def __init__(self, number):
		self.number = number
		self.vehicle = None

	def setVehicle(self, vehicle):
		self.vehicle = vehicle

	def getVehicle(self):
		return self.vehicle

	def removeVehicle(self):
		self.setVehicle(None)

	def isAvailableToPark(self):
		return self.getVehicle() == None

class AirportParkingSlotManager(SlotManager):
	def __init__(self):
		self.store = {}
		self.store[VehicleCategory.LIGHT.value] = [ParkingSlot(i) for i in range(200)]
		self.store[VehicleCategory.MID.value] = [ParkingSlot(i) for i in range(500)]
		self.store[VehicleCategory.HEAVY.value] = [ParkingSlot(i) for i in range(100)]

class StadiumParkingSlotManager(SlotManager):
	def __init__(self):
		self.store = {}
		self.store[VehicleCategory.LIGHT.value] = [ParkingSlot(i) for i in range(1000)]
		self.store[VehicleCategory.MID.value] = [ParkingSlot(i) for i in range(1500)]

class MallParkingSlotManager(SlotManager):
	def __init__(self):
		self.store = {}
		self.store[VehicleCategory.LIGHT.value] = [ParkingSlot(i) for i in range(100)]
		self.store[VehicleCategory.MID.value] = [ParkingSlot(i) for i in range(80)]
		self.store[VehicleCategory.HEAVY.value] = [ParkingSlot(i) for i in range(10)]

class SmallParkingSlotManager(SlotManager):
	def __init__(self):
		self.store = {}
		self.store[VehicleCategory.LIGHT.value] = [ParkingSlot(i) for i in range(2)]

