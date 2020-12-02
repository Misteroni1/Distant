let arr = [-1, 0, 1, 2, 3]; // №1

let result = arr.filter(function(elem) {
	if (elem > 0) {
		return true;
	} else {
		return false;
	}
});

console.log(result);


let arr2 = [-2, -1, 0, 1, 2, 3]; // №2

let result2 = arr2.filter(function(elem) {
	if (elem < 0) {
		return true;
	} else {
		return false;
	}
});

console.log(result2);


let arr3 = [-1, 0, 1, 2, 3, 9, 10, 100]; // №3

let result3 = arr3.filter(function(elem) {
	if (elem > 0  && elem < 10) {
		return true;
	} else {
		return false;
	}
});

console.log(result3);


let arr4 = ['Hello!', 'Word', '12', 'Example', 'Two']; // №4

let result4 = arr4.filter(function(elem){
	if(elem.length > 5) {
		return true;
	} else {
		return false;
	}
});

console.log(result4);


let arr7 = [-1, 0, 1, 2, 3, 9, 10, 100]; // №5

let result7 = arr7.filter(function(elem, index) {
	if ((elem * index) < 30) {
		return true;
	} else {
		return false;
	}
});

console.log(result7);


let arr5 = [1, 3, 1000, [6, 9], 25, [2, 5]]; // №6

let result5 = arr5.filter(function(elem){
	if(Array.isArray(elem)) {
		return false;
	} else {
		return true;
	}
});

console.log(result5);


let arr6 = [-1, -25, -1423, 2, -3, 3, 4, 5]; // №7

let result6 = arr6.filter(function(elem){
	if(elem < 0 ) {
		return true;
	} else {
		return false;
	}
});

console.log(result6.length);

