"""defines pre-scripted behaviours"""
import time
import random
from math import *

idle_gap = 3.0
propogate_gap = 2.0

light_duration = 4 # unit: second
sma_duration = 4 # unit:second
active_patche_keys = [] # a list of patches that are currently active


def idle_random_event(sma_list, parameters, idle_event_start_time, active_list):
	# print('time is ' + str(type(time.time())))
	# print('idle_event_start_time is ' + str(idle_event_start_time))
	# print('idle_gap is ' + str(type(idle_gap)))
	if time.time() - idle_event_start_time > idle_gap:

		r_index = random.randint(0, len(sma_list) - 1)
		print('random index = ' + str(r_index))
		# rand_patch_par = patch_parameters[rand_patch_key]
		if not parameters[r_index].busy:
			active_list.append(r_index)
			print("active list:")
			print(active_list)
		# update idle start time
		idle_event_start_time = time.time()

	for idx in active_list:
		finish = single_motion(sma_list[idx], parameters[idx])
		if finish:
			active_list.remove(idx)

	return idle_event_start_time,  active_list


def single_motion(actr, actr_parameter):

	# perform one step for actuator
	finish = False
	actr_type = actr_parameter.gettype()

	if not actr_parameter.busy:
		actr_parameter.actrstart()

	if actr_type == 'sma':
		t = time.time() - actr_parameter.start_time
		# print('t=' + str(t))
		if t < sma_duration:
			# sma_index = 1
			# target = 1.5 # simulate the magnitude of controls current
			v = sin(t / 10) * (t / 10)
			actr.set_matrix(
				[0, 0, 0, 0,
				 0, 0, 0, 0,
				 v, 0, 0, 0])
		else:
			v = 0
			actr.set_matrix(
				[0, 0, 0, 0,
				 0, 0, 0, 0,
				 v, 0, 0, 0])
			finish = True
			actr_parameter.actrstop()

	# if time.time() - actr_parameter.start_time < light_duration:

	return finish


def active_event(trigger_key, coordinate, patches, patch_parameters, location_map, event_start_time):
	if time.time() - event_start_time > propogate_gap:

		event_start_time = time.time()

	return event_start_time


# def propogate():


def find_location(patch_map, trigger_key):
	# Find coordinate [row, col] of triggered patch
	coordinate = [-1, -1]
	for m in range(len(patch_map)):
		for n in range(len(patch_map[0])):
			if patch_map[m][n] == trigger_key:
				coordinate = [m, n]

	return coordinate