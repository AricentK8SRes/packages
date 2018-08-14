import netifaces as ni

class Interface(object):
    #def __init__(self):
        #print "inside constructor"

    #ipv6_val = "fd01::99"

    def get_interface_name(self, ipv6_val):
        intList = ni.interfaces()
        intname = ''
        for interface in intList:
            #print "interface name", interface
            find = str(ni.ifaddresses(interface)[10][0]['addr'])
            if find == ipv6_val:
                #print 'method has args', type(ipv6_val), ipv6_val
                #print 'found string in interface', interface, find
                intname = str(interface)
                break
            else:
                #print 'string not found in interface', interface
                continue

        return intname

obj = Interface()

val = "fd01::99"
int = obj.get_interface_name(val)

print int
