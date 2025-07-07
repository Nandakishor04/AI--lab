# Simple dataset
dataset = [
    ['Sunny', 'No'],
    ['Rainy', 'Yes'],
    ['Sunny', 'No'],
    ['Rainy', 'Yes']
]

# Function to build simple tree
def build_simple_tree(data):
    sunny_count = sum(1 for row in data if row[0] == 'Sunny' and row[1] == 'Yes')
    rainy_count = sum(1 for row in data if row[0] == 'Rainy' and row[1] == 'Yes')

    tree = {}
    tree['Weather'] = {}
    
    # For Sunny
    if sunny_count == 0:
        tree['Weather']['Sunny'] = 'No'
    else:
        tree['Weather']['Sunny'] = 'Yes'
    
    # For Rainy
    if rainy_count == 0:
        tree['Weather']['Rainy'] = 'No'
    else:
        tree['Weather']['Rainy'] = 'Yes'

    return tree

# Build the tree
decision_tree = build_simple_tree(dataset)

# Print the tree
print(decision_tree)
