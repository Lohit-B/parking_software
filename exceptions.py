
class BaseException(Exception):
	def __init__(self, message=None):
		self.message = message

class NoParkingSlotAvailableException(BaseException):
	pass

class ParkingNotAvailableException(BaseException):
	pass

class InvalidTicketIdException(BaseException):
	pass

class PricingRulesNotApplicableException(BaseException):
	pass

class InvalidVehicleCategoryException(BaseException):
	pass

class InvalidParkingLotCategoryException(BaseException):
	pass
