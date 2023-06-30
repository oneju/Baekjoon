// 8진수, 10진수, 16진수
// https://www.acmicpc.net/problem/11816
// let input = require('fs').readFileSync('example.txt').toString().trim();
let input = require('fs').readFileSync('/dev/stdin').toString().trim();
let num = 0
if (input[0]=='0'){
    if (input[1]=='x'){
        num = input.substring(2);
        console.log(parseInt(num,16));
    }
    else{
        num = input.substring(1);
        console.log(parseInt(num,8));
    }
}
else{
    num = input;
    console.log(num);
}