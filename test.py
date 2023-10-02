def _split_commands(commands):
    result = []
    current_group = []
    
    for instruction in commands:
        current_group.append(instruction)
        
        if instruction.startswith('P'):
            result.append(current_group.copy())
            current_group = []
    
    # Add the remaining instructions if any
    if current_group:
        result.append(current_group)
    
    return result

# Test the function with your input
instructions = [
    "SF090", "RF090", "SB020", "LF090", "P___3", "SB010", "LB090", "SF010",
    "RF090", "P___1", "SB010", "LB090", "SB040", "LB090", "SB030", "LB090",
    "P___5", "RB090", "SF040", "P___2", "RB090", "SF020", "RB090", "SB040",
    "LB090", "SF010", "RB090", "SB010", "RB090", "SF020", "P___6", "SB030",
    "RF090", "SF030", "LB090", "SF020", "P___4"
]

split_result = _split_commands(instructions)

for group in split_result:
    print(group)

