let arr = [49, 4, 16, 9, 25];//Задание №1

let result = arr.map(function(elem) {
	return Math.sqrt(elem)
});

console.log(result);


let strin = ['Привет','Hello', 'Hi', 'World', '?'];//Задание №2

strin = strin.map(function(elem) {
	return elem + '!'
});

console.log(strin);


let str = ['Привет','Hello', 'Hi', 'World', '?!'];//Задание №3

result2 = str.map(function(elem) {
	return elem.split('').reverse().join('')
});

console.log(result2);


let arr2 = ['123', '456', '789'];//Задание №4

let finish = arr2.map(function(elem) {
	return elem.split('')
});

console.log(finish);


let arr3 = [1, 2, 3, 4, 5];//Задание №5

let finish2 = arr3.map(function(elem, index) {
	return elem * index;
});

console.log(finish2);