import logging
import sys

from storage import TinyDBStorage, InMemStorage
from todoapp import TodoAppSvc

if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)

    port = int(sys.argv[1])
    dbpath = str(sys.argv[2])
    logging.info(f"running with port={port}, dbpath={dbpath}")

    svc = TodoAppSvc(port, TinyDBStorage(dbpath))
    #svc = TodoAppSvc(port, InMemStorage())
    svc.run()

