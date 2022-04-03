import pyshark
cap = pyshark.FileCapture('/tmp/mycapture.cap')
print(cap[0])