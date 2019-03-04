// Eg1
const obj = {
	score: 60,
	name: 'hello',
	location: 'Taiwan',
	city: 'Taipei'
}

const { score, name, ...rest1 } = obj;
console.log(rest1) // output: { location: 'Taiwan', city: 'Taipei' }

//Eg2
const [first, ...rest2] = [1, 2, 3, 4, 5]
console.log(rest2) // output: [ 2, 3, 4, 5 ]