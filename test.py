import time
import numpy as np

class Timer:
    '''记录多次运行时间'''
    def __init__(self):
        self.times = []
        self.start()
    
    def start(self):
        '''启动计时器'''
        self.tik = time.time()
    
    def stop(self):
        '''停止计时器并将实践记录在列表中'''
        self.times.append(time.time()-self.tik)
        return self.times[-1]

    def avg(self):
        '''返回平均时间'''
        return sum(self.times)/len(self.times)

    def sum(self):
        return sum(self.times)
    
    def cumsum(self):
        return np.array(self.times).cumsum().tolist()