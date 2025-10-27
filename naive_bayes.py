import pandas as pd

df = pd.read_csv("buy_computer.csv")


features = ['age', 'income', 'student', 'credit_rating']
target = 'buys_computer'

# =======================================================
# Calculate Prior Probabilities P(Class)
# =======================================================
class_probs = df[target].value_counts(normalize=True).to_dict()

# =======================================================
# Calculate Conditional Probabilities P(Attribute | Class)
#     (with Laplace smoothing for stability)
# =======================================================
conditional_probs = {}

for feature in features:
    conditional_probs[feature] = {}
    for value in df[feature].unique():
        conditional_probs[feature][value] = {}
        for c in df[target].unique():
            subset = df[df[target] == c]
            # Laplace smoothing
            prob = (len(subset[subset[feature] == value]) + 1) / (len(subset) + len(df[feature].unique()))
            conditional_probs[feature][value][c] = prob

# =======================================================
# Function to predict class for ONE new sample
# =======================================================
def predict(sample):
    probs = {}
    for c in class_probs:
        # Start with prior probability
        probs[c] = class_probs[c]
        # Multiply by each conditional probability
        for feature in features:
            value = sample[feature]
            probs[c] *= conditional_probs[feature].get(value, {}).get(c, 1e-6)
    return max(probs, key=probs.get)

# =======================================================
# 5️⃣ Predict for one new sample
# =======================================================
new_sample = {
    'age': 'youth',
    'income': 'medium',
    'student': 'yes',
    'credit_rating': 'fair'
}

result = predict(new_sample)
print("Predicted class for new sample:", result)
