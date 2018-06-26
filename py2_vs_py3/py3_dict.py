metric_prefixes = {
	"peta":	1000000000000000,
	"tera":	1000000000000,
	"giga":	1000000000,
	"mega":	1000000,
	"kilo":	1000,
	"hecto": 100,
	"deca": 10,
	"deci":	0.1	,
	"centi": 0.01	,
	"milli": 0.001	,
	"micro": 0.000001	,
	"nano":	0.000000001	,
	"pico":	0.000000000001,
	"femto": 0.000000000000001
}

print("keys(): ")
key_iter = metric_prefixes.keys()
print("key iter type: {}".format(type(key_iter)))
for key in metric_prefixes.keys():
	print("\t{}".format(key))
