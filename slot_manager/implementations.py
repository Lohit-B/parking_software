from datetime import datetime, timedelta
from uuid import uuid4
import math

VEHICLE_CATEGORY = {1:'LIGHT', 2:'MID', 3:'HEAVY'}

from exceptions import InvalidVehicleCategoryException 

from .abstractions import *

class Vehicle():
	def __init__(self, category, title):
		if not VEHICLE_CATEGORY.get(category):raise InvalidVehicleCategoryException('Invalid Vehicle Number')
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
		self.store[1] = [ParkingSlot(i) for i in range(200)]
		self.store[2] = [ParkingSlot(i) for i in range(500)]
		self.store[3] = [ParkingSlot(i) for i in range(100)]

class StadiumParkingSlotManager(SlotManager):
	def __init__(self):
		self.store = {}
		self.store[1] = [ParkingSlot(i) for i in range(1000)]
		self.store[2] = [ParkingSlot(i) for i in range(1500)]

class MallParkingSlotManager(SlotManager):
	def __init__(self):
		self.store = {}
		self.store[1] = [ParkingSlot(i) for i in range(100)]
		self.store[2] = [ParkingSlot(i) for i in range(80)]
		self.store[3] = [ParkingSlot(i) for i in range(10)]

class SmallParkingSlotManager(SlotManager):
	def __init__(self):
		self.store = {}
		self.store[1] = [ParkingSlot(i) for i in range(2)]

