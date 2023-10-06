#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let k = 0; k < size; k++) {
    let row = '';
    for (let j = 0; j < size; j++) row += 'X';
    console.log(row);
  }
}
