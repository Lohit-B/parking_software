import math
from .abstractions import *

class FixedPricingRule(PricingRule):
	def calculateCost(self, time_parked_in_hours):
		return self.cost

class HourlyPricingRule(PricingRule):
	def calculateCost(self, time_parked_in_hours):
		return self.cost*math.ceil(time_parked_in_hours - self.interval[0])
	
class DailyPricingRule(PricingRule):
	def calculateCost(self, time_parked_in_hours):
		return self.cost*math.ceil((time_parked_in_hours)/24)

class DailyPricingRuleWithCarryOn(DailyPricingRule):
	def __init__(self, interval, cost, carry_on):
		super().__init__(interval, cost)
		self.carry_on = carry_on

	def calculateCost(self, time_parked_in_hours):
		return self.carry_on + self.cost*math.ceil((time_parked_in_hours - self.interval[0])/24)

class FixedPricingRuleWithCarryOn(FixedPricingRule):
	def __init__(self, interval, cost, carry_on):
		super().__init__(interval, cost)
		self.carry_on = carry_on

	def calculateCost(self, time_parked_in_hours):
		return self.carry_on + self.cost

class HourlyPricingRuleWithCarryOn(HourlyPricingRule):
	def __init__(self, interval, cost, carry_on):
		super().__init__(interval, cost)
		self.carry_on = carry_on

	def calculateCost(self, time_parked_in_hours):
		return self.carry_on + self.cost*math.ceil(time_parked_in_hours - self.interval[0])

class SmallParkingPricingRuleManager(PricingRuleManager):
	def __init__(self):
		self.store= {}
		self.store[1] = [
			HourlyPricingRule((0,math.inf), 10) 
		]

class MallParkingPricingRuleManager(PricingRuleManager):
	def __init__(self):
		self.store= {}
		self.store[1] = [
			HourlyPricingRule((0,math.inf),10) 
		]
		self.store[2] = [
			HourlyPricingRule((0,math.inf),20) 
		]
		self.store[3] = [
			HourlyPricingRule((0,math.inf),50) 
		]

class StadiumParkingPricingRuleManager(PricingRuleManager):
	def __init__(self):
		self.store= {}
		self.store[1] = [
			FixedPricingRule((0,4), 30), 
			FixedPricingRuleWithCarryOn((4,12), 60, 30), 
			HourlyPricingRuleWithCarryOn((12,math.inf), 100, 90)
		]
		self.store[2] = [
			FixedPricingRule((0,4), 60), 
			FixedPricingRuleWithCarryOn((4,12), 120, 60), 
			HourlyPricingRuleWithCarryOn((12,math.inf), 200, 180)
		]

class AirportParkingPricingRuleManager(PricingRuleManager):
	def __init__(self):
		self.store= {}
		self.store[1] = [
			FixedPricingRule((0,1), 0), 
			FixedPricingRule((1,8), 40), 
			FixedPricingRule((8,24), 60), 
			DailyPricingRule((24, math.inf), 80)
		]
		self.store[2] = [
			FixedPricingRule((0,12), 60), 
			FixedPricingRule((12,24), 80), 
			DailyPricingRule((24,math.inf), 100)
		]
		self.store[3] = [
			FixedPricingRule((0,4), 60), 
			FixedPricingRuleWithCarryOn((4,12), 120, 60), 
			FixedPricingRuleWithCarryOn((12,math.inf), 200, 180)
		]
	 
