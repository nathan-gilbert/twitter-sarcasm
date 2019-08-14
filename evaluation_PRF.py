import sys, os, string

args = sys.argv

fin_gold = open(args[1])
fin_test = open(args[2])

gold_labels = []
positive_gold = 0
for line in fin_gold:
	if not line: break
	line = line.strip()
	if line != '':
		gold_labels.append(line)
		if line == 'SARCASM':
			positive_gold += 1
fin_gold.close

lineN = 0
positive_test = 0
positive_overlap = 0
for line in fin_test:
	if not line: break
	line = line.strip()
	if line != '':
		score = float(line) 
		if score > 0:
			positive_test += 1
			if gold_labels[lineN] == 'SARCASM':
				positive_overlap += 1
	lineN += 1
fin_test.close

print 'positive_gold: '+str(positive_gold)
print 'positive_test: '+str(positive_test)

recall = float(positive_overlap) / float(positive_gold)
precision = float(positive_overlap) / float(positive_test)

f = 0
if recall != 0 and precision != 0:
	f = 2*recall *precision / (recall+precision)

print 'recall: '+str(recall)
print 'precision: '+str(precision)
print 'f: '+str(f)
