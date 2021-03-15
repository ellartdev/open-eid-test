# open-eid-test
 Testing out, getting content from ID-card with Python

## Purpose
I wanted to see, what stuff I could get from my ID-card. You can get the contents of the card easily as it turned out. Needed some hex commands to type in

Keep in mind: different countries have likely different hex commands to parse info from them.

## How does it work?
- Insert in your Estonian ID-card. Currently it looks for first ID-card reader in a list if you have multiple ID-card slots installed.
- Install Python if you haven't
- Install Smartcard Reader library for Python: `python -m pip install pyscard`
- Run the script: `python id-kaart-test.py`

### Expected output
```
>>> Select Main AID
<<< 90 0
>>> Select DF5000
<<< 90 0
>>> Select Transparent EF5002 (First Name)
<<< 90 0
>>> Read Binary
<<< 90 0 | [69, 76, 76, 65, 82, 84] - ELLART
```

90 0 - OK

## Bugs?
I noticed that Windows hijacks the ID-card for itself for about 5-8 seconds. I have no idea what Windows is doing with it. After that 5-8 seconds, other applications like this script can use the ID-card.

Possible output #1:
```
>>> Select Main AID
<<< 90 0
>>> Select DF5000
<<< 90 0
>>> Select Transparent EF5002 (First Name)
<<< 90 0
>>> Read Binary
<<< 69 86 | [] - 
```

Possible output #2:
```
>>> Select Main AID
<<< 90 0
>>> Select DF5000
<<< 90 0
>>> Select Transparent EF5002 (First Name)
<<< 6a 82
>>> Read Binary
<<< 69 86 | [] -
```

90 0 - OK

Hex code errors:
- 6A 82 - File not found for provided FID
- 69 86 - Missing  selection  pointer  for EF

## Docs on Estonian ID-card and stuff
- [Estonia ID1Chip/App 2018 - Technical Description](https://www.id.ee/wp-content/uploads/2020/10/td-id1-chip-app-1.pdf) | Made by RIA / Information System Authority
