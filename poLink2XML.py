#!/usr/bin/python -tt
#https://www.ingress.com/intel?ll=39.946889,116.426838&z=17&pll=39.946889,116.426838



def main():
    fr = open('input', 'r')
    #fw = open('output', 'w')
    print "<?xml version='1.0' encoding='UTF-8'?>\n<kml xmlns='http://www.opengis.net/kml/2.2'>\n<Document>\n<Folder>"
    for line in fr:
        poLink = line
        content = poLink.split('=')
        coordinates = content[-1].split(',')
        print "<Placemark>"
        print "<name>%s,%s</name>" % (coordinates[1], coordinates[0])
        print "<Point>"
        print "<coordinates>%s,%s,0.0</coordinates>" % (coordinates[1], coordinates[0])
        print "</Point>\n</Placemark>"
    print "</Folder>\n</Document>\n</kml>"

if __name__ == '__main__':
    main()

