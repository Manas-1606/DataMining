import math
import csv

# reads the data and returns a list of all rows
def readData(filename):
	reader = csv.reader(open(filename, 'r'))
	transactions = []
	for row in reader:
		transactions.append(row)
	print ("Transactions: ", transactions)
	return transactions


#calculates info(D)
def gain_category(col, dataset):
	total = list(row[col] for row in dataset)
	len_total = len(total)

	att_dict = {}

	#counts the number of occurences of the particular attribute
	for i in total:
		if i in att_dict:
			att_dict[i] += 1
		else:
			att_dict[i] = 1

	gain = 0
	for i in att_dict.keys():

		# calculating p = no. of occurence/ total rows
		p = (att_dict[i] / float(len_total))

		# gain = p * log(p)
		gain += -p * math.log(p, 2)

	return gain


#calculates info_a(D)
def gain_attribute_category(col, dataset):
	gain = 0
	p = 0
	classes = list(set(row[col] for row in dataset))
	for i in classes:
		len_total = len(dataset)
		new_dataset = [row for row in dataset if i == row[col]]
		new_len_total = len(new_dataset)
		p += (new_len_total / float(len_total)) * gain_category(len(dataset[0]) - 1, new_dataset)

	return p


# Select the best split point for a dataset
def split_attribute(dataset):
	# get list of classes
	# use set to make remove redundant

	# dataset[0] is attribute value
    
	classes = list(set(row[-1] for row in dataset[1:]))

	info_gain = gain_category(3, dataset[1:])
	# print("info_gain: ",info_gain)

	best_gain = 0
	for col in range(len(dataset[0]) - 1):
		# Get gain for this new subdataset
		gainA = gain_attribute_category(col, dataset[1:])

		#gain(A)
		dgain = info_gain - gainA

		# if new gainA is better then update and also in case we need inital update
		if dgain > best_gain or best_gain == 0:
			b_col, best_gain = col, dgain

	# print(dataset[0][b_col])

	links = list(set(val[b_col] for val in dataset[1:]))
	ret = {}
	for i in links:
		ret[i] = [dataset[0]] + [row for row in dataset if i == row[b_col]]

	return {'b_col': b_col, 'best_gain': best_gain, 'data': ret}


# check if sub_dataset contains only one label then prune
def prune(sub_dataset):
	outcomes = [row[-1] for row in sub_dataset[1:]]
	max_val = max(set(outcomes), key=outcomes.count)

	for i in sub_dataset[1:]:

		if i[-1] != max_val:
			return False
	return True


# Create a terminal node value
def to_terminal(sub_dataset):
	outcomes = [row[-1] for row in sub_dataset[1:]]
	return max(set(outcomes), key=outcomes.count)



#final split of decision tree, where pruning is done
def split(node, max_depth, min_size, depth):
	ret = node['data']
	# remove the key:value
	del (node['data'])

	for i in ret.keys():

		check = prune(ret[i])

		if check:
			node[i] = to_terminal(ret[i])
			continue

		if depth >= max_depth:
			node[i] = to_terminal(ret[i])
			continue

		if len(ret[i]) <= min_size:
			node[i] = to_terminal(ret[i])
		else:
			node[i] = split_attribute(ret[i])
			split(node[i], max_depth, min_size, depth + 1)


def create_tree(data):
	root = split_attribute(data)
	split(root, 4, 1, 1)

	return root


def print_tree(root, n=1):
	print(root)
	

#data is a list of all rows
data = readData("3-dataset.csv")

# print(split_Attribute(data))
# print(to_terminal(data))

root = create_tree(data)
# print(root)

print_tree(root)