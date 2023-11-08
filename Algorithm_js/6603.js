/* 로또
 * https://www.acmicpc.net/problem/6603 */
let input = require("fs").readFileSync("example.txt").toString().split("\n");
// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
let i = 0;

const lotto = (arr, cnt) => {
  const results = [];
  if (cnt === 1) return arr.map((value) => [value]);
  arr.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1);
    const combine = lotto(rest, cnt - 1);
    const attached = combine.map((comb) => [fixed, ...comb]);

    results.push(...attached);
  });
  return results;
};

while (input[i] !== "0") {
  const arr = input[i++].split(" ").slice(1);

  const answer = lotto(arr, 6);
  for (const ans of answer) console.log(ans.join(" "));
  console.log();
}
