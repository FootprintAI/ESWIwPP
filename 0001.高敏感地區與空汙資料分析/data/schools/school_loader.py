import os
import pathlib
import pandas as pd

class SchoolLoader():
    def __init__(self):
        self.base_path = pathlib.Path(__file__).parent.resolve()

    def read_excel(self, filename:str):
        return pd.read_excel(os.path.join(self.base_path, filename), engine='xlrd')

    def load_special_education(self):
        return self.read_excel(r'mapdata201806041032/105學年度各級學校分布位置_特殊教育學校.xls')

    def load_elementory_school(self):
        return self.read_excel(r'mapdata201805310212/105學年度各級學校分布位置_國小.xls')

    def load_junior_supplementary_school(self):
        return self.read_excel(r'mapdata201806041032(2)/105學年度各級學校分布位置_國中小補校.xls')

    def load_junior_high_school(self):
        return self.read_excel(r'mapdata201805310229/105學年度各級學校分布位置_國中.xls')

    def load_senior_high_school(self):
        return self.read_excel(r'mapdata201805311206/105學年度各級學校分布位置_高中職.xls')

    def load_college_school(self):
        return self.read_excel(r'mapdata201805311038/105學年度各級學校分布位置_大專院校.xls')
