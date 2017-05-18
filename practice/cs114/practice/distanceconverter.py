km_per_mi = 1.60934
mi_per_km = 0.621371
ft_per_m = 3.28084
m_per_ft = 0.3048

print('Hey, give me a number. This is going to be your distance, got it?')
num = float(input())

print('Okay, cool. Is that miles or kilometers. Or perhaps feet or meters...?')
print('Please answer in "mi" or "km" or "ft" or "m". Thanks.')

distance_unit = input()
miles = mi_per_km * num
kilometers = km_per_mi * num
feet = ft_per_m * num
meters = m_per_ft * num

if distance_unit == 'mi':
    print('Aight. I gotchu. ' + str(num) + 'mi.... that would be ' + str(kilometers) + ' kilometers')
    print('Yeah?')

elif distance_unit == 'km':
    print('OKAY. In that case, your ' + str(num) + 'km is...' + str(miles) + ' miles.')

elif distance_unit == 'ft':
    print('Let us do this! ' + str(num) + 'ft is equivalent to ' + str(meters) + ' meters!')

elif distance_unit == 'm':
    print('So... uh, ' + str(num) + ' meters comes out to ' + str(feet) + ' feet.')

print('BYE')
