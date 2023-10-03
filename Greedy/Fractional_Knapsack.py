def fractional_knapsack(items, capacity):
    # Calculate the value-to-weight ratios for each item
    value_per_weight = [(item[0] / item[1], item[0], item[1]) for item in items]

    # Sort the items by their value-to-weight ratios in descending order
    value_per_weight.sort(reverse=True)

    total_value = 0.0  # Initialize the total value of items in the knapsack
    knapsack = []      # Initialize the knapsack as an empty list

    for ratio, value, weight in value_per_weight:
        if capacity >= weight:
            # Add the entire item to the knapsack
            knapsack.append((value, weight))
            total_value += value
            capacity -= weight
        else:
            # Add a fraction of the item to the knapsack
            fraction = capacity / weight
            knapsack.append((fraction * value, fraction * weight))
            total_value += fraction * value
            break  # Knapsack is full

    return total_value, knapsack

# Example usage:
if __name__ == "__main__":
    items = [(60, 10), (100, 20), (120, 30)]
    capacity = 50
    max_value, knapsack_items = fractional_knapsack(items, capacity)

    print("Maximum value:", max_value)
    print("Knapsack items:", knapsack_items)
