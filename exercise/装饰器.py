import time
import functools
def ti(fn):
    @functools.wraps(fn)
    def warpp(*args,**kw):
        start=time.time()
        fun=fn(*args,**kw)
        end=time.time()
        print('运行了%f秒'%(end-start))
        return fun
    return warpp

@ti
def now():
    time.sleep(1)
    print('2015-3-25')

now()
