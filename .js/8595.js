// 히든 넘버
// https://www.acmicpc.net/problem/8595
let input = require('fs').readFileSync('example.txt').toString().split('\n');
// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
let num = input[0];
let str = input[1].split('');
let sum = 0;
let prev = '';
for (let i=0;i<num;i++){
    if (!isNaN(Number(str[i])))
        prev+=str[i];
    else if (isNaN(Number(str[i]))){
        sum+=Number(prev);
        prev = '';
    }
}
if (!isNaN(Number(prev)))
    sum+=Number(prev);
console.log(sum);