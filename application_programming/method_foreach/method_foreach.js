var numbers = [1,2,3,4,5];
var summ = 0;
numbers.forEach(function(element, index, array){
	array[index] = element* element;
	summ += array[index]
});
console.log(summ);