from exceptions import InvalidParkingLotCategoryException

from parking_lot.implementations import ParkingLotImpl
from price_rules.implementations import AirportParkingPricingRuleManager, MallParkingPricingRuleManager, SmallParkingPricingRuleManager, StadiumParkingPricingRuleManager
from slot_manager.implementations import AirportParkingSlotManager, StadiumParkingSlotManager, SmallParkingSlotManager, MallParkingSlotManager 


class ParkingLotFactory():
	parking_lot = None

	def getParkingLot(self, category):
		if category == 'AIRPORT':
			slot_manager = AirportParkingSlotManager()
			pricing_rule_manager = AirportParkingPricingRuleManager()
			return ParkingLotImpl(slot_manager, pricing_rule_manager)
		if category == 'MALL':
			slot_manager = MallParkingSlotManager()
			pricing_rule_manager = MallParkingPricingRuleManager()
			return ParkingLotImpl(slot_manager, pricing_rule_manager)
		if category == 'STADIUM':
			slot_manager = StadiumParkingSlotManager()
			pricing_rule_manager = StadiumParkingPricingRuleManager()
			return ParkingLotImpl(slot_manager, pricing_rule_manager)
		if category == 'SMALL':
			slot_manager = SmallParkingSlotManager()
			pricing_rule_manager = SmallParkingPricingRuleManager()
			return ParkingLotImpl(slot_manager, pricing_rule_manager)

		raise InvalidParkingLotCategoryException('Invalid Parking Category')
