import sys, os, string

args = sys.argv

fin = open(args[1])#config file

fou_features = open(args[2], 'w')#output the integrated features

if not os.path.exists('feature_indexes'):
	#os.system('mkdir feature_indexes')
	print 'feature indexing files are not found!'

featureInsts = []


lineN = 0
for line in fin:
	if not line: break
	line = line.strip()
	if line != '':
		lineV = line.split('\t')
		featureName = lineV[0]

		featureIndex = {}
		fin_featIndex = open('feature_indexes/'+featureName)		
		for linec in fin_featIndex:
			if not linec: break
			linec = linec.strip()
			if linec != '':
				linecV = linec.split('\t')
				featureIndex[linecV[0]] = linecV[1]
		fin_featIndex.close
		

		featureF = open(lineV[1])
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
					if cfeat in featureIndex:
						featureInd = featureIndex[cfeat]					
						featStr += str(featureInd)+':'+eleV[1]+' '
				featStr = featStr.strip()
				if lineN == 0:
					featureInsts.append(featStr)
				else:
					featureInsts[linecN] += ' '+featStr
				linecN += 1							
		
		lineN += 1
for ele in featureInsts:
	fou_features.write('0 '+ele+'\n')
fou_features.flush()
fou_features.close

		
	
