/** 알파벳
 * https://www.acmicpc.net/problem/1987 */
let input = require("fs").readFileSync("example.txt").toString().split("\n");
// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const [R, C] = input[0].split(' ').map(a => +a);
const board = input.slice(1);
const visited = Array.from({ length: R }, () => Array(C).fill(0));
const used = {};
let ans = 0;
const dir = [[0, 1], [1, 0], [0, -1], [-1, 0]];
const Search = (x, y, cnt) => {
    ans = Math.max(cnt, ans);
    for (let i = 0; i < 4; i++) {
        const dy = y + dir[i][0];
        const dx = x + dir[i][1];
        
        if (dx >= 0 && dy >= 0 && dx < C && dy < R) {
            if (visited[dy][dx] === 0 && !used[board[dy][dx]]) {
                visited[dy][dx] = used[board[dy][dx]] = 1;
                Search(dx, dy, cnt + 1);
                visited[dy][dx] = used[board[dy][dx]] = 0;
            }
        }
    }
}
visited[0][0] = used[board[0][0]] = 1;
Search(0, 0, 1);
console.log(ans);