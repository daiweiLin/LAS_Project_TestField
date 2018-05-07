import time
from pyrep import VRep
from behaviours import *
from Parameter import *

# contextlib
# simpy
# multiprocessing cpu


with VRep.connect("127.0.0.1", 19997) as vrep:
	#    vrep.simulation.stop()
	#    time.sleep(2)
	# vrep.simulation.start()

	sma1 = vrep.joint.spherical("sp_joint")
	sma2 = vrep.joint.spherical("sp_joint2")
	sma_list = [sma1, sma2]
	# improve later........
	sma_par1 = Parameter('sma')
	sma_par2 = Parameter('sma')
	sma_par_list = [sma_par1, sma_par2]

	#######################
	# flags and constants #
	#######################
	state = -1
	idle_time = 4
	idle_gap = 5
	active_gap = 1

	idle_event_start_time = time.time()
	active_event_start_time = time.time()

	state_start_time = time.time()

	trigger_ls = []
	active_ls = []



	print('Simulation starts')
	print('*************')
	while True:
		#########################################
		#  Get triggered locations and numbers  #
		#########################################

		# for sma_id in sma_patches:
		# 	ir_out = sma_patches[sma_id].get_block_output('IRSensor_1', 'ir')
		# 	print str(sma_id) + ':' + str(ir_out.value)
		# 	if ir_out.value == 1:
		# 		trigger_key.append(sma_id)
		# 		coordinate = find_location(location_map)

		if len(trigger_ls) == 0 and time.time() - state_start_time >= idle_time:
			# Idle state
			# Update start time only at state transitions
			if state != 0:
				state = 0
				idle_event_start_time = time.time()
				print('state = ' + str(state))
		elif len(trigger_ls) > 0:
			# Active state
			# activate blocks
			if state != 1:
				state = 1
				active_event_start_time = time.time()
				print('state = ' + str(state))

		if state == 0:
			# random delay
			idle_event_start_time, active_ls = idle_random_event(sma_list, sma_par_list, idle_event_start_time, active_ls)

		#if state == 1:
			# propagate the action
			# assume ONLY ONE sensor is triggered each time


# vrep.simulation.stop()

