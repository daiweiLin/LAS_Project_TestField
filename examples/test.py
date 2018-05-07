import time
from pyrep import VRep
from math import *
# contextlib
# simpy
# multiprocessing cpu


with VRep.connect("127.0.0.1", 19997) as vrep:
#    vrep.simulation.stop()
#    time.sleep(2)
#vrep.simulation.start()

    j_pos = vrep.joint.with_position_control("Revolute_joint")
    j_sph = vrep.joint.spherical("sp_joint")
    for i in range(5):
        b = pi / 9
        j_pos.set_target_position(b * i + 0.2)
        time.sleep(1)

    for i in range(1000):
        v = sin(i / 100) * (i / 1000)
        j_sph.set_matrix([0, 0, 0, 0,
                          0, 0, 0, 0,
                          v, 0, 0, 0])
        time.sleep(0.01)

#vrep.simulation.stop()

