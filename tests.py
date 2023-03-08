from exceptions import ParkingNotAvailableException, NoParkingSlotAvailableException, InvalidVehicleCategoryException, InvalidParkingLotCategoryException 
from abc import ABC, abstractmethod	

class BaseTestRunner(ABC):
	@abstractmethod
	def run():
		pass

class TestParkingTicket(BaseTestRunner):
	pass

class TestParkingTicketManager(BaseTestRunner):
	pass

class TestParkingSlotManager(BaseTestRunner):
	pass

class TestPricePolicy(BaseTestRunner):
	pass

class TestParkingLot(BaseTestRunner):
	pass
