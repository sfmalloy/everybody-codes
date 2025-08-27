import * as q1 from './quests/quest1.js';
import * as q2 from './quests/quest2.js';
import * as q3 from './quests/quest3.js';
import { performance } from 'perf_hooks';
import { styleText } from 'util';

function main() {
	runQuest(q1, 1);
	runQuest(q2, 2);
	runQuest(q3, 3);
}

function runQuest(q, num) {
	const start = performance.now();
	const p1 = q.part1();
	const p2 = q.part2();
	const p3 = q.part3();
	const end = performance.now();

	print(styleText(['underline', 'bold', 'redBright'], `Quest ${num}`));
	print(styleText('green', 'Part 1:'), ` ${p1}`);
	print(styleText('green', 'Part 2:'), ` ${p2}`);
	print(styleText('green', 'Part 3:'), ` ${p3}`);
	print(styleText('yellow', 'Runtime:'), `${(end - start).toFixed(3)}ms\n`);
}

function print(...data) {
	console.log(...data);
}

main();
