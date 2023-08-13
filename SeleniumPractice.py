data = """7:15 am–10:33 amDeltanonstop3h 18mBOS-MCO
7:00 am–10:09 amDeltanonstop3h 09mMCO-BOS
9:40 am–12:56 pmFrontiernonstop3h 16mBOS-MCO
5:40 am–8:40 amFrontiernonstop3h 00mMCO-BOS"""

def format_flight_info(info):
    departure_time = info[:7]
    arrival_time = info[7:14]
    airline = info[14:22]
    duration = info[22:30]
    route = info[30:]

    return f"Departure: {departure_time} | Arrival: {arrival_time} | Airline: {airline} | Duration: {duration} | Route: {route}"

lines = data.split('\n')
formatted_data = [format_flight_info(line) for line in lines]

for flight_info in formatted_data:
    print(flight_info)
