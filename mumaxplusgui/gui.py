from mumaxplus import Antiferromagnet, DmiTensor, Ferromagnet, FieldQuantity, Grid, InterParameter, Magnet, NcAfm, Parameter
from mumaxplus import PoissonSystem, ScalarQuantity, StrayField, TimeSolver, BoundaryTraction, Variable, World
import subprocess



"Asking user for parameters for simulation"
world = input("World Size: ")
print(f"Confirming: {world}")


file_location = input("Where is your file located? ")
print(f"Confirming: {file_location}")

result = subprocess.run(["echo", "Hello from Terminal"], capture_output=True, text=True)
print(result.stdout)  # Outputs: Hello from Terminal