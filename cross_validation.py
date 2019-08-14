import sys, os, string

args = sys.argv

fin_features = open(args[1])
fin_labels = open(args[2])
classifierPath = args[3]

feature_list = []
label_list = []

for line in fin_features:
	if not line: break
	line = line.strip()
	if line != '':
		feature_list.append(line)
fin_features.close

for line in fin_labels:
	if not line: break
	line = line.strip()
	if line != '':
		label_list.append(line)
fin_labels.close


overlaps = 0
annotated = 0
labeled = 0

training_size = len(feature_list)

if training_size != len(label_list):
	print 'the numbers of feature lines and label lines are not consistent!'
	exit(0)

fold = 0
while fold < 10:
	#generate testing list
	testing_list = {}
	temp = fold
	while temp < training_size:
		testing_list[temp] = 1
		temp = temp + 10

	fout_feat_train = open('feature_file_training_cv', 'w')
	fout_label_train = open('label_file_training_cv', 'w')
	fout_test = open('file_test_cv', 'w')
	test_annotated = [] 

	i = 0
	while i < training_size:
		if not i in testing_list:
			fout_feat_train.write(feature_list[i]+'\n')
			fout_label_train.write(label_list[i]+'\n')
		else:
			fout_test.write('0 '+feature_list[i]+'\n')
			test_annotated.append(label_list[i])
		i += 1
	fout_feat_train.flush()
	fout_feat_train.close
	fout_label_train.flush()
	fout_label_train.close
	fout_test.flush()
	fout_test.close
	#training
	#os.system("valgrind " + classifierPath+' feature_file_training_cv label_file_training_cv')
	os.system(classifierPath+' feature_file_training_cv label_file_training_cv')

	#testing
	os.system(classifierPath+' -f feature_file_training_cv.weights file_test_cv')
	
	#testing result
	fresult = open('file_test_cv.outputs')
	lineN = 0
	for line in fresult:
		if not line: break
		line = line.strip()
		if line != '':
			score = float(line)
			if score > 0:
				labeled += 1
				if test_annotated[lineN] == '1':
					overlaps += 1
					
			if test_annotated[lineN] == '1':
				annotated += 1
		lineN += 1
	fresult.close

	fold += 1

recall = 0
precision = 0
f = 0
if annotated > 0:
	recall = float(overlaps) / float(annotated)
if labeled > 0:
	precision = float(overlaps) / float(labeled)
if recall > 0 and precision > 0:
	f = 2*recall*precision / (recall+precision)

print 'annotated sarcasms: '+str(annotated)
print 'total sarcasms labeled by the classifiers: '+str(labeled)
print 'correct sarcasms labeled by the classifiers: '+str(overlaps)
print 'recall: '+str(recall)
print 'precision: '+str(precision)
print 'f: '+str(f)
		

