const prettyPrice = (grossPrice, extension) => {
if (extension>1){extension /=100;}
return Math.floor(grossPrice)+ extension;
}
console.log(prettyPrice(3.40, 99));