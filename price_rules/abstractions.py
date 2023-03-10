from datetime import datetime

from abc import ABC, abstractmethod	
from exceptions import ResourceNotFoundException

class PricingRule(ABC):
	def __init__(self, interval, cost):
		self.interval = interval
		self.cost = cost

	def isRuleApplicable(self, time_parked_in_hours):
		applicable = True
		if self.interval[0] > time_parked_in_hours: applicable = False
		if self.interval[1] and self.interval[1] < time_parked_in_hours: applicable = False
		return applicable

class PricingRuleManager(ABC):
	def __init__(self):
		self.store = {}

	def getPricingRulesForVehicleCategory(self, vehicle):
		rules = self.store.get(vehicle.category.value)
		if not rules:raise ResourceNotFoundException
		return rules

	def calculateCost(self, total_hours, vehicle):
		cost = 0
		pricing_rules = self.getPricingRulesForVehicleCategory(vehicle)
		for pr in pricing_rules:
			if pr.isRuleApplicable(total_hours):
				cost = pr.calculateCost(total_hours)
				break
		else:
			raise PricingRulesNotApplicableException()

		return cost

