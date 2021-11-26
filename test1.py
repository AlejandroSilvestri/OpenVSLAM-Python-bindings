'''
Minimal test, starting openvslam.
It tests import and some basic bindings.
You can see openvslam console messages while warming up and shutting down.
You need config.yaml and orb_vocab.dbow2.  Feel free to change their paths.
'''

import openvslam

print("This is an operation test.  It should open openvslam binding module, init and shutdown openvslam whitout errors, and nothing else.  You should see many console messages as proof of work.")
print("openvslam module content:", dir(openvslam))
config = openvslam.config(config_file_path="./config.yaml")
SLAM = openvslam.system(cfg=config, vocab_file_path="./orb_vocab.dbow2")
SLAM.startup()
SLAM.shutdown()