
# parses and returns the values of the config [NOTE: config parser should be given only a line of text]
def parse(config):
    out = dict()

    c = config.split(" ")
    out["minute"] = c[0]
    out["hour"] = c[1]
    out["date"] = c[2]
    out["month"] = c[3]
    out["year"] = c[4]

    out["command"] = c[5]
    i = 6
    while i < len(c):
        out["command"] += " " + c[i]
        i += 1

    return out


# parses and returns the values of the given file
def parseFromFile(filename):
    f = open(filename)
    lines = f.readlines()
    out = []

    for i in lines:
        out.append(parse(i))

    return out
