import { performance } from 'node:perf_hooks';
import Day01 from './day01';
import Day02 from './day02';

function main() {
	const start = performance.now();
	// const d = new Day01('./notes/day02/part01.txt');
	// const d = new Day01('./notes/day02/part02.txt');
	// const d = new Day01('./notes/day02/part03.txt');
	const d = new Day02('./notes/day02/test.txt');
	console.log(d.part1());
	const end = performance.now();
	console.log(`${(end - start).toFixed(3)}ms`);
}

main();
