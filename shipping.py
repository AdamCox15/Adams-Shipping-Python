weight = 41.5
premium_ground = 125.00
# Ground Shipping
if weight <= 2:
  ground_cost = weight * 1.5 + 20
elif weight >= 3 and weight <= 6:
  ground_cost = weight * 3 + 20
elif weight >= 7 and weight <= 10:
  ground_cost = weight * 4 + 20
elif weight > 10:
  ground_cost = weight * 4.75 + 20
else:
  print('error')

# Drone Shipping
if weight <= 2:
  drone_cost = weight * 4.5 
elif weight >= 3 and weight <= 6:
  drone_cost = weight * 9
elif weight >= 7 and weight <= 10:
  drone_cost = weight * 12
elif weight > 10:
  drone_cost = weight * 14.25

print("Cost of premium ground shipping: $", premium_ground)

print(ground_cost)

print(drone_cost)
