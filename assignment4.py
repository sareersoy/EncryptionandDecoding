import os
import sys
matrixkey=[]
encode = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13,
          "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25,
          "Z": 26, " ": 27, "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11,
          "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23,
          "x": 24, "y": 25, "z": 26, "":0}
decode = {}
for x in encode:
    decode[encode[x]]=x
class Error(Exception):     #bu nest error classım diğerlerini hep bunun içine attım
    pass
class FileEmptyError(Error):
    pass
class PathCouldntFindError(Error):
    pass
class UndefinedParameterError(Error):
    pass
class ParameterNumberError(Error):
    pass
def enc():

    try:

        keyf = open(sys.argv[2], "r",encoding="utf-8")
        if sys.argv[2][-3:] != "txt":  # eğer txt dosyası değilse error veriyorum
            raise PermissionError
        keys=keyf.readlines()
        keyf.close()
        emptyness=0
        for line in keys:
            if " " in line:
                raise ValueError
            if line[-1] == "\n":                            #eğer sonunda \n varsa siliyorum
                line = line[:-1]
                line = line.split(",")
            else:
                line = line.split(",")
            if line != "":
                for el in line:
                    el=int(el)

                emptyness+=1                     # emptyness ile boşluğunu kontrol ediyorum eğer bir şey varsa 1 arttırıyor 0 ise dosya boş hatası geliyor
            else:
                pass
            matrixkey.append(line)
        if not emptyness:
            raise FileEmptyError("Key file is empty error")
    except FileNotFoundError:
        print("Key file not found error")
        sys.exit()
    except PermissionError:
        print("Key file could not be read error")
        sys.exit()
    except FileEmptyError:
        print("Key file is empty error")
        sys.exit()
    except ValueError:
        print("Invalid character in key file error")
        sys.exit()
    input=[]
    try:

        emptyness2 = 0
        inputf=open(sys.argv[3],"r",encoding="utf-8")
        if sys.argv[3][-3:]!="txt":          # burda da eper input dosyam txt değilse error veriyor
            raise PermissionError
        inputs=inputf.readlines()
        inputf.close()
        for line2 in inputs:

            if line2 != "":
                if line2[-1] == "\n":
                    emptyness2+=1
                    line2 = str(line2[:-1])
                else:
                    emptyness2 += 1            #boş olup olmadığını yine bu şekilde kotnrol ediyorum
                    line2 = str(line2)
            else:
                pass
            input.append(str(line2))
        if not emptyness2:
            raise FileEmptyError
        input=[input[i][j] for i in range(len(input)) for j in range(len(input[i]))]
        for i in input:
            assert i in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","\n"]
        inputnumber=[]
        for eleman in input:
            if eleman == "\n":
                pass
            else:
                eleman = encode[eleman]
                inputnumber.append(eleman)
        sep=len(matrixkey[0])
        sepmaxises=[]
        z=0
        y=0
        while y == 0:
            if len(inputnumber)%len(matrixkey)==0:                    #burda inputun boyu keye göre bölüyorum ve keyle uymuyorsa boşluk ekliyorum
                y+=1
                pass
            else:
                inputnumber.append(27)
        for i in range(len(inputnumber)//len(matrixkey)):
            list=[]
            for x in range(len(matrixkey)):
                list.append([inputnumber[z+x]])
            sepmaxises.append(list)
            z+=len(matrixkey)
        data=len(inputnumber)

    except PermissionError:
        print("The input file could not be read error")
        sys.exit()
    except FileEmptyError:
        print("Input file is empty error")
        sys.exit()
    except FileNotFoundError:
        print("Input file not found error")
        sys.exit()
    except AssertionError:
        print("Invalid character in input file error")
        sys.exit()
    except:
        pass
    try:
        all=[]
        if os.path.exists(sys.argv[4]):
            outputf=open(sys.argv[4],"w")
        else:
            raise PathCouldntFindError
        for matrix2 in sepmaxises:
            result = []
            for i in range(sep):
                result.append([0])
            for i in range(len(matrixkey)):
                for j in range(len(matrix2[0])):
                    for k in range(len(matrix2)):

                        if matrix2[k][j] == " ":
                            pass
                        else:
                            result[i][j] += int(matrixkey[i][k]) * int(matrix2[k][j])
            all.append(result)
        count = 0
        for i in all:
            for x in i:
                for a in x:
                    outputf.write(str(a))
                    count += 1
                if count==data:
                    pass
                else:
                    outputf.write(",")
        outputf.close()
    except PermissionError:
        print("Output file could not be written error")
        sys.exit()
    except PathCouldntFindError:
        print("Output file could not be written error")
        sys.exit()
    except:
        pass
""" Burası determinant ve ters matrix için olan kısım"""
def Det(m):
    if len(m[0]) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    if len(m[0]) == 3:
        return (m[0][0]*m[1][1]*m[2][2])+(m[0][1]*m[1][2]*m[2][0])+(m[0][2]*m[1][0]*m[2][1])-(m[0][2]*m[1][1]*m[2][0])-(m[0][0]*m[1][2]*m[2][1])-(m[0][1]*m[1][0]*m[2][2])
def Inverse(m):
    det=Det(m)
    if len(m[0]) == 2:
        return [[m[1][1]/det, (-1)*m[0][1]/det],[(-1)*m[1][0]/det, m[0][0]/det]]
    elif len(m[0]) == 3:
        minor1 = [[m[1][1], m[1][2]], [m[2][1], m[2][2]]]
        minor2 = [[m[0][2], m[0][1]], [m[2][2], m[2][1]]]
        minor3 = [[m[0][1], m[0][2]], [m[1][1], m[1][2]]]
        minor4 = [[m[1][2], m[1][0]], [m[2][2], m[2][0]]]
        minor5 = [[m[0][0], m[0][2]], [m[2][0], m[2][2]]]
        minor6 = [[m[0][2], m[0][0]], [m[1][2], m[1][0]]]
        minor7 = [[m[1][0], m[1][1]], [m[2][0], m[2][1]]]
        minor8 = [[m[0][1], m[0][0]], [m[2][1], m[2][0]]]
        minor9 = [[m[0][0], m[0][1]], [m[1][0], m[1][1]]]
        return [[Det(minor1)/det,Det(minor2)/det,Det(minor3)/det],[Det(minor4)/det,Det(minor5)/det,Det(minor6)/det],[Det(minor7)/det,Det(minor8)/det,Det(minor9)/det]]
declines=[]
decvalues=[]
def dec():
    try:

        if os.path.exists(sys.argv[3]):
            inputf = open(sys.argv[3], "r",encoding="utf-8")
            if sys.argv[3][-3:] != "txt":
                raise PermissionError
            lines = inputf.readlines()
            emptyness = 0
            for line in lines:
                if line[-1] == "\n":
                    line = line[:-1]
                    line = line.split(",")                       #burda yine keye göre bölme işlemleri
                else:
                    line = line.split(",")

                if line != "":
                    for el in line:
                        el = int(el)

                    emptyness += 1
                else:
                    pass
                declines.append(line)
            if not emptyness:
                raise FileEmptyError("Key file is empty error")
        else:
            raise PathCouldntFindError
        inputf.close()
    except PathCouldntFindError:
        print("Input file not found error")
        sys.exit()
    except PermissionError:
        print("The input file could not be read error")
        sys.exit()
    except FileEmptyError:
        print("Input file is empty error")
        sys.exit()
    except ValueError:
        print("Invalid character in input file error")
        sys.exit()
    except:
        pass
    try:

        keyf = open(sys.argv[2], "r",encoding="utf-8")
        if sys.argv[2][-3:]!="txt":
            raise PermissionError
        keys=keyf.readlines()
        keyf.close()
        emptyness=0
        for line in keys:
            if " " in line:
                raise ValueError
            if line[-1] == "\n":
                line = line[:-1]
                line = line.split(",")
            else:
                line = line.split(",")
            if line != "":
                for el in line:
                    el=int(el)
                emptyness+=1
            else:
                pass
            matrixkey.append(line)
        if not emptyness:
            raise FileEmptyError("Key file is empty error")
    except FileNotFoundError:
        print("Key file not found")
        sys.exit()
    except PermissionError:
        print("Key file could not be read error")
        sys.exit()
    except FileEmptyError:
        print("Key file is empty error")
        sys.exit()
    except ValueError:
        print("Invalid character in key file error")
        sys.exit()
    except:
        pass
    try:
        matrixdec=[]
        sepvalues=[]
        sep = len(matrixkey[0])
        for x in matrixkey:
            d1=[]
            for y in x:
                d1.append(int(y))
            matrixdec.append(d1)
        Inversematrix=Inverse(matrixdec)
        for i in declines[0]:
            decvalues.append(int(i))
        z=0
        for i in range(len(decvalues) // len(matrixkey)):
            list = []
            for x in range(len(matrixkey)):
                list.append([decvalues[z + x]])
            sepvalues.append(list)
            z += len(matrixkey)
    except:
        pass
    try:
        all=[]
        if os.path.exists(sys.argv[4]):
            outputf=open(sys.argv[4],"w")
        else:
            raise PathCouldntFindError
        for matrix2 in sepvalues:
            result = []
            for i in range(sep):
                result.append([0])
            for i in range(len(Inversematrix)):
                for j in range(len(matrix2[0])):
                    for k in range(len(matrix2)):
                        result[i][j] += int(Inversematrix[i][k]) * int(matrix2[k][j])
            all.append(result)
        all2=[]
        for a in all:
            for b in a:
                all2.append(decode[b[0]])
        for i in all2:
                outputf.write(i)
    except PermissionError:
        print("Output file could not be written error")
        sys.exit()
    except PathCouldntFindError:
        print("Output file could not be written error")
        sys.exit()
    finally:
        outputf.close()
try:
    argvcount = len(sys.argv)
    if argvcount != 5:                     #burası da eğer 2. parametre enc dec değilse veya 5ten farklı sayıda parametre girildiyse hata veriyor
        raise ParameterNumberError
    x=sys.argv[1]
    if x=="enc":
        enc()
    elif x=="dec":
        dec()
    if x not in ["enc","dec"]:
        raise UndefinedParameterError


except UndefinedParameterError:
    print("Undefined parameter error")
    sys.exit()
except ParameterNumberError:
    print("Parameter number error")
    sys.exit()
