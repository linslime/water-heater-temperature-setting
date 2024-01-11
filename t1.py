import math

c = 4200
m = 60
a = 0.879
s = 1.08
p2 = 1500
v = 0.08

T1 = 37
T2 = 25
Ta = 46
Tb = 37

def get_t1(T1,T0,Ta,Tb):
    temp1 = p2 - v * c * (T1 - T0) + a * s * (T0 - Ta)
    temp2 = p2 - v * c * (T1 - T0) + a * s * (T0 - Tb)
    t = c * m /(a * s) * math.log(temp1/temp2)
    return t


def get_Ta(T1,T0,t,Tb):
    temp1 = a * s /( c * m) * t
    temp2 = p2 - v * c * (T1 - T0) + a * s * (T0 - Tb)
    temp3 = p2 - v * c * (T1 - T0) + a * s * T0
    Ta = (temp3 - math.exp(temp1) * temp2)/(a * s)
    if Ta < Tb:
        Ta = Tb
    return Ta + 5

def get_low(T0,Ta,Tb):
    temp1 = c * m / (a * s)
    temp2 = (T0 - Tb) / (T0 - Ta)
    t = temp1 * math.log(temp2)
    return t / 3600
# for i in range(37):
#     print(get_Ta(37,i,900,37))

def get_up(T0,Ta,Tb):
    temp1 = p2 + a * s * (T0 - Ta)
    temp2 = p2 + a * s * (T0 - Tb)
    t = c * m / (a * s) * math.log(temp1 / temp2)
    return t / 3600

# for i in range(5,12):i
#     print(i,get_low(i,55,60))

# for i in range(4,11):
#     print(get_up(i,42,60))


def get_Tb(T1,T0,t,Ta):
    temp1 = a * s /( c * m) * t
    temp2 = p2 -   v * c * (T1 - T0) + a * s * (T0 - Ta)
    temp3 = p2 -   v * c * (T1 - T0) + a * s * T0
    Tb = (temp3 - temp2/math.exp(temp1) )/(a * s)
    return Tb
# print(get_Tb(42,7,900,60))
# i = 64
# while i <= 75:
#     temp1 = get_Tb(42,7,900,i)
#     temp2 = get_up(7,temp1,59)
#     temp3 = get_up(7,59,i)
#     temp4 = temp2 + 0.5 + temp3
#     # print(temp4)
#     print(temp4*(temp2))
#     i += 0.1
# print(get_up(7,64,76))
# print(get_up(7,temp1,59))
for i in range(5,12):
    temp1 = get_Tb(42,i,900,60)
    temp2 = get_up(i,temp1,60)
    print(0.25+temp2)