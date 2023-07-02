// 배열 합치기
// https://www.acmicpc.net/problem/11728
let input = require('fs').readFileSync('example.txt').toString().split('\n');
// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
let len = input[0].split(' ');
let A = input[1].split(' ').map(x=>Number(x));
let B = input[2].split(' ').map(x=>Number(x));
let arr = [];
let idx_a = 0;
let idx_b = 0;
while (true){
    if (idx_a == len[0]){
        arr = arr.concat(B.slice(idx_b,len[1]));
        break;
    } else if (idx_b == len[1]){
        arr = arr.concat(A.slice(idx_a,len[0]));
        break;
    }
    if (A[idx_a]>B[idx_b]){
        arr.push(B[idx_b]);
        idx_b+=1;
    } else {
        arr.push(A[idx_a]);
        idx_a+=1;
    }
}
console.log(arr.join(' '));