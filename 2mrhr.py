#/usr/bin/env python3
curies = float(input("Curies?:"))
ir = 5900
int1 = (curies * ir)
co = 14000
int2 = (curies * co)
d1 = 1
i2 = 2
Ir192 = ((((int1 * d1) / i2)) ** .5)
Co60 = ((((int2 * d1) / i2)) ** .5)
source = input("Ir192 Or Co60?:")
if source == Ir192:
    print ("{}ft".format(Ir192))
elif source == Co60:
    print ("{}ft".format(Co60))
