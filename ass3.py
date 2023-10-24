def fractional_knapsack(weight,values,capacity):
    res=0
    # Pair : [Weight,value]
    for pair in sorted(zip(weights,values), key= lambda x: x[1]/x[0], reverse=True):
        print (pair)

        if capacity<=0: # Capacity completed - Bag fully filled 
            break 

        if pair[0]>capacity: # Current's weight with highest value/weight ratio Available Capacity
            res+=int(capacity * (pair[1]/pair[0]))  # Completely fill the bag
            capacity=0

        elif pair[0]<=capacity: # Take the whole object
            res+=pair[1]
            capacity-=pair[0]
            
    print(res)        

if __name__=="__main__":
    num_items = int(input("Enter the number of items: "))

# Initialize empty lists for weights and values
    weights = []
    values = []

# Get user input for weights and values
    for i in range(num_items):
        weight = float(input(f"Enter the weight of item {i + 1}: "))
        value = float(input(f"Enter the value of item {i + 1}: "))
        weights.append(weight)
        values.append(value)

# Get user input for the knapsack capacity
    capacity = float(input("Enter the knapsack capacity: "))
    fractional_knapsack(weight,values,capacity)
