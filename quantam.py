from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2, 2)

# Apply a Hadamard gate to the first qubit, putting it in superposition (|0> + |1>)
qc.h(0)

# Apply a CNOT gate, entangling the first qubit with the second
qc.cx(0, 1)

# Measure both qubits
qc.measure([0,1], [0,1])

# Use Aer's simulator to run the circuit
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
job = simulator.run(compiled_circuit, shots=1024)
result = job.result()
counts = result.get_counts()

# Display the results
print(counts)
# Output will be approximately {'00': 512, '11': 512}
plot_histogram(counts)
