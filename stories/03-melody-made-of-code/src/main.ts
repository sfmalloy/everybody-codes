import { performance } from 'node:perf_hooks';
import Day01 from './day01';

function main() {
	const start = performance.now();
	const d = new Day01('./notes/day01/part03.txt');
	console.log(d.part3());
	const end = performance.now();
	console.log(`${(end - start).toFixed(3)}ms`);
}

main();
