from configparser import ConfigParser

parser = ConfigParser()
parser.read("types.ini")

print("Integers:")
for name in parser.options("ints"):
    string_value = parser.get("ints", name)
    value = parser.getint("ints", name)
    print("  %-12s : %-7r -> %d" % (name, string_value, value))

print("\nFloats:")
for name in parser.options("floats"):
    string_value = parser.get("floats", name)
    value = parser.getfloat("floats", name)
    print("  %-12s : %-7r -> %0.2f" % (name, string_value, value))

print("\nBooleans:")
for name in parser.options("booleans"):
    string_value = parser.get("booleans", name)
    value = parser.getboolean("booleans", name)
    print("  %-12s : %-7r -> %s" % (name, string_value, value))
