import numpy as np

# Transition model
T = np.array([[0.7, 0.3], [0.3, 0.7]])

# Sensor models
O_true = np.array([0.9, 0.2])  # Umbrella = True
O_false = np.array([0.1, 0.8])  # Umbrella = False


def normalize(v):
    return v / np.sum(v)


def forward(prev_f, observation):
    # Correct sensor vector
    if observation:
        sensor_vector = O_true
    else:
        sensor_vector = O_false

    # f_t = α * O_t * ( T^T @ f_{t-1} )
    prediction = T.T @ prev_f
    f = sensor_vector * prediction
    return normalize(f)


# Part 1: Verification for two umbrellas (T, T)
f = np.array([0.5, 0.5])
f1 = forward(f, True)
f2 = forward(f1, True)

print("P(Rain at t=2 | umbrellas T,T) =", f2[0])

observations = [True, True, False, True, True]

f = np.array([0.5, 0.5])
messages = []

for obs in observations:
    f = forward(f, obs)
    messages.append(f)

print("Messages after each observation:")
for i, msg in enumerate(messages):
    if i < len(observations):
        print(f"After observation {i+1} (Umbrella = {observations[i]}): P(Rain) = {msg[0]:.4f}, P(No Rain) = {msg[1]:.4f}")
