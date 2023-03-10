from datetime import datetime, timedelta
from uuid import uuid4
import math
from enum import Enum
from exceptions import InvalidVehicleCategoryException 
from kv_store.kv_store import KVStore

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

class ParkingSlotStorage(SlotStorage):
	def __init__(self, kv_store):
		self.store = kv_store

	def getAllSlots(self, vehicle_category_val):
		return self.store.getValue(vehicle_category_val)

class AirportParkingSlotManager(SlotManager):
	def __init__(self):
		self.store = ParkingSlotStorage(getAirportParkingSlotKVStore())

class StadiumParkingSlotManager(SlotManager):
	def __init__(self):
		self.store = ParkingSlotStorage(getStadiumParkingSlotKVStore())

class MallParkingSlotManager(SlotManager):
	def __init__(self):
		self.store = ParkingSlotStorage(getMallParkingSlotKVStore())

class SmallParkingSlotManager(SlotManager):
	def __init__(self):
		self.store = ParkingSlotStorage(getSmallParkingSlotKVStore())

def getAirportParkingSlotKVStore():
	store = KVStore()
	store.putValue(VehicleCategory.LIGHT.value, [ParkingSlot(i) for i in range(200)])
	store.putValue(VehicleCategory.MID.value, [ParkingSlot(i) for i in range(500)])
	store.putValue(VehicleCategory.HEAVY.value,  [ParkingSlot(i) for i in range(100)])
	return store

def getStadiumParkingSlotKVStore():
	store = KVStore()
	store.putValue(VehicleCategory.LIGHT.value, [ParkingSlot(i) for i in range(1000)])
	store.putValue(VehicleCategory.MID.value, [ParkingSlot(i) for i in range(1500)])
	return store

def getMallParkingSlotKVStore():
	store = KVStore()
	store.putValue(VehicleCategory.LIGHT.value, [ParkingSlot(i) for i in range(100)])
	store.putValue(VehicleCategory.MID.value, [ParkingSlot(i) for i in range(80)])
	store.putValue(VehicleCategory.HEAVY.value, [ParkingSlot(i) for i in range(10)])
	return store

def getSmallParkingSlotKVStore():
	store = KVStore()
	store.putValue(VehicleCategory.LIGHT.value, [ParkingSlot(i) for i in range(2)])
	return store

