
def replace1():
    f = open('workfile', 'r')
    r = open('replace1', 'w')

    for line in f:
        if len(line) > 3:
            line = line.replace("ago0x", ";")
            line = line.replace("0x", "\n")
            r.write(line)

def replace2():
    f = open('replace1', 'r')
    r = open('replace2', 'w')

    dict = {}
    for line in f:
        if len(line) > 3:
            line = line.replace("  IN   EOSCrowdsale", ";")
            line = line.replace(" Ether", ";")
            line = line.replace(",", "")
            if not dict.__contains__("line[0:64]"):
                r.write(line[0:64] +";" + line[64:71] + ";"  +line[71:])
                dict[line[0:64]] = line[0:64]
            else:
                print(line[0:64])

replace2()