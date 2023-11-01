/**이모티콘
 * https://www.acmicpc.net/problem/14226 */
const S = +require("fs").readFileSync("example.txt").toString().trim();
// const S = +require('fs').readFileSync('/dev/stdin').toString().trim();
const queue = [[1, 0, 0]];
const visited = Array.from({ length: 1001 }, () => Array(1001).fill(false));
while (queue.length > 0) {
  const [screen, board, cnt] = queue.shift();
  if (screen === S) {
    console.log(cnt);
    break;
  }
  if (screen <= 0 || screen > 1000) continue;

  if (board === 0 || !visited[screen][board]) {
    queue.push([screen, board + screen, cnt + 1]);
    visited[screen][board] = true;
  }
  if (screen + board < 1001 && !visited[screen + board][0]) {
    queue.push([screen + board, 0, cnt + 1]);
    visited[screen + board][0] = true;
  }
  if (!visited[screen - 1][board]) {
    queue.push([screen - 1, board, cnt + 1]);
    visited[screen - 1][board] = true;
  }
}
