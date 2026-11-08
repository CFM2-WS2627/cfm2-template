"""Check that JuPedSim and PedPy are installed and a simulation runs."""

import jupedsim as jps
import pedpy
from shapely import Polygon

geometry = Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])
simulation = jps.Simulation(model=jps.CollisionFreeSpeedModel(), geometry=geometry)
exit_id = simulation.add_exit_stage(Polygon([(9, 4), (10, 4), (10, 6), (9, 6)]))
journey_id = simulation.add_journey(jps.JourneyDescription([exit_id]))
for y in range(3, 8):
    simulation.add_agent(
        jps.CollisionFreeSpeedModelAgentParameters(
            position=(1, y), journey_id=journey_id, stage_id=exit_id
        )
    )
while simulation.agent_count() > 0:
    simulation.iterate()

print(f"jupedsim {jps.__version__}, pedpy {pedpy.__version__}")
print(f"5 agents left the room after {simulation.elapsed_time():.1f} s")
print("Setup OK")
