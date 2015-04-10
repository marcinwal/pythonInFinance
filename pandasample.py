import numpy as np
import pandas as pd
import pandas.io.data as web

sp500 = web.DataReader('^GSPC',data_source='yahoo',
                       start='1/1/2000',end='4/04/2015)
                      
print sp500.info()
