from datetime import datetime

from .abstractions import ParkingLot
from ticket.implementations import ParkingTicketManager

class ParkingLotImpl(ParkingLot):
	def __init__(self, slot_manager, price_rule_manager):
		self.ticket_manager = ParkingTicketManager()
		self.slot_manager = slot_manager
		self.price_rule_manager = price_rule_manager

	def park(self, vehicle, in_time=datetime.now()):
		available_slot = self.slot_manager.getParkingSlotForVehicleCategory(vehicle.category)
		available_slot.setVehicle(vehicle)
		ticket = self.ticket_manager.generateTicket(available_slot)
		return ticket

	def unpark(self, ticket_id, exit_time=None):
		ticket = self.ticket_manager.fetchTicket(ticket_id)
		ticket.setExitTime(exit_time or datetime.now())
		total_hours = self.ticket_manager.getTotalHours(ticket)
		vehicle = ticket.getSlot().getVehicle()
		cost = self.price_rule_manager.calculateCost(total_hours, vehicle)
		ticket.setCost(cost)
		ticket.getSlot().removeVehicle()
		return ticket

