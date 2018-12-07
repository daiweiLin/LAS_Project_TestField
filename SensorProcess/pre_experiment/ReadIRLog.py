import numpy as np
import re
import math
import warnings


def ReadTXT():
    file_name = "IR_samples_ROM_July_04_2018_at_12-59-55" + ".txt"
    num_sensor = 24
    num_group = int(num_sensor/2)
    freq = 10 # Hz
    
    one_sec_readings = []
    for _ in range(num_group):
        one_sec_readings.append([])
        one_sec_readings.append([])
    
    all_readings = np.zeros((num_sensor,1))
    all_times = []
    
    file = open(file_name,'r')
#    group_count = 0
    last_time = '13-00-13'
    for line in file:

        m = re.search(r'[0-9]+-[0-9]+-[0-9]+', line)
        time = m.group(0)

        m = re.search(r'[0-9]+, [0-9]+',line)
        m_num = re.findall(r'[0-9]+',m.group(0))
        value = [int(m_num[0]), int(m_num[1])]

        m = re.search(r'BPC [0-9]+', line)
        m_id = re.search(r'[0-9]+',m.group(0))
        group_id = int(m_id.group(0)) - 1

        
        if time != last_time:
            
            np_one_sec_readings = fill_missing_data(one_sec_readings, (num_sensor,freq))
            all_readings = np.append(all_readings, np_one_sec_readings, axis = 1)
            for _ in range(freq):
                all_times = np.append(all_times, time)
            # Reset
            one_sec_readings = []
            for _ in range(num_group):
                one_sec_readings.append([])
                one_sec_readings.append([])
            last_time = time
        else:
            one_sec_readings[group_id*2].append(value[0])
            one_sec_readings[group_id*2+1].append(value[1])
      

    file.close()
    
    return all_times, all_readings

def fill_missing_data(data, shape):
    """
    Input: 2D list, each row doesn't necessarily have same length
    Output: 2D numpy array
    """
    assert shape[0] == len(data)
    
    for r in range(len(data)):
        diff = shape[1] - len(data[r])
        if diff != 0:
            last_val = data[r]
            for _ in range(diff):
                data[r].append(last_val)
    
    return np.array(data)
    
if __name__ == '__main__':
    time, readings = ReadTXT()