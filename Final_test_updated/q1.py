import sys
import numpy as np
total_subparts = 4

train = sys.argv[1]
test = sys.argv[2]

classes = ["0", "1"]

with open(test) as f:
    data = f.readlines()
    for subpart in range(total_subparts):           # Print predictions for each subpart
        for line in data:
            print classes[np.random.randint(0,2)]
