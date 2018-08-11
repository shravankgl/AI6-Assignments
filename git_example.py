```
This python file is a good starting point.
Activation Functions
```

#libraries
import numpy as np

def sigmoid(x):
  # enter code below
  return (1 / (1 + numpy.exp(-x)))

def tanh(x):
  # enter code below
  return((2/(1 + numpy.exp(-2x)))-1)

def relu(x):
  # entr code below
  y = 0
  if x>0:
    y = 1
  return(y)
