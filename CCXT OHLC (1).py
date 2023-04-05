import ccxt
import pandas as pd
import pandas_ta as ta
import numpy as np
import os
from datetime import date, datetime, timezone, tzinfo
import time, schedule
import numpy as np
import requests
from math import floor
import matplotlib.pyplot as plt
import ta as tl
import math
import functools
from pandas import DataFrame
import warnings
from io import StringIO
from pathlib import Path
from scipy.signal import argrelextrema
from collections import deque
import itertools
import talib.abstract as tt
import talib
warnings.filterwarnings("ignore")
symbol = "ETH/BUSD"  # Binance 
pos_size =1
timeframe = "5m"
 


# API TANIMLAMALARI
account_binance = ccxt.binance({
    "apiKey": '',
    "secret": '',
    "enableRateLimit": True,
    'options': {
        'defaultType': 'spot'
    }
})




while True: 

    try:
        
        orderTime = datetime.utcnow()
        ohlcvLB = account_binance.fetch_ohlcv(symbol, timeframe)
        dfLB = pd.DataFrame(ohlcvLB, columns=['time', 'open', 'high', 'low', 'close', 'volume'])
        indiPoint = pd.DataFrame(columns=['time'])
        if len(ohlcvLB):
            dfLB['time'] = pd.to_datetime(dfLB['time'], unit='ms')
            print(dfLB) # this is the dataframe



                
                        

        
    except Exception as e:
        print(e)
        continue


