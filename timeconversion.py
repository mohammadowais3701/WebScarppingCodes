s="12:45:22AM"
s = s.split(':')
formats = s[2][2:]
if formats == 'PM':
    if s[0] != '12':
        s[0] = int(s[0]) + 12

        s[0] %= 24

elif (s[0] == '12' and formats == 'AM'):
    print('hh')
    s[0] = '00'
newTime = str(s[0]) + ":" + str(s[1]) + ":" + str(s[2][0:2])
print(newTime)