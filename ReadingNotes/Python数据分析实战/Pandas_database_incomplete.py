# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 20:21:31 2017

@author: River

Python数据分析实战 第五章 数据读写 - 对接数据库
"""

from sqlalchemy import create_engine

#PostgreSQL
engine=create_engine('postgresql://scott:tiger@localhost:5432/mydatabase')

#MYSQl
engine=create_engine('mysql+mysqldbL//scott:tiger@localhost/foo')

#Oracle
engine=create_engine('some str')

#MSSQL
engine=create_engine('some str')

#SQLite
engine=create_engine('sqlite://foo.db')


#SQLite
import pandas as pd;import numpy as np
frame=pd.DataFrame(np.arange(20).reshape(4,5),
                   columns=['white','red','blue','black','green'])

engine=create_engine('sqlite:///foo.db')

