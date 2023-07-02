// 숫자의 합
// https://www.acmicpc.net/problem/11720
// let input = require('fs').readFileSync('example.txt').toString().split('\n');
let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
let n = input[0]; 
let n_lst = input[1].split(''); 
let sum = 0;
for (let i=0;i<n;i++){
    sum+=Number(n_lst[i]);
}
console.log(sum);