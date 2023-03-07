
class BaseException(Exception):
	def __init__(self, message):
		self.message = message

class NoParkingSlotAvailableException(BaseException):
	pass

class ParkingNotAvailableException(Exception):
	pass

class InvalidTicketIdException(Exception):
	pass

class PricingRulesNotApplicableException(Exception):
	pass
