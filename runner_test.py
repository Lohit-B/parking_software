from parkinglot_factory import ParkingLotFactory, Vehicle
if __name__=='__main__':
	parking_lot = ParkingLotFactory().getParkingLot('AIRPORT')
	vehicle = Vehicle(1, 'Scooter')
	ticket = parking_lot.park(vehicle)
	assert ticket != None
	
	

