import logging
import asyncio


import shelve
from collections import OrderedDict
import pickle,os

# NODES_PRIME = [("128.232.229.63",8468), ("68.66.241.111",8468)]    

NODES_PRIME = [("68.66.241.111",8467)]
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger = logging.getLogger('app')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

def log(*args):
    #with open('log.txt','a+') as of:
    #    of.write(' '.join([str(x) for x in args])+'\n')
    line = ' '.join(str(x) for x in args)
    logger.debug(line)

async def echo(msg):
    print('echo',msg)    

def boot_selfless_node(port=8468, loop=None):
    

    if not loop: loop = asyncio.get_event_loop()
    loop.set_debug(True)

    # shelf = HalfForgetfulStorage()
    shelf = None
    print('starting kad server')

    #server = Server(storage=shelf)
    try:
        from kad import KadServer,HalfForgetfulStorage
    except ImportError:
        from .kad import KadServer,HalfForgetfulStorage
    
    server = KadServer(storage=HalfForgetfulStorage())
    loop.create_task(server.listen(port))

    # try:
    #     loop.run_forever()
    # except KeyboardInterrupt:
    #     pass
    # finally:
    #     server.stop()
    #     loop.close()
    return loop


def boot_lonely_selfless_node(port=8467):
    loop = boot_selfless_node(port)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.stop()
        loop.close()





