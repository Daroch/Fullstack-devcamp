let array = [1,2,3,4,5,6,7,8,9];
function extract(array) {
  let array_copy = array.slice();
  for(i=0;i<array.length;i++){
    if(i % 2 == 0){
      console.log(array_copy.shift());
    }else{
      console.log(array_copy.pop());
    }
  }
}
extract(array); 
