from genie.testbed import load
import pprint
testbed = load("yaml/my_testbed.yaml")
devices = ['node1','node2']
for device in devices:
    device = testbed.devices[device]
    device.connect(init_exec_commands=[], init_config_commands=[])
    response = device.parse('show ip int brief')
    pprint.pprint (response)
    #chassis = response['version']['chassis_sn']