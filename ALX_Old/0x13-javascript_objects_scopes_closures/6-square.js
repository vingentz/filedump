#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let k = 0; k < this.height; k++) {
      let s = '';
      for (let l = 0; l < this.width; l++) {
        s += c;
      }
      console.log(s);
    }
  }
}

module.exports = Square;
