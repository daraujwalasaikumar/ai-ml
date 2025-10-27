# Knowledge base: rules and facts
rules = {
    "Ukraine-Russia war": ["political tension", "territorial dispute"],
    "territorial dispute": ["Crimea conflict"],
    "political tension": ["NATO expansion", "sanctions"],
}

# Known facts
known_facts = {"Crimea conflict", "NATO expansion", "sanctions"}

def backward_chaining(goal, rules, known_facts):
    # If the goal is already known, we can stop
    if goal in known_facts:
        return True

    # If there are no rules to infer this goal, fail
    if goal not in rules:
        return False

    # Check each condition required to prove the goal
    for condition in rules[goal]:
        if condition not in known_facts:
            # Try to infer this condition recursively
            if not backward_chaining(condition, rules, known_facts):
                return False

    # If all conditions are satisfied, we can infer the goal
    known_facts.add(goal)
    return True


# Run backward chaining for the goal
goal = "Ukraine-Russia war"
result = backward_chaining(goal, rules, known_facts)

if result:
    print("The cause of Ukraine-Russia war is inferred from known facts.")
else:
    print("The cause of Ukraine-Russia war could not be inferred.")
