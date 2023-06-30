// 소인수분해
// https://www.acmicpc.net/problem/11653
var input = require('fs').readFileSync('example.txt').toString().trim();
// var input = require('fs').readFileSync('/dev/stdin').toString().trim();
var n = input; 
for (let i=2;i<=n;i++){
    if (n==1) break;
    while (n%i==0){
        console.log(i);
        n/=i;
    }
};