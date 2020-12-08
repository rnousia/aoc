import { promises as fs } from 'fs';

fs.readFile('./input.txt').then((inputBuffer) => {
  const expenses = String(inputBuffer)
    .split('\n')
    .map((item) => parseInt(item));

  expenses.forEach((expense1, i) => {
    expenses.forEach((expense2, j) => {
      if ((i != j && expense1 + expense2) == 2020)
        console.log(expense1 * expense2);
    });
  });
});
