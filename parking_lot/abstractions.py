from datetime import datetime

from abc import ABC, abstractmethod	
from exceptions import ParkingNotAvailableException, NoParkingSlotAvailableException, InvalidVehicleCategoryException 

class ParkingLot(ABC):
	@abstractmethod
	def park(self, vehicle):
		pass
	
	@abstractmethod
	def unpark(self, ticket_id):
		pass

