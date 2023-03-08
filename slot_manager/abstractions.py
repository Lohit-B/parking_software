from datetime import datetime

from abc import ABC, abstractmethod	
from exceptions import ParkingNotAvailableException, NoParkingSlotAvailableException, InvalidVehicleCategoryException 

class Slot(ABC):
	@abstractmethod
	def getVehicle(self):
		pass
	
	@abstractmethod
	def setVehicle(self, vehicle):
		pass

	@abstractmethod
	def removeVehicle(self):
		pass

	@abstractmethod
	def isAvailableToPark(self):
		pass


class SlotManager(ABC):
	def __init__(self):
		self.store = {}
		
	def getParkingSlotForVehicleCategory(self, vehicle_category):
		applicable_slots = self.store.get(vehicle_category)
		if not applicable_slots: raise ParkingNotAvailableException()
		available_slot = self._findFreeSlot(applicable_slots)
		if not available_slot: raise NoParkingSlotAvailableException()
		return available_slot

	def _findFreeSlot(self, applicable_slots):
		for slot in applicable_slots:
			if slot.isAvailableToPark(): return slot
		return None



