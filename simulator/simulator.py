#
# Copyright 2017 by InfoMus Lab - DIST - University of Genova, http://www.infomus.org
#

"""Simulator sketch"""

# execfile( 'simulator.py' )

import eyesweb_mobile
import time
import random
import csv
import sensor_info

from csv_reader import read_csv
from my_callback import my_callback
from patches_manager import *
from movement import *

from Parameter import *
from Behaviour import *

"""
Main
"""

with VRep.connect("127.0.0.1", 19997) as vrep:


	# sculpture = read_csv('sculpture.csv')
	# (patches, callbacks) = init_patches_from_structure(kernel, sculpture)
	# user_simulation_patch = init_users_simulation_patch( kernel, False )
	visitor_patch = init_my_visitor(kernel)
	patches['visitor'] = visitor_patch

	# start_all_patches(patches)

	################################################################
	################################################################
	# position = 1
	t = 0
	# traj = [-0.5, 0.5, 1, 0.5]
	# prev_position = 0
	num_sma_patches = 0
	print 'Waiting for CTRL+C to be pressed'
	# check patches exists before using them
	patch_parameters = {}
	if 'sma-infrared' in patches:
		sma_patches = patches['sma-infrared']
		num_sma_patches = len(sma_patches)
		print 'sma patches : ' + str(num_sma_patches)

		for patch_id in sma_patches:
			patch_parameters[patch_id] = PatchParameter('sma-infrared')
	if 'visitor' in patches:
		visitor = patches['visitor']

	# relative location of the patches:
	#---------------------------------
	#    | 1   2   3  |
	#    |            |
	#    | 4   5   6  |
	#---------------------------------

	n = 3
	m = 2
	location_map = [[0] * n for i in range(m)]
	if num_sma_patches == 6:
		location_map[0][0] = 'sma-ir1'
		location_map[0][1] = 'sma-ir2'
		location_map[0][2] = 'sma-ir3'
		location_map[1][0] = 'sma-ir4'
		location_map[1][1] = 'sma-ir5'
		location_map[1][2] = 'sma-ir6'

	#######################
	# flags and constants #
	#######################
	state = 0
	idle_time = 4
	idle_gap = 5
	active_gap = 1

	idle_event_start_time = time.time()
	active_event_start_time = time.time()

	state_start_time = time.time()

	active_patches = []

	try:
		while True:
			time.sleep(0.01)
			# t = t + 1

			# if num_sma_patches > 0:
			# sma_index = random.randint(0, num_sma_patches - 1 )
			sma_trigger_key = []
			for sma_id in sma_patches:
				ir_out = sma_patches[sma_id].get_block_output('IRSensor_1', 'ir')
				print str(sma_id) + ':' + str(ir_out.value)
				if ir_out.value == 1:
					sma_trigger_key.append(sma_id)
					coordinate = find_location(location_map)

			print '*************'

			if len(sma_trigger_key) == 0 and time.time()-state_start_time >= idle_time:
				# Idle state
				# Update start time only at state transitions
				if state != 0:
					state = 0
					idle_event_start_time = time.time()
			elif len(sma_trigger_key) > 0:
				# Active state
				# activate blocks
				if state != 1:
					state = 1
					active_start_time = time.time()

			if state == 0:
				# random delay
				idle_event_start_time = idle_random_event(sma_patches, patch_parameters, idle_start_time, num_sma_patches)

			if state == 1:
				# propagate the action
				# assume ONLY ONE sensor is triggered each time
				active_event_start_time = active_event(sma_trigger_key, coordinate, sma_patches, patch_parameters, location_map, active_event_start_time)



			# sma_patch_index = 0
			# p = sma_patches['sma-ir1']
			#
			# time.sleep(0.1)
			#
			# sma_index = 1
			# target = random.uniform(-3.14, 3.14)
			# p.set_block_parameter('sma_control_' + str(sma_index), 'value', eyesweb_mobile.double_parameter(target))

			# visitor moves
			# prev_position = movement(t, traj, visitor, prev_position)

	except KeyboardInterrupt:
		pass

	stop_all_patches(patches)

	patches.clear()
	kernel = None

	print 'End of script'
