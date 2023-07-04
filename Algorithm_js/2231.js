/* 분해합 */
/* https://www.acmicpc.net/problem/2231 */
let input = require('fs').readFileSync('example.txt').toString();
// let input = require('fs').readFileSync('/dev/stdin').toString();
let len = input.length;
let N = Number(input);
let flag = 0;
for (let num = 1;num<N;num++){
    let check = num;
    let a = String(num);
    for (let i=0;i<len;i++){
        check+=Number(a.charAt(i));
    }
    if (check == N) {
        console.log(num);
        flag = 1;
        break;
    }
}
if (flag===0){
    console.log(0);
}