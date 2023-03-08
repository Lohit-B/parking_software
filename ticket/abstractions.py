from datetime import datetime

from abc import ABC, abstractmethod	
from exceptions import ParkingNotAvailableException, NoParkingSlotAvailableException, InvalidVehicleCategoryException 

class Ticket(ABC):
	@abstractmethod
	def setExitTime():
		pass
	
	@abstractmethod
	def getSlot():
		pass

class TicketStorage(ABC):
	@abstractmethod
	def addTicket(self, ticket):
		pass

	@abstractmethod
	def getTicket(self, ticket):
		pass

class TicketManager(ABC):
	@abstractmethod
	def generateTicket(self, parking_slot, in_time=datetime.now()):
		pass

	@abstractmethod
	def fetchTicket(self, ticket_id):
		pass

	@abstractmethod
	def printTicket(self, ticket):
		pass

	@abstractmethod
	def getTotalHours(self, ticket):
		pass

