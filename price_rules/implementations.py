import math
from .abstractions import *
from slot_manager.implementations import VehicleCategory
from kv_store.kv_store import KVStore

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

class PricingRuleStorage(RuleStorage):
	def __init__(self, kv_store):
		self.store = kv_store
	
	def getPricingRule(self, vehicle_category_val):
		return self.store.getValue(vehicle_category_val)

class SmallParkingPricingRuleManager(PricingRuleManager):
	def __init__(self):
		self.store = PricingRuleStorage(getKVStoreForSmallParking())

class MallParkingPricingRuleManager(PricingRuleManager):
	def __init__(self):
		self.store = PricingRuleStorage(getKVStoreForMallParking())

class StadiumParkingPricingRuleManager(PricingRuleManager):
	def __init__(self):
		self.store = PricingRuleStorage(getKVStoreForStadiumParking())

class AirportParkingPricingRuleManager(PricingRuleManager):
	def __init__(self):
		self.store = PricingRuleStorage(getKVStoreForAirportParking())
	 

#can be changed to a store with all the different parking types.
def getKVStoreForSmallParking():
	kv_store = KVStore() 
	kv_store.putValue(VehicleCategory.LIGHT.value, [
		HourlyPricingRule((0,math.inf), 10) 
	])
	return kv_store

def getKVStoreForMallParking():
	kv_store = KVStore() 
	kv_store.putValue(VehicleCategory.LIGHT.value, [
		HourlyPricingRule((0,math.inf),10) 
	])
	kv_store.putValue(VehicleCategory.MID.value,[
		HourlyPricingRule((0,math.inf),20) 
	])
	kv_store.putValue(VehicleCategory.HEAVY.value,[
		HourlyPricingRule((0,math.inf),50) 
	])
	return kv_store

def getKVStoreForStadiumParking():
	kv_store = KVStore() 
	kv_store.putValue(VehicleCategory.LIGHT.value, [
		FixedPricingRule((0,4), 30), 
		FixedPricingRuleWithCarryOn((4,12), 60, 30), 
		HourlyPricingRuleWithCarryOn((12,math.inf), 100, 90)
	])
	kv_store.putValue(VehicleCategory.MID.value, [
		FixedPricingRule((0,4), 60), 
		FixedPricingRuleWithCarryOn((4,12), 120, 60), 
		HourlyPricingRuleWithCarryOn((12,math.inf), 200, 180)
	])
	return kv_store

def getKVStoreForAirportParking():
	kv_store = KVStore() 
	kv_store.putValue(VehicleCategory.LIGHT.value, [
		FixedPricingRule((0,1), 0), 
		FixedPricingRule((1,8), 40), 
		FixedPricingRule((8,24), 60), 
		DailyPricingRule((24, math.inf), 80)
	])
	kv_store.putValue(VehicleCategory.MID.value, [
		FixedPricingRule((0,12), 60), 
		FixedPricingRule((12,24), 80), 
		DailyPricingRule((24,math.inf), 100)
	])
	kv_store.putValue(VehicleCategory.HEAVY.value, [
		FixedPricingRule((0,4), 60), 
		FixedPricingRuleWithCarryOn((4,12), 120, 60), 
		FixedPricingRuleWithCarryOn((12,math.inf), 200, 180)
	])
	return kv_store
