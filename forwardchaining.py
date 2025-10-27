# Knowledge base: IF symptoms THEN diagnosis
rules = {
    ("fever", "cough"): "flu",
    ("fever", "rash"): "measles",
    ("headache", "nausea"): "migraine",
    ("sore_throat", "cough"): "cold"
}

# Facts (known symptoms)
facts = {"fever", "cough"}

# Forward chaining function
def forward_chaining(rules, facts):
    inferred = set()
    added = True

    while added:
        added = False
        for conditions, conclusion in rules.items():
            # Check if all conditions are present in known facts
            if set(conditions).issubset(facts) and conclusion not in facts:
                facts.add(conclusion)
                inferred.add(conclusion)
                added = True

    return inferred

# Run forward chaining
inferred_facts = forward_chaining(rules, facts)

# Display results
print("Inferred :", list(inferred_facts)[0] if inferred_facts else "None")
print("Possible diagnoses:", inferred_facts)
