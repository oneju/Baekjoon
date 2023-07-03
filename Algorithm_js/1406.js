/* 에디터 */
/* https://www.acmicpc.net/problem/1406 */
let input = require('fs').readFileSync('example.txt').toString().split('\n');
// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
let word = input[0].split('');
let M = Number(input[1]);

let s1 = word;
let s2 = [];

function editor (comm) {
    if (comm == 'L' && s1.length>0)
        s2.push(s1.pop());
        
    else if (comm == 'D' && s2.length>0)
        s1.push(s2.pop());

    else if (comm == 'B')
        if (s1.length > 0) s1.pop();

    else if (comm[0] == 'P'){
        let str = comm.split(' ')[1];
        s1.push(str);
    }
};
for (let i=0;i<M;i++){
    editor(input[i+2]);
}
s2.reverse();
console.log(s1.join('')+s2.join(''));