import math
h = int(input('Часы:'))
m = int(input('Минуты:'))
s = int(input('Секунды:'))
angle = 0
if h > 12:
    true_h = math.sqrt((12 - h) ** 2)
else:
    true_h = h
one_angle_hour = 360 // 12
one_angle_minute = one_angle_hour // 60
one_angle_seconds = one_angle_minute // 60

angle = one_angle_hour * h + one_angle_minute + one_angle_seconds 

print('Угол равен:', angle)

    

    
