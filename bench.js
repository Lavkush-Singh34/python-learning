// bench.js
// let total = 0;
//
// for (let i = 1; i <= 100000000; i++) {
//     total += i * i;
// }
//
// console.log(total);


let total = 0n;

for (let i = 1n; i <= 100000n; i++) {
      total += i * i;
}

console.log(total.toString());

