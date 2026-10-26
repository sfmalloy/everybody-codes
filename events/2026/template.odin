package ec2026

import "core:time"
import "core:strings"
import "core:fmt"
import "core:os"

import "base:runtime"

main :: proc() {
    options := time.Benchmark_Options{}
    options.bench = proc(options: ^time.Benchmark_Options, allocator: runtime.Allocator) -> (err: time.Benchmark_Error) {
        data, e := os.read_entire_file("inputs/day01.txt", context.allocator)
        if e != nil {
            fmt.eprintln("Unable to read file", e)
            return nil
        }
        defer delete(data, context.allocator)
        fmt.println(solve(data))

        return nil
    }
    t := time.benchmark(&options)

    if (t == time.Benchmark_Error.Okay) {
        fmt.println(options.duration)
    }
}

solve :: proc(input: []byte) -> int {
    it := string(input)
    for line in strings.split_lines_iterator(&it) {
        fmt.println(line)
        // do stuff
    }

    return 0
}
