Here's a step-by-step guide on how to create a Bell state circuit in Qiskit, simulate it using a sampler, and then plot a histogram of the results.

```python
# Import necessary libraries
from qiskit import QuantumCircuit, Aer, execute
import matplotlib.pyplot as plt
import numpy as np

# Create a new quantum circuit
qc = QuantumCircuit(2)

# Apply H gates to both qubits (Happlies Hadamard gate to the qubit)
qc.h(0)
qc.h(1)

# Apply CNOT gate between the two qubits (CNOT Applies Controlled-NOT gate)
qc.cx(0, 1)

# Measure the state of the circuit
qc.measure([0, 1], [0, 1])

# Create a backend simulator for the quantum circuit
backend = Aer.get_backend('qasm_simulator')

# Run the quantum circuit on the backend and get the counts from the measurements
job = execute(qc.to_circuit(), backend, shots=10000)
counts = job.result().get_counts()

# Print out the counts of all possible states
for state, count in counts.items():
    print(f"State: {state} Probability: {count / 10000:.2%}")

# Plot a histogram of the results
plt.bar(counts.keys(), counts.values())
plt.xlabel('States')
plt.ylabel('Probabilities')
plt.title('Histogram of Bell State Circuit Results')
plt.show()
```

In this code:

1. We create a new quantum circuit using `QuantumCircuit(2)` which is a 2-qubit circuit.

2. We apply Hadamard gates to both qubits using `qc.h(0)` and `qc.h(1)`. This creates an equal superposition of the two states for each qubit.

3. We then apply a CNOT gate between the two qubits, which entangles them. The result is a Bell state where the two qubits are correlated.

4. Finally, we measure the state of the circuit using `qc.measure([0, 1], [0, 1])`, and run it on an Aer simulator backend with a specified number of shots (10000 in this case). We then get the counts from the measurements using `job.result().get_counts()`.

5. The counts are then plotted as a histogram to visualize the results.

Note: This code will output the probabilities for each possible state and plot a bar chart of these probabilities.