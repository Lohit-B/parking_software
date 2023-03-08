from datetime import datetime, timedelta
from uuid import uuid4
import math

from .abstractions import *

class ParkingTicket(Ticket):
	def __init__(self, slot, in_time):
		self.id = uuid4()
		self.slot = slot
		self.in_time = in_time
		self.exit_time = None
		self.cost = None

	def setExitTime(self, exit_time):
		self.exit_time = exit_time

	def setCost(self, cost):
		self.cost = cost

	def getCost(self):
		return self.cost

	def getSlot(self):
		return self.slot
	
	def setSlot(self, slot):
		self.slot = slot

class ParkingTicketStorage(TicketStorage):
	def __init__(self):
		self.tickets = {}

	def addTicket(self, ticket):
		self.tickets[str(ticket.id)] = ticket

	def getTicket(self, ticket_id):
		return self.tickets.get(str(ticket_id))

class ParkingTicketManager(TicketManager):
	def __init__(self):
		self.ticket_storage = ParkingTicketStorage()

	def generateTicket(self, parking_slot, in_time=datetime.now()):
		ticket = ParkingTicket(parking_slot, in_time)
		self.ticket_storage.addTicket(ticket)
		return ticket
	
	def fetchTicket(self, ticket_id):
		ticket = self.ticket_storage.getTicket(ticket_id)
		if not ticket: raise InvalidTicketIdException()
		return ticket

	def printTicket(self, ticket):
		date_format =  "%d-%b-%Y %H:%M:%S"
		data =  {
			'id':str(ticket.id),
			'spot':ticket.slot.number,
			'entry_time':datetime.strftime(ticket.in_time, date_format),
		}

		if ticket.exit_time:
			data['exit_time'] = datetime.strftime(ticket.exit_time, date_format)
		if ticket.cost != None:
			data['cost'] = ticket.cost

		return data

	def getTotalHours(self, ticket):
		total_hours = round(((ticket.exit_time - ticket.in_time).total_seconds())/60/60,2)
		return total_hours

