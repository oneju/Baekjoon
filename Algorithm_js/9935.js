/* 문자열 폭발 */
/* https://www.acmicpc.net/problem/9935 */
let input = require('fs').readFileSync('example.txt').toString().split('\n');
// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
let str = input[0].split('');
let boom = input[1].split('');
let ans = [];
for (let a of str){
    ans.push(a);
    if (ans.length>=boom.length){
        let flag = 0;
        for (let i=0;i<boom.length;i++){
            if (ans[ans.length-i-1]!=boom[boom.length-i-1]){
                flag=1;
                break;
            }
        }
        if (!flag){
            for (let i=0;i<boom.length;i++){
                ans.pop();
            }
        }
    }
}
if (ans.length>0)
    console.log(ans.join(''));
else
    console.log('FRULA');