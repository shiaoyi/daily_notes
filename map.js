arr = [1, 2, 3, 4, 5]

//Way1
// function twice(n) {
// 	return n*n;
// }
// console.log(arr.map(twice));

//Way2 -> 直接把function包在裡面
// console.log(arr.map(function(n){
// 	return n*n;
// }))

//Way3 -> 變arrow function，且變一行時可直接省略return
console.log(arr.map(n => n*n)) //Output: [ 1, 4, 9, 16, 25 ]
