from . import *
from knite import *

Ӽɛռ.start()
LOGS.info(XEon)
idle()
Ӽɛռ.stop()   
try:
    shutil.rmtree(K)
    shutil.rmtree(P)
    shutil.rmtree(V)
    shutil.rmtree(Y)
    shutil.rmtree(M)
except:
    pass
LOGS.info(XEof)
