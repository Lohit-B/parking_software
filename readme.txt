How to run:
	python3 runner_test.py


Folder Structure:
- Each Folder contains interfaces/abstraction and the implementations
- ParkinglotFactory provides software implementation for different type of locations (Airport, Stadium)
- runner_test implements all the test cases for different parking lots.
- Exceptions are used to send specific fail response to end users.

Solution:
- The given problem has 4 section solutions
1. Ticket Management - (Ticket Generation, TicketPrinting)
2. Price Management - (Price Mapping to vehicle category, Price based on parking hours, cost calculation)
3. Parking spot management - (Adding vehicle to spot, Freeing spot)
4. Vehicle Category Management - (Vehicles are divided into 3 categories)

- ParkinglotImpl is the main interface for the software which provides 2 functions: park and unpark
- To get an specific parkinglot software, you can query ParkinglotFactory.
- You can configure the ParkingLot software by setting different price schemes and spot distributions in ParkingLotFactory.
- At the time of initialization, number of spots for vehicles and price rules are mapped for different parking lots such as Airport,


Storage:
Currently all the data is stored in memory.

Further Improvements:
- Currently Parking spot and pricing configuration is hard coded but it can be fetched from a json file or database during initialization. 
- Currently all the data is stored in memory, which implies that each run starts fresh.


