import numpy as np

coords = [
    {
        'x': 0,
        'y': 0,
        'r': 0,
        'theta': 0,
    }
]


def coordConvert(x,y):
    if x==0 and y==0:
        return 'depois eu faço'
    
    
    r = np.sqrt((x**2 + y**2))
    if x != 0:
        theta = np.arctan(y/x)
    elif y > 0;
        theta = (np.pi/2)
    else:
        theta = -(np.pi/2)
        
    return 

for x in range(0,11):
    for y in range(0,11):
        coords.append({
            'x': x
        })