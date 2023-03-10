from parking_lot.parkinglot_factory import ParkingLotFactory
from slot_manager.implementations import Vehicle, VehicleCategory
from ticket.implementations import ParkingTicketManager
from datetime import datetime, timedelta

from exceptions import ParkingNotAvailableException, NoParkingSlotAvailableException, InvalidVehicleCategoryException, InvalidParkingLotCategoryException 

if __name__=='__main__':
	ticket_manager = ParkingTicketManager()

	print(end="\n")	
	print('==Testing SMALL Parking Lot==')
	print(end="\n")	

	parking_lot = ParkingLotFactory().getParkingLot('SMALL')

	print("Parking Scooter")
	vehicle = Vehicle(VehicleCategory.LIGHT, 'Scooter')
	ticket1 = parking_lot.park(vehicle)
	assert ticket1 != None
	print(ticket_manager.printTicket(ticket1))


	print("Parking Motorcycle")
	vehicle = Vehicle(VehicleCategory.LIGHT, 'MOTOR')
	ticket = parking_lot.park(vehicle)
	print(ticket_manager.printTicket(ticket))
	assert ticket != None


	print("Parking Motorcycle 2")
	vehicle = Vehicle(VehicleCategory.LIGHT, 'MOTOR')
	try:
		ticket = parking_lot.park(vehicle)
		assert False
	except NoParkingSlotAvailableException: 
		print('No Spot Available')
		assert True
	except Exception:
		assert False

	print("Parking Car")
	vehicle = Vehicle(VehicleCategory.MID, 'CAR')
	try:
		ticket = parking_lot.park(vehicle)
	except ParkingNotAvailableException: 
		print('This type of vehicle are not parked here')
		assert True
	except Exception:
		assert False
	
		
	print("Un-Parking scooter")
	ticket = parking_lot.unpark(ticket1.id, exit_time=datetime.now()+timedelta(hours=4))
	print(ticket_manager.printTicket(ticket))

	print("Parking MS3")
	vehicle = Vehicle(VehicleCategory.LIGHT, 'MOTOR3')
	ticket = parking_lot.park(vehicle)
	print(ticket_manager.printTicket(ticket))
	assert ticket != None

	print(end="\n")	
	print('==TESTING MALL PARKING==')
	print(end="\n")	

	mall_parking_lot = ParkingLotFactory().getParkingLot('MALL')

	print('Parking MotorCycle')
	vehicle = Vehicle(VehicleCategory.LIGHT, 'MOTOR')
	motor_ticket = mall_parking_lot.park(vehicle)
	assert motor_ticket != None
	print(ticket_manager.printTicket(motor_ticket))

	print('Parking CAR')
	vehicle = Vehicle(VehicleCategory.MID, 'CAR')
	car_ticket = mall_parking_lot.park(vehicle)
	assert car_ticket != None
	print(ticket_manager.printTicket(car_ticket))

	print('Parking BUS')
	vehicle = Vehicle(VehicleCategory.HEAVY, 'BUS')
	bus_ticket = mall_parking_lot.park(vehicle)
	assert  bus_ticket != None
	print(ticket_manager.printTicket(bus_ticket))
		
	print('Un-Parking MotorCycle')
	motor_ticket = mall_parking_lot.unpark(motor_ticket.id, exit_time=datetime.now()+timedelta(hours=3, minutes=30))
	print(ticket_manager.printTicket(motor_ticket))
	assert motor_ticket.getCost() == 40
	print('Un-Parking Car')
	car_ticket = mall_parking_lot.unpark(car_ticket.id, exit_time=datetime.now()+timedelta(hours=6, minutes=1))
	print(ticket_manager.printTicket(car_ticket))
	assert car_ticket.getCost() == 140
	print('Un-Parking Bus')
	bus_ticket= mall_parking_lot.unpark(bus_ticket.id, exit_time=datetime.now()+timedelta(hours=1, minutes=59))
	print(ticket_manager.printTicket(car_ticket))
	assert bus_ticket.getCost() == 100

	print(end="\n")	
	print('==TESTING STADIUM PARKING==')
	print(end="\n")	

	parking_lot = ParkingLotFactory().getParkingLot('STADIUM')

	print('Parking MotorCycle')
	vehicle = Vehicle(VehicleCategory.LIGHT, 'MOTOR')
	motor_ticket = parking_lot.park(vehicle)
	assert motor_ticket != None
	print(ticket_manager.printTicket(motor_ticket))

	print('Parking MotorCycle 2')
	vehicle = Vehicle(VehicleCategory.LIGHT, 'MOTOR2')
	motor_ticket2 = parking_lot.park(vehicle)
	assert motor_ticket2 != None
	print(ticket_manager.printTicket(motor_ticket2))

	print('Parking EV1')
	vehicle = Vehicle(VehicleCategory.MID, 'CAR')
	car_ticket = parking_lot.park(vehicle)
	assert car_ticket != None
	print(ticket_manager.printTicket(car_ticket))

	print('Parking EV2')
	vehicle = Vehicle(VehicleCategory.MID, 'CAR')
	car_ticket2 = parking_lot.park(vehicle)
	assert car_ticket2 != None
	print(ticket_manager.printTicket(car_ticket2))

	print('Parking BUS')
	vehicle = Vehicle(VehicleCategory.HEAVY, 'BUS')
	try:
		bus_ticket = parking_lot.park(vehicle)
		assert False
	except ParkingNotAvailableException: 
		print('This type of vehicle are not parked here')
		assert True
	except Exception:
		assert False
		
	print('Un-Parking MotorCycle 1')
	motor_ticket = parking_lot.unpark(motor_ticket.id, exit_time=datetime.now()+timedelta(hours=3, minutes=40))
	assert motor_ticket.getCost() == 30
	print(ticket_manager.printTicket(motor_ticket))

	print('Un-Parking MotorCycle 2')
	motor_ticket2 = parking_lot.unpark(motor_ticket2.id, exit_time=datetime.now()+timedelta(hours=14, minutes=59))
	assert motor_ticket2.getCost() == 390
	print(ticket_manager.printTicket(motor_ticket2))

	print('Un-Parking EV1')
	car_ticket = parking_lot.unpark(car_ticket.id, exit_time=datetime.now()+timedelta(hours=11, minutes=30))
	assert car_ticket.getCost() == 180
	print(ticket_manager.printTicket(car_ticket))

	print('Un-Parking EV2')
	car_ticket2 = parking_lot.unpark(car_ticket2.id, exit_time=datetime.now()+timedelta(hours=13, minutes=5))
	assert car_ticket2.getCost() == 580
	print(ticket_manager.printTicket(car_ticket2))

	print(end="\n")	
	print('==TESTING AIRPORT PARKING==', end='\n\n')
	parking_lot = ParkingLotFactory().getParkingLot('AIRPORT')

	print('Parking MotorCycle')
	vehicle = Vehicle(VehicleCategory.LIGHT, 'MOTOR')
	motor_ticket = parking_lot.park(vehicle)
	assert motor_ticket != None
	print(ticket_manager.printTicket(motor_ticket))

	print('Parking MotorCycle 2')
	vehicle2 = Vehicle(VehicleCategory.LIGHT, 'MOTOR')
	motor_ticket2 = parking_lot.park(vehicle2)
	assert motor_ticket2 != None
	print(ticket_manager.printTicket(motor_ticket2))

	print('Parking MotorCycle 3')
	motor_ticket3 = parking_lot.park(Vehicle(VehicleCategory.LIGHT, 'M3'))
	assert motor_ticket3 != None
	print(ticket_manager.printTicket(motor_ticket3))

	print('Parking CAR 1')
	car_ticket = parking_lot.park(Vehicle(VehicleCategory.MID, 'C1'))
	assert car_ticket != None
	print(ticket_manager.printTicket(car_ticket))

	print('Parking CAR 2')
	car_ticket2 = parking_lot.park(Vehicle(VehicleCategory.MID, 'C1'))
	assert car_ticket2 != None
	print(ticket_manager.printTicket(car_ticket2))
	print('Parking CAR 3')
	car_ticket3 = parking_lot.park(Vehicle(VehicleCategory.MID, 'C1'))
	assert car_ticket3 != None
	print(ticket_manager.printTicket(car_ticket3))

	print('Parking BUS')
	bus_ticket = parking_lot.park(Vehicle(VehicleCategory.HEAVY, 'Bus'))
	assert bus_ticket != None
	print(ticket_manager.printTicket(bus_ticket))
		
	print('Un-Parking MotorCycle 1 after 30 mins')
	motor_ticket = parking_lot.unpark(motor_ticket.id, exit_time=datetime.now()+timedelta(hours=0.5))
	assert motor_ticket.getCost() == 0
	print(ticket_manager.printTicket(motor_ticket))

	print('Un-Parking MotorCycle 2 after 14 hours')
	motor_ticket2 = parking_lot.unpark(motor_ticket2.id, exit_time=datetime.now()+timedelta(hours=14))
	assert motor_ticket2.getCost() == 60
	print(ticket_manager.printTicket(motor_ticket2))

	print('Un-Parking MotorCycle 3 after 1 day 12 hours')
	motor_ticket3 = parking_lot.unpark(motor_ticket3.id, exit_time=datetime.now()+timedelta(hours=12, days=1))
	assert motor_ticket3.getCost() == 160
	print(ticket_manager.printTicket(motor_ticket3))

	print('Un-Parking Car 1')
	car_ticket = parking_lot.unpark(car_ticket.id, exit_time=datetime.now()+timedelta(hours=0.5))
	assert car_ticket.getCost() == 60
	print(ticket_manager.printTicket(car_ticket))

	print('Un-Parking Car 2')
	car_ticket2 = parking_lot.unpark(car_ticket2.id, exit_time=datetime.now()+timedelta(hours=23))
	assert car_ticket2.getCost() == 80
	print(ticket_manager.printTicket(car_ticket2))

	print('Un-Parking Car 3')
	car_ticket3 = parking_lot.unpark(car_ticket3.id, exit_time=datetime.now()+timedelta(hours=1, days=3))
	assert car_ticket3.getCost() == 400
	print(ticket_manager.printTicket(car_ticket3))

	print('Un-Parking Bus')
	bus_ticket = parking_lot.unpark(bus_ticket.id, exit_time=datetime.now()+timedelta(hours=5))
	assert bus_ticket.getCost() == 180
	print(ticket_manager.printTicket(bus_ticket))
