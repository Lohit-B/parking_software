import json
from datetime import datetime

from abc import ABC, abstractmethod	
import uuid4

from exceptions import ParkingNotAvailableException, NoParkingSlotAvailableException 

class Ticket():
	def __init__(self, slot, in_time):
		self.id = uuid4()
		self.slot = slot
		self.in_time = in_time

	def setExitTime(self, exit_time):
		self.exit_time = exit_time

	def setCost(self, cost):
		self.cost = cost

	def print(self):
		data =  {
			'id':self.id,
			'spot':self.slot.number,
			'entry':self.in_time,
		}

		if self.exit_time:
			data['exit_time'] = self.exit_time
	
class Vehicle():
	def __init__(self, title, category):
		self.title = title
		self.category = category

class ParkingSlot()
	def __init__(self, number):
		self.number = nubmer

	def parkVehicle(self, vehicle)
		self.vehicle = vehicle

	def isAvailableToPark(self):
		return self.vehicle != None
		
class TicketManager(ABC):
	@abstractmethod
	def generateTicket(self)
		pass

	@abstractmethod
	def fetchTicket(self)
		pass

	@abstractmethod
	def PrintTicket(self, ticket)
		pass

	@abstractmethod
	def calculateCost(self, ticket, pricing_rules)
		pass

class ParkingTicketManager()
	def __init__(self):
		self.tickets = {}

	def generateTicket(self, parking_slot):
		ticket = Ticket()
		self.tickets[ticket.id] = ticket
	
	def fetchTicket(self, ticket_id):
		ticket = self.tickets.get(ticket.id)
		if not ticket: raise InvalidTicketIdException()
		return ticket

	def printTicket(self, ticket):
		return ticket.print()

	def calculateCost(self, ticket, pricing_rules):
		total_hours = (timedelta(ticket.exit_time - ticket.in_time).total_seconds())/60/60
		cost = 0
		for pr in pricing_rules:
			if pr.isRuleApplicable(total_hours):
				cost = pr.calculateCost(total_hours)
				break
		else:
			raise PricingRulesNotApplicableException()

		ticket.setCost(cost)

class PricingRuleABC():
	MODE = {'H':'hourly', 'D':'daily', 'F':'fixed'}
	def isRuleApplicable(self, time_parked_in_hours):
		pass

	def calculateCost(self, time_parked_in_hours):
		pass


class PricingRule(PricingRuleABC):
	def __init__(self, interval, mode, charge, carry_on=0):
		self.interval = interval
		self.mode = mode 
		self.charge = charge
		self.carry_on = carry_on

	def isRuleApplicable(self, time_parked_in_hours):
		applicable = True
		if self.interval[0] > time_parked_in_hours: applicable = False
		if self.interval[1] and self.interval[1] < time_parked_in_hours: applicable = False
		return applicable

	def calculateCost(self, time_parked_in_hours):
		if self.mode == self.MODE['F']:return self.charge + self.carry_on
		if self.mode == self.MODE['H']:return self.carry_on + cost*(time_parked_in_hours - self.interval[0])
		if self.mode == self.MODE['D']:return self.carry_on + cost*Math.ceil(time_parked_in_hours - self.interval[0])
	
class ParkingLot(ABC):
	def __init__(self):
		self.ticket_manager = TicketManager()
		self.slots = {}
		self.pricing_rules = {}

	def park(self, vehicle, in_time=datetime.now()):
		applicable_slots = self.slots.get(vehicle.category)
		if not applicable_slots: raise ParkingNotAvailableException()
		available_slot = self._findFreeSlot(applicable_slots)
		if not available_slot: raise NoParkingSlotAvailableException()

		available_slot.parkVehicle(vehicle)

		ticket = self.ticket_manager.generateTicket(available_slot)
		return self.ticket_manager.printTicket(ticket)

		
	def _findFreeSlot(self, applicable_slots):
		for slot in applicable_slots:
			if slot.isAvailableToPark(): return slot
		return None

	def unpark(self, ticket_id):
		ticket = self.ticket_manager.fetchTicket(ticket_id)

		ticket.setExitTime(datetime.now())
		self.ticket_manager.calculateCost(ticket, self.pricingRules)
		return self.ticket_manager.printTicket(ticket)

class SmallParkingLot(ParkingLot):
	def __init__(self, vehicle):
		self.ticket_manager = ParkingTicketManager()

		self.slots = {}
		self.slots[1] = [ParkingSlot() for _ in range(2)]

		self.pricing_rules = {}
		self.pricing_rules[1] = [
			PricingRule((0,), PricingRule.MODE['H'], 10) 
		]

class MallParkingLot(ParkingLot):
	def __init__(self, vehicle):
		self.ticket_manager = ParkingTicketManager()
		self.slots = {}
		self.slots[1] = [ParkingSlot() for _ in range(100)]
		self.slots[2] = [ParkingSlot() for _ in range(80)]
		self.slots[3] = [ParkingSlot() for _ in range(10)]

		self.pricing_rules = {}
		self.pricing_rules[1] = [
			PricingRule((0,), PricingRule.MODE['H'],10) 
		]
		self.pricing_rules[2] = [
			PricingRule((0,), PricingRule.MODE['H'],20) 
		]
		self.pricing_rules[3] = [
			PricingRule((0,), PricingRule.MODE['H'],50) 
		]

class StadiumParkingLot(ParkingLot):
	def __init__(self, vehicle):
		self.ticket_manager = ParkingTicketManager()

		self.slots = {}
		self.slots[1] = [ParkingSlot() for _ in range(1000)]
		self.slots[2] = [ParkingSlot() for _ in range(1500)]

		self.pricing_rules = {}
		self.pricing_rules[1] = [
			PricingRule((0,4), PricingRule.MODE['F'], 30, 0), 
			PricingRule((4,12), PricingRule.MODE['F'], 60, 30), 
			PricingRule((12,), PricingRule.MODE['H'], 100, 90)
		]
		self.pricing_rules[2] = [
			PricingRule((0,4), PricingRule.MODE['F'], 60, 0), 
			PricingRule((4,12), PricingRule.MODE['F'], 120, 60), 
			PricingRule((12,), PricingRule.MODE['H'], 200, 180)
		]

class AirportParkingLot(ParkingLot):
	def __init__(self, vehicle):
		self.ticket_manager = ParkingTicketManager()

		self.slots = {}
		self.slots[1] = [ParkingSlot() for _ in range(200)]
		self.slots[2] = [ParkingSlot() for _ in range(500)]
		self.slots[3] = [ParkingSlot() for _ in range(100)]

		self.pricing_rules = {}
		self.pricing_rules[1] = [
			PricingRule((0,1), PricingRule.MODE['F'], 0), 
			PricingRule((1,8), PricingRule.MODE['F'], 40), 
			PricingRule((8,24), PricingRule.MODE['F'], 60), 
			PricingRule((24,), PricingRule.MODE['D'], 80)
		]
		self.pricing_rules[2] = [
			PricingRule((0,12), PricingRule.MODE['F'], 60), 
			PricingRule((12,24), PricingRule.MODE['F'], 80), 
			PricingRule((24,), PricingRule.MODE['D'], 100)
		]


class ParkingLotFactory():
	parking_lot = None

	def getParkingLot(self, category):
		if category == 'AIRPORT':
			return AirportParkingLot()
		if category == 'MALL':
			return MallParkingLot()
		if category == 'STADIUM':
			return StadiumParkingLot()
		if category == 'SMALL':
			return SmallParkingLot()

		raise Exception('Invalid Category')
