def steal(price):
	if price <= 100:
		str = "No one is stealing this cheap sh*t!"
	elif price <= 500 and price > 100:
		str = "This one is a class A replica!"
	elif price <= 1000 and price > 500:
		str = "This is okay. Just going to fit it, not steal it!"
	else:
		str = "I have to steal this!"

	return str

def fare(km,sec,noob):
	fare = 40 + (3.50 * (km/0.5)) + (3.50 * (sec/30))
	if noob:
		fare += 100
	return fare

def regulate(peeps): #broken as fuck, learn how to return an array/tuple/thing
	i = 0
	while i < len:
		fix[i] = math.floor(peeps[i] / 0.90)
		i += 1
	return fix

def csgoisbetter(skin):
	dmg = 0
	if skin['stun'] != 'passive':
		dmg += int(skin['stun'])
	if skin['2nd skill'] != 'passive':
		dmg += int(skin['2nd skill'])
	if skin['skill that inflicts damage'] != 'passive':
		dmg += int(skin['skill that inflicts damage'])
	if skin['ultimate'] != 'passive':
		dmg += int(skin['ultimate'])
	return dmg


print "gahaha"