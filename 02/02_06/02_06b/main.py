# Tuples are immutable array-like structures

coordinates = (10, 15, 5)
print(coordinates[0])
print(coordinates[1])
print(coordinates[2])

def calculate_square_properties(side_len):
  perimeter = side_len * 4
  area = pow(side_len, 2)
  return (perimeter, area)

result = calculate_square_properties(5)
print('Perimeter:', result[0])
print('Area:', result[1])