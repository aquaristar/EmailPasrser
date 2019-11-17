import sys
import re

inputFile="email_contacts.mbox"
#inputFile="test_input.txt"
outputFile="result3.csv"
content = ""

def writeFile(content, file, append=False):
    if(append is True):
        fout = open(file, 'ab')
    else:
        fout = open(file, 'wb')
    fout.write(content)
    fout.close()

def readFile(file):
	try:
		f = open(file, 'r+')
		lines = f.readlines()

		if(len(lines)<1):
			print (":::ERROR::: empty file.")
			return False

		global content
		csvline = ""
		e_flag = False
		f_flag = False
		l_flag = False
		for line in lines:			
			if ("email:" in line) and ("@" in line):
				match = re.findall(r'[\w\.-]+@[\w\.-]+', line)
				e_flag = True
				if len(match) == 0:
					e_flag = False
					f_flag = False
					l_flag = False
					continue			
				
			if "namefirst: " in line:
				f_flag = True
				nf = line.split("namefirst: ")
				if len(nf) == 0:
					namefirst = ""
				if len(nf) > 1:
					namefirst = re.sub('<[^>]*>', '', nf[1]).rstrip("\n")

			if "namelast:" in line:
				l_flag = True
				nl = line.split("namelast: ")
				if len(nl) == 0:
					namelast = ""
				if len(nl) > 1:
					namelast = re.sub('<[^>]*>', '', nl[1]).rstrip("\n")

			if e_flag and f_flag and l_flag:
				content += namefirst + "," + namelast + "," + match[0] + "\n"
				e_flag = False
				f_flag = False
				l_flag = False

		for line in lines:			
			if ("Email:" in line) and ("@" in line):
				match = re.findall(r'[\w\.-]+@[\w\.-]+', line)
				e_flag = True
				if len(match) == 0:
					e_flag = False
					f_flag = False
					l_flag = False
					continue			
				
			if "Name: " in line:
				f_flag = True
				nf = line.split("namefirst: ")
				if len(nf) == 0:
					namefirst = ""
				if len(nf) > 1:
					namefirst = re.sub('<[^>]*>', '', nf[1]).rstrip("\n")

			if "namelast:" in line:
				l_flag = True
				nl = line.split("namelast: ")
				if len(nl) == 0:
					namelast = ""
				if len(nl) > 1:
					namelast = re.sub('<[^>]*>', '', nl[1]).rstrip("\n")

			if e_flag and f_flag and l_flag:
				content += namefirst + "," + namelast + "," + match[0] + "\n"
				e_flag = False
				f_flag = False
				l_flag = False

		f.closed
		return True

	except Exception as e:
		print e
    	return False	


#===================== Start Program ======================#
#set arguments
# if (len(sys.argv) > 1):
#     for index in range(len(sys.argv)):
# 	    if(sys.argv[index] == '-i'):
# 	        inputFile = sys.argv[index+1]
# 	    elif(sys.argv[index] == '-o'):
# 	        outputFile = sys.argv[index+1]
if(readFile(inputFile)==False):
	exit()
		
writeFile(content, outputFile)

print ":::INFO::: successfully completed!!!"