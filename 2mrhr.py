#/usr/bin/env python3
Curies=float(input("Curies?: "))
Ir=5900
Int=(Curies * Ir)
Co=14000
Int2=(Curies * Co)
d1=1
i2=2
Ir192=((((Int*d1)/i2))**.5)
Co60=((((Int2*d1)/i2))**.5)
Source=input("Ir192 Or Co60?: ")
if Source == Ir192:
    print("{}ft".format(Ir192))
elif Source == Co60:
    print("{}ft".format(Co60))
