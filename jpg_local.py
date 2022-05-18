import exifread
f = open('ns.jpg','rb')
imageinfo = exifread.process_file(f)

for key in imageinfo:
    print(key,":",imageinfo[key])
print("+++++++++++++++++\n++++++++++++++++")
for q in imageinfo:
    if q=="GPS GPSLongitude":
        print("GPS经度=",imageinfo[q],imageinfo['GPS GPSLatitudeRef'])
    elif q=="GPS GPSLatitudeRef":
        print("GPS维度=",imageinfo[q],imageinfo['GPS GPSLongitude'])
    if q=="Image DateTime":
        print("拍摄时间：",imageinfo[q])