arr = [1, 2, 3, 4, 5]

console.log(
	arr.filter(function(n)({
		return n % 2 
	}))
) // Output: [1, 3, 5]

//也可以寫成
//console.log(arr.filter(n => n % 2 )) 