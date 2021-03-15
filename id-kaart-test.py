from smartcard.System import readers
from smartcard.util import HexListToBinString, toBytes
from smartcard.Exceptions import NoCardException, NoReadersException

# Open-EID Testing with Python and pyscard library
# [tested with my own personal ID-card]

## Initializing ID-card reader and connecting to the ID-card
try:
    r = readers()
    try:
        conn = r[0].createConnection() ### Connecting straight up to first ID-card reader
        conn.connect()
    except NoCardException:
        print("> No card inserted. Insert a smart card into the reader.")
        exit(1)
except NoReadersException:
    print("> No card reader found. Insert smart card reader to your computer, then try again.")
    exit(1)

## I took the main example from that documentation:
## https://www.id.ee/wp-content/uploads/2020/10/td-id1-chip-app-1.pdf (page 33 of 43)
## docs author: Republic of Estonia, Information System Authority

print(">>> Select Main AID")
data, sw1, sw2 = conn.transmit(toBytes("00A40400 10 A000000077010800070000FE00000100"))
print("<<< %x %x" % (sw1, sw2))

print(">>> Select DF5000")
data, sw1, sw2 = conn.transmit(toBytes("00A4010C 02 5000"))
print("<<< %x %x" % (sw1, sw2))

print(">>> Select Transparent EF5002 (First Name)")
data, sw1, sw2 = conn.transmit(toBytes("00A4010C 02 5002"))
print("<<< %x %x" % (sw1, sw2))

print(">>> Read Binary")
data, sw1, sw2 = conn.transmit(toBytes("00B00000 00"))
print("<<< %x %x | %s - %s" % (sw1, sw2, data, HexListToBinString(data)))
print()
