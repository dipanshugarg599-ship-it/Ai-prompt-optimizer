# Deep Learning Neural Network Demo
# B.Tech AI & ML Project

import math
import random

print("=" * 60)
print("       🧠 DEEP LEARNING NEURAL NETWORK")
print("=" * 60)


# Activation Function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))


# Neural Network
class NeuralNetwork:

    def __init__(self):
        random.seed(10)

        # Input -> Hidden layer
        self.w1 = random.uniform(-1, 1)
        self.w2 = random.uniform(-1, 1)

        # Hidden -> Output
        self.w3 = random.uniform(-1, 1)
        self.w4 = random.uniform(-1, 1)

        self.bias1 = random.uniform(-1, 1)
        self.bias2 = random.uniform(-1, 1)

    def predict(self, x1, x2):

        # Hidden Layer
        h1 = sigmoid(x1 * self.w1 + x2 * self.w2 + self.bias1)
        h2 = sigmoid(x1 * self.w2 + x2 * self.w1 + self.bias2)

        # Output Layer
        output = sigmoid(h1 * self.w3 + h2 * self.w4)

        return output


# Create model
model = NeuralNetwork()

print("\nNeural Network Created Successfully!")
print("Architecture:")
print("Input Layer  ->  Hidden Layer  ->  Output Layer")
print("   2 neurons       2 neurons        1 neuron")


while True:

    print("\n" + "-" * 60)

    user_input = input(
        "Enter two numbers (example: 1 0) or type 'exit': "
    )

    if user_input.lower() == "exit":
        print("\n🧠 Deep Learning program closed!")
        break

    try:
        values = user_input.split()

        if len(values) != 2:
            print("⚠️ Please enter exactly two numbers.")
            continue

        x1 = float(values[0])
        x2 = float(values[1])

        result = model.predict(x1, x2)

        print("\n📊 Neural Network Output:", round(result, 4))

        if result >= 0.5:
            print("✅ Prediction: CLASS 1")
        else:
            print("❌ Prediction: CLASS 0")

    except ValueError:
        print("⚠️ Invalid input! Please enter numbers.")
