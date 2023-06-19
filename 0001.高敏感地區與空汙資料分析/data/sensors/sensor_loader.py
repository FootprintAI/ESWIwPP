import os
import pathlib
import pandas as pd

class SensorLoader():
    def __init__(self):
        self.base_path = pathlib.Path(__file__).parent.resolve()

    def load_devices(self):
        return pd.DataFrame.from_dict(
                pd.read_pickle(
                    os.path.join(
                        self.base_path,
                        'government_device-20230616.tar.gz')), orient='index'))

    def load_devices_geo(self):
        return pd.DataFrame.from_dict(
                pd.read_pickle(
                    os.path.join(
                        self.base_path,
                        'device_geo_20230616.tar.gz')), orient='index'))

    def load_sensors(self):
        return pd.DataFrame.from_dict(
                pd.read_pickle(
                    os.path.join(
                        self.base_path, 
                        'government_device_data-20230616.tar.gz')), orient='index'))

    def load_full_sensors(self):
        url = 'https://storage.dev01.footprint-ai.com/project-2-striking-black-bird/data/0001/government_device_data-20230616.tar.gz'
        return pd.DataFrame.from_dict( pd.read_pickle(url), orient='index')


