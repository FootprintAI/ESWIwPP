import requests

from typing import TypedDict

# list all available devices from government type
def get_government_devices(time:str = '2023-06-15 22:00'):
    # device_id_dict is dict keyed by device id
    device_id_dict = {}

    base_url = 'https://wot.epa.gov.tw/Layer/get_device_data'
    query_params = {
        'time': time,
        'type': 'government',
    }
    resp = requests.get(base_url,
                 params=query_params)
    #resp.status_code
    device_json = resp.json()
    for key in device_json['data']:
        val = device_json['data'][key]
        intstr = hex2int(key)
        if intstr not in device_id_dict:
            device_id_dict[intstr] = val

    return device_id_dict

def hex2int(hexstr: str)-> str:
    return str(int(hexstr, 16))

def get_device_location():
    # device_id2loc_dict is keyed by $device id with device's geo location data
    device_id2loc_dict = {}

    base_url = 'https://wot.epa.gov.tw/Layer/get_json'

    query_iot = { 'url': 'http://10.0.100.184/api/v1/device/iot?fields=lon,lat,desc,name&display=true' }
    query_nat = { 'url': 'http://10.0.100.184/api/v1/device/national_hr?fields=lon,lat,desc,name' }

    query_params = [ query_iot, query_nat ]
    for query_param in query_params:
        resp = requests.get(base_url, params=query_param)
        #resp.status_code
        device_json_list = resp.json()
        for device_json in device_json_list:
            device_id2loc_dict[device_json['_id']] = device_json
    return device_id2loc_dict

def get_device_datapoint(device_id: str, start_time:str = '2023-06-16 10:00:00', end_time:str = '2023-06-19 10:00:00'):
    # device_datapoint is keyed by time, contain all smapled data from the device
    device_datapoint = {}

    base_url = 'https://wot.epa.gov.tw/Layer/get_json'
    query_params = {
        'url':
        'http://10.0.100.184/api/v1/data/device/{0}/pm2_5,pm10,co,voc/{1}/{2}/0?'.format(device_id, start_time, end_time),
    }
    try:
        resp = requests.get(base_url,
                 params=query_params, timeout=10)
    except requests.exceptions.Timeout:
        print("request timeout with device id:{}".format(device_id))
        return device_datapoint
    if resp.status_code != 200:
        return device_datapoint
    device_datapoints_json = resp.json()
    if not device_datapoints_json:
        return device_datapoint
    for datapoint in device_datapoints_json:
        key = datapoint['time']
        val = { }
        if 'pm2_5' in datapoint:
            val['pm2_5'] = datapoint['pm2_5']
        if 'pm10' in datapoint:
            val['pm10'] = datapoint['pm10']
        if 'voc' in datapoint:
            val['voc'] = datapoint['voc']
        device_datapoint[key] = val 
    return device_datapoint

def save(filename: str, d):
    import pickle
    import time

    start_time = time.time()
    with open(filename, 'wb') as fd:
        pickle.dump(d, fd, protocol=pickle.HIGHEST_PROTOCOL)
    print("--- save took %s seconds ---" % (time.time() - start_time))

def load(filename: str):
    import pickle
    with open(filename, 'rb') as fd:
        return pickle.load(fd)

if __name__ == '__main__':
    import os


    government_device_id_dict = {}
    government_devices_pickle_filename = 'government_device-20230619.pickle'
    if os.path.exists(government_devices_pickle_filename):
        government_device_id_dict = load(government_devices_pickle_filename)
    else:
        government_device_id_dict = get_government_devices('2023-06-19 10:00')
        save(government_devices_pickle_filename, government_device_id_dict)

    device_geo_dict = {}
    devices_geo_pickle_filename = 'device_geo_20230616.pickle'
    if os.path.exists(devices_geo_pickle_filename):
        device_geo_dict = load(devices_geo_pickle_filename)
    else:
        device_geo_dict = get_device_location()
        save(devices_geo_pickle_filename, device_geo_dict)

    device_data_pickle_filename = 'government_device_data-20230616.pickle'
    government_device_data_dict = {}
    if os.path.exists(device_data_pickle_filename):
        government_device_data_dict = load(device_data_pickle_filename)
    for device_id in government_device_id_dict:
        if device_id in government_device_data_dict:
            print('skipped {}'.format(device_id))
            continue
        print ('{}/{}'.format(len(government_device_data_dict), len(government_device_id_dict)))
        device_data = get_device_datapoint(device_id)
        government_device_data_dict[device_id] = device_data
        if len(government_device_data_dict) % 1000 == 0:
            save("{}.{}".format(pickle_filename, len(government_device_data_dict)), government_device_data_dict)
    save("{}.{}".format(pickle_filename, 'final'), government_device_data_dict)
