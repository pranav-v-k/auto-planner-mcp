from teammates.dev_b.logic import (
    check_jis_inventory,
    calculate_station_oee,
    estimate_downtime_cost,
)

print("=" * 50)
print("Developer B Test")
print("=" * 50)

print("\n1. Inventory Check")
print(check_jis_inventory("RED_LEATHER"))

print("\n2. OEE Calculation")
print(calculate_station_oee("STATION_WELDING"))

print("\n3. Downtime Cost")
print(estimate_downtime_cost("STATION_PAINT"))