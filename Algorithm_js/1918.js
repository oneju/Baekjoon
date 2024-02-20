/** 후위 표기식
 * https://www.acmicpc.net/problem/1918 */
let input = require("fs").readFileSync("example.txt").toString().trim().split('');
// let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('');
let postfix = '';
const oper = ['+','-','*','/','(',')'];
const stack = [];

for (const i of input) {
    const isOper = oper.indexOf(i);
    if (isOper < 0) postfix+=i;
    else {
        if (isOper === 5) {
            let idx = 5;
            while (idx !== 4) {
                idx = stack.pop();
                if (idx === 4) break;
                postfix+=oper[idx];
            }
            continue;
        }
        if (stack.length>0 && isOper < 4) {
            for (let j = stack.length - 1; j >= 0; j--){
                if (stack[j] === 4 || ~~(stack[j] / 2) < ~~(isOper / 2)) break;
                postfix += oper[stack.pop()];
            }
        }
        stack.push(isOper);
    }
}
while (stack.length > 0) {
    postfix += oper[stack.pop()];
}
console.log(postfix);