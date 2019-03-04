arr = [1, 2, 3, 4, 5]

console.log(
	arr.map(n => n*n)
	   .map(n => n+1)
	   .map(n => n-1)
	   .map(n => Math.sqrt(n))
) //Output: [ 1, 2, 3, 4, 5 ]