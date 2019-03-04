arr = [6, 5, 4, 3, 2, 1]

console.log(arr.reduce(function(total,value){
	return total + value;
}, 0))


// arr[0] 6 => total: 0, value: 6, return => 6
// arr[1] 5 => total: 6, value: 5, return => 11
// arr[2] 4 => total: 11, value: 4, return => 15
// arr[3] 3 => total: 15, value: 3, return => 18
// arr[4] 2 => total: 18, value: 2, return => 20
// arr[5] 1 => total: 20, value: 1, return => 21

