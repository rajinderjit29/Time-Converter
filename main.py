def converter(str1):
    if (str1 [-2:] == 'AM' and str1 [0:2] == "12"):
        return ("00" + str1 [2: -2])
    elif (str1 [-2:] == 'AM'):
        return (str1 [0:-2])
    elif (str1 [0:2] == '12' and str1 [-2:] == "PM"):
        return (str1 [0: -2])
    elif (str1 [-2:] == 'PM'):
        return str(int(str1[0:2])+12)+str1[2:-2]
    else:
        return ("Something went wrong")
a = input ("Enter time in the format hh:mm:ss AM or PM")
output = converter(a)
print (output)