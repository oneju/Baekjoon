// 블랙잭
// https://www.acmicpc.net/problem/2798
let input = require('fs').readFileSync('example.txt').toString().split('\n');
// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
let N = input[0].split(' ')[0];
let M = input[0].split(' ')[1];
let cards = input[1].split(' ').map(x=>Number(x));
let ans = 0;
for (let i=0;i<N;i++){
    for (let j=i+1;j<N;j++){
        for (let k=j+1;k<N;k++){
            let sum = cards[i]+cards[j]+cards[k];
            if (sum > ans && sum <= M){
                ans = sum;
            }
        }
    }
    if (ans==N)
        break;
}
console.log(ans);