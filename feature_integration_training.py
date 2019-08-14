import sys, os, string

args = sys.argv

fin = open(args[1])#config file

fou_features = open(args[2], 'w')#output the integrated features

if not os.path.exists('feature_indexes'):
	os.system('mkdir feature_indexes')

featureInsts = []

featureInd = 0
lineN = 0
for line in fin:
	if line.startswith('#'):
		continue
	if not line: break
	line = line.strip()
	
	if line != '':
		
		lineV = line.split('\t')
		featureName = lineV[0]
		featureF = open(lineV[1])
		featureIndex = {}
		print featureInd
		for linec in featureF:
			if not linec: break
			linec = linec.strip()
			if linec != '':
				linecV = linec.split()
				for ele in linecV:
					eleV = ele.split(':')
					cfeat = eleV[0]
					if not cfeat in featureIndex:
						#print cfeat
						featureInd += 1
						featureIndex[cfeat] = featureInd
		print featureInd
		print "-----------"
		

		#save featureIndex
		feats = featureIndex.keys()
		fou_featIndex = open('feature_indexes/'+featureName, 'w')
		for ele in feats:
			fou_featIndex.write(ele+'\t'+str(featureIndex[ele])+'\n')
		fou_featIndex.flush()
		fou_featIndex.close

		featureF.seek(0)
		linecN = 0
		for linec in featureF:
			if not linec: break
			linec = linec.strip()
			if linec != '':
				featStr = ''
				linecV = linec.split()
				for ele in linecV:
					eleV = ele.split(':')
					cfeat = eleV[0]
					#featureInd = featureIndex[cfeat]
					#featStr += str(featureInd)+':'+eleV[1]+' '
					featureIndTemp = featureIndex[cfeat]
					featStr += str(featureIndTemp)+':'+eleV[1]+' '
				featStr = featStr.strip()
				#if linecN == 0:
				if lineN == 0:
					featureInsts.append(featStr)
				else:
					featureInsts[linecN] += ' '+featStr
				linecN += 1							
		
		lineN += 1
		
for ele in featureInsts:
	fou_features.write(ele+'\n')
fou_features.flush()
fou_features.close

		
	
