/* 모든순열
 * https://www.acmicpc.net/problem/10974
 */
let input = require('fs').readFileSync('example.txt').toString().trim();
// let input = require('fs').readFileSync('/dev/stdin').toString().trim();
let arr = [];
for (let i=0;i<input;i++){
    arr.push(i+1);
}
const perm = (list, len) => {
    if (len == input){
        console.log(list.join(' '));
        return
    }
    for (let i=0;i<input;i++){
        if (!list.includes(arr[i])){
            list.push(arr[i]);
            perm(list,len+1);
            list.pop();
        }
    }
}

perm([],0);