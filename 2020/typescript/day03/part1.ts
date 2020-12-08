import { promises as fs } from 'fs';

function countTrees(slope: string[], stepRight: number, stepDown: number) {
  let numTrees = 0;
  let x = stepRight;

  for (let i = stepDown; i < slope.length; i += stepDown, x += stepRight) {
    if (slope[i].charAt(x % slope[0].length) == '#') {
      numTrees++;
    }
  }
  return numTrees;
}

fs.readFile('./input.txt').then((inputBuffer) => {
  const slope = String(inputBuffer).split('\n');

  const num_trees = countTrees(slope, 3, 1);

  console.log(num_trees);
});
