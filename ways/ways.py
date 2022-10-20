from dataclasses import dataclass
import yaml
from pydantic import BaseModel

with open('network-device.yaml', 'r') as file:
    devices = yaml.safe_load(file)


"""
Parse through the YAML in a simple script

ref. https://pyyaml.org/wiki/PyYAMLDocumentation
"""

for i in devices['switches']:
    print(f" device {i['hostname']} is made by {i['vendor']} and is in location {i['location']}")



"""
Parse through the YAML with a Class

ref. https://docs.python.org/3/library/dataclasses.html
"""
class Devices:
    def __init__(self, hostname, vendor, location):
        self.hostname = hostname
        self.vendor = vendor
        self.location = location
    
D = [Devices(hostname = d['hostname'], vendor = d['vendor'], location = d['location']) for d in devices['switches']]

for i in D:
    print(f" device {i.hostname} is made by {i.vendor} and is in location {i.location} {type(Devices)}")     


"""
Using the dataclass decorator

ref. https://docs.python.org/3/library/dataclasses.html
"""
@dataclass
class OtherDevices:
    hostname: str
    vendor: str
    location: str

A = [OtherDevices(**c) for c in devices['switches']]

for i in A:
    print(f" device {i.hostname} is made by {i.vendor} and is in location {i.location} {type(OtherDevices)}")     


"""
Using Pydantic

ref. https://pydantic-docs.helpmanual.io/usage/models/
"""
class Switches(BaseModel):
    hostname: str
    vendor: str
    location: str

E = [Switches(**h) for h in devices['switches']]

for i in E:
    print(f" device {i.hostname} is made by {i.vendor} and is in location {i.location} with {type(Switches)}")   
