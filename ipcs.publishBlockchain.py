# Scripts for AVA API
# Author: https://github.com/zefonseca/
# License MIT

import ipcs
import sys

blockchainID = sys.argv[1]

stt = ipcs.publishBlockchain(blockchainID)
print(stt)