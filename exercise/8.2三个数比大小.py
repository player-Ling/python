x,y,z=6,5,4
#shit
"""
small=x if x<y else y
small=small if small<z else z
"""
small=x if x<y and x<z else(y if y<z else z)
print(small)

x,y,z=y,z,x
print("x=%d,y=%d,z=%d"%(x,y,z))
