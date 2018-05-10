#prints a funny message when the user types in the exact file name "na na boo boo" 
fname = input("enter the file name: ")
while fname == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd")
    fname = 0
    break
#
try:
    fhand = open(fname)
except:
	print("file not exist:", fname)
	exit()
count = 0
tot_conf = 0.0
for line in fhand:
    line = line.rstrip()
#determine if line has data
    if line.find("X-DSPAM-Confidence:") == -1: continue
#determine number of lines with data
    count = count + 1
    colonpos = line.find(":")
    confidence = line[colonpos+1:]
    tot_conf = tot_conf + float(confidence)
    ave_confidence = tot_conf / count
    #print(count, confidence, tot_conf)
#round(ave_confidence, 11)
#return ave_confidence
print("Ave spam confidence:", round(ave_confidence, 12))
