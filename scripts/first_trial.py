from capacity_scenario.capacity_scenario import Scenario

capacities = {(18, 1): 10, (19, 1): 15, (19, 2): 10}
s = Scenario(capacities)

print(s._items)

for i in range(17, 23):
    key = (i, 1)
    try:
        print(f"{i}: {s[key]}")
    except KeyError:
        print(f"key <{key}> not found")
