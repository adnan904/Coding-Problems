# Returns number of pairs in arr[0..n-1] with sum equal to 'sum'
from collections import defaultdict

def getPairsCount(arr, n, sum):
	m = defaultdict(int)

	# Store counts of all elements in map m
	for i in range(0, n):
		m[arr[i]] += 1

	twice_count = 0

	for i in range(0, n):
		test = m[sum - arr[i]]
		twice_count += m[sum - arr[i]]

	return int(twice_count)


if __name__ == '__main__':
	arr = [1,3,-2,8,5]
	n = len(arr)
	sum = 6
	print("Count of pairs is", getPairsCount(arr,n, sum))

