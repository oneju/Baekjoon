// 대칭 차집합
// https://www.acmicpc.net/problem/1269
let input = require('fs').readFileSync('example.txt').toString().split('\n');
// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
let len = input[0].split(' ');
let A = input[1].split(' ');
let B = input[2].split(' ');
let arr = new Set(A.concat(B));
let ans = 2*arr.size - (Number(len[0])+Number(len[1]));
// arr.size - Number(len[0]) + arr.size - Number(len[1]) - 2
console.log(ans);