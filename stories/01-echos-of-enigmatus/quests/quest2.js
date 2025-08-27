import { readFileSync } from 'node:fs';

class Node {
	/**
	 * @param {number} rank
	 * @param {string} symbol
	 * @param {number | undefined} id
	 */
	constructor(rank, symbol, id) {
		this.rank = rank;
		this.symbol = symbol;
		this.left = null;
		this.right = null;
		this.id = id;
		this.parent = null;
	}

	/**
	 * Compare other node and insert on right or left depending on its rank
	 * @param {Node} other node to insert
	 */
	add(other) {
		if (other.rank < this.rank) {
			if (!this.left) {
				this.left = other;
				other.parent = this;
			} else {
				this.left.add(other);
			}
		} else {
			if (!this.right) {
				this.right = other;
				other.parent = this;
			} else {
				this.right.add(other);
			}
		}
	}

	/**
	 * @param {Node} other
	 */
	swap(other) {
		let id = this.id;
		let rank = this.rank;
		let symbol = this.symbol;

		this.id = other.id;
		this.rank = other.rank;
		this.symbol = other.symbol;

		other.id = id;
		other.rank = rank;
		other.symbol = symbol;
	}

	treeSwap(other) {
		if (this.parent && this.parent.left === this) {
			this.parent.left = other;
		} else if (this.parent && this.parent.right === this) {
			this.parent.right = other;
		}

		if (other.parent && other.parent.left === other) {
			other.parent.left = this;
		} else if (other.parent && other.parent.right === other) {
			other.parent.right = this;
		}

		let thisParent = this.parent;
		this.parent = other.parent;
		other.parent = thisParent;
	}

	find(id, ignore) {
		if (this.id === id && this !== ignore) {
			return this;
		}
		return this.left?.find(id, ignore) || this.right?.find(id, ignore);
	}

	/**
	 * Sorts nodes into groups by level
	 * @param {Node[][]} nodes node map by level
	 * @param {number} level current level of the tree
	 * @returns node map group by level
	 */
	getLevels(nodes = undefined, level = 0) {
		if (!nodes) {
			nodes = [];
		}
		while (nodes.length <= level) {
			nodes.push([]);
		}
		nodes[level].push(this);
		if (this.left) {
			nodes = this.left.getLevels(nodes, level + 1);
		}
		if (this.right) {
			nodes = this.right.getLevels(nodes, level + 1);
		}
		return nodes;
	}

	static getMaxNodes(levelNodes) {
		let res = [];
		let max = 0;
		for (let i = 0; i < levelNodes.length; ++i) {
			const L = levelNodes[i].length;
			if (L > max) {
				res = [...levelNodes[i]];
				max = L;
			}
		}
		return res;
	}
}

export function part1() {
	let inputNodes = readFileSync('inputs/quest2/part1.in')
		.toString()
		.trim()
		.split('\n')
		.map((line) => [
			[...line.match(/left=\[(\d+),([^\]]+)\]/).values()].slice(1),
			[...line.match(/right=\[(\d+),([^\]])\]/).values()].slice(1),
		])
		.map(([[leftRank, leftSymbol], [rightRank, rightSymbol]]) => [
			new Node(parseInt(leftRank), leftSymbol),
			new Node(parseInt(rightRank), rightSymbol),
		]);
	let [left, right] = inputNodes[0];
	inputNodes.slice(1).forEach(([l, r]) => {
		left.add(l);
		right.add(r);
	});
	return (
		Node.getMaxNodes(left.getLevels())
			.map((elem) => elem.symbol)
			.join('') +
		Node.getMaxNodes(right.getLevels())
			.map((elem) => elem.symbol)
			.join('')
	);
}

export function part2() {
	const lines = readFileSync('inputs/quest2/part2.in')
		.toString()
		.trim()
		.split('\n');
	let parsedLines = lines
		.map((line) => {
			if (line.startsWith('ADD')) {
				return [
					'ADD',
					line.match(/id=(\d+)/)[1],
					[...line.match(/left=\[(\d+),([^\]]+)\]/).values()].slice(1),
					[...line.match(/right=\[(\d+),([^\]])\]/).values()].slice(1),
				];
			}
			return ['SWAP', line.match(/(\d+)/)[1]];
		})
		.map(([ins, ...rest]) => {
			if (ins === 'ADD') {
				const [id, [leftRank, leftSymbol], [rightRank, rightSymbol]] = rest;
				return [
					'ADD',
					new Node(parseInt(leftRank), leftSymbol, parseInt(id)),
					new Node(parseInt(rightRank), rightSymbol, parseInt(id)),
				];
			}
			return ['SWAP', parseInt(rest)];
		});

	let left = null;
	let right = null;
	for (let [ins, ...rest] of parsedLines) {
		if (ins === 'ADD') {
			if (!left) {
				left = rest[0];
				right = rest[1];
			} else {
				left.add(rest[0]);
				right.add(rest[1]);
			}
		} else {
			const id = rest[0];
			left.find(id).swap(right.find(id));
		}
	}

	return (
		Node.getMaxNodes(left.getLevels())
			.map((elem) => elem.symbol)
			.join('') +
		Node.getMaxNodes(right.getLevels())
			.map((elem) => elem.symbol)
			.join('')
	);
}

export function part3() {
	const lines = readFileSync('inputs/quest2/part3.in')
		.toString()
		.trim()
		.split('\n');
	let parsedLines = lines
		.map((line) => {
			if (line.startsWith('ADD')) {
				return [
					'ADD',
					line.match(/id=(\d+)/)[1],
					[...line.match(/left=\[(\d+),([^\]]+)\]/).values()].slice(1),
					[...line.match(/right=\[(\d+),([^\]])\]/).values()].slice(1),
				];
			}
			return ['SWAP', line.match(/(\d+)/)[1]];
		})
		.map(([ins, ...rest]) => {
			if (ins === 'ADD') {
				const [id, [leftRank, leftSymbol], [rightRank, rightSymbol]] = rest;
				return [
					'ADD',
					new Node(parseInt(leftRank), leftSymbol, parseInt(id)),
					new Node(parseInt(rightRank), rightSymbol, parseInt(id)),
				];
			}
			return ['SWAP', parseInt(rest)];
		});

	let left = null;
	let right = null;
	for (let [ins, ...rest] of parsedLines) {
		if (ins === 'ADD') {
			if (!left) {
				left = rest[0];
				right = rest[1];
			} else {
				left.add(rest[0]);
				right.add(rest[1]);
			}
		} else {
			const id = rest[0];
			if (id === 1) {
				let tmp = left;
				left = right;
				right = tmp;
			} else {
				let a = left.find(id);
				if (!a) {
					a = right.find(id);
				}
				let b = left.find(id, a);
				if (!b) {
					b = right.find(id, a);
				}
				a.treeSwap(b);
			}
		}
	}

	return (
		Node.getMaxNodes(left.getLevels())
			.map((elem) => elem.symbol)
			.join('') +
		Node.getMaxNodes(right.getLevels())
			.map((elem) => elem.symbol)
			.join('')
	);
}
