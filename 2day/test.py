myFile = open("c:\\tmp\\setUp_sec.exe", "rb")
secFile = open("c:\\tmp\\setUp.exe", "wb")

data = myFile.read(1)


while data : 

    result = int.from_bytes(data,byteorder='big') ^ 10

    
    secFile.write( int.to_bytes(result,length=1,byteorder='big') )  


    data = myFile.read(1)


myFile.close()
secFile.close()
