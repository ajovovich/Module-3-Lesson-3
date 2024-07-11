#Task 1:Flight Route Comparison 

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

shared_destinations = our_routes.intersection(competitor_routes)
print("Both airlines fly to:", shared_destinations)

our_unique_destinations = our_routes.difference(competitor_routes)
print("Destinations unique to our airline are:", our_unique_destinations)

overall_unique_destinations = our_routes.symmetric_difference(competitor_routes)
print(overall_unique_destinations)

