##
## Written by Jonathan Klaric
## (c) 2019 Innovyze Australia
##
## ABSOLUTELY No guarantee or warranty is given
## as to quality or accuracy of this script.
## No responsibility is taken for any data or file loss
## as a result of using this code.
##
## All usage is at user's risk.
## 
## Good luck, and God speed.
##

def RoundASCfile(ascFilepath,decimals2round2):
    ## takes an asc file and the number of decimals to round the data to as arguments
    ## creates a new file with _rounded at the same location
    outputFilepath = ascFilepath[:ascFilepath.find('.asc')]+'_rounded.asc'
    data = []
    f = open(ascFilepath,'r')
    for line in f:
        data.append(line)
    f.close()
    outputFile = open(outputFilepath,'w')
    for i in range(0,len(data)):
        if i < 6:
            lineToWrite = data[i]
        else:
            dataline = data[i].strip('\n')
            dataline = dataline.split(' ')
            for j in range(0,len(dataline)):
                if dataline[j] != '':
                    dataline[j] = str(round(float(dataline[j]),decimals2round2))
            lineToWrite = ' '.join(dataline)+'\n'
        outputFile.write(lineToWrite)
    outputFile.close()
    print(outputFilepath+' created and written.')
    return

# filepath as a string - REMEMBER the double backslashes!
andrewsASCFile = 'C:\\Users\\jonathan.klaric\\Downloads\\e337n5820_melbourne_2017nov28_dtm1m_v10cm_mga55.asc'
RoundASCfile(andrewsASCFile,6)
