# get_ipython().system('pip3 install pandas')
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description = "linear interpolation")
parser.add_argument("-cp", "--cpath", default = "tester.csv", help = "csv data path")
parser.add_argument("-rp", "--resultpath", default = "result.csv", help = "result data path")
args = parser.parse_args()

tan=pd.read_csv(args.cpath)

tan['datetime']=pd.to_datetime(tan['datetime'])
# tan.info()

tan_1=tan.set_index('datetime')
# tan_1.info()
# type(tan_1)

tan_1_resample=tan_1.resample(rule='T').last()
# 리샘플링 할 기준 입니다. 단위로는 Y, M, D, H, T(min), S ... 등을 조합하여 사용할 수 있습니다.

tan_2=tan_1_resample.interpolate(method='linear') #, order=0.01

tan_3=round(tan_2['level'],1)

tan_3.to_csv(args.resultpath)




