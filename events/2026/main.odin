package ec2026

import "core:time"
import "core:strings"
import "core:fmt"
import "core:os"
import "core:flags"

import "base:runtime"

SOLVERS := [1][3](#type proc(input: []byte) -> ReturnValue){
    [3](#type proc(input: []byte) -> ReturnValue){ solve1_1, solve1_2, solve1_3 }
}

main :: proc() {
    args := os.args[1:]
    parsed_args : struct{
        day: int `args:"name=d,required" usage:"Day to run"`,
        part: int `args:"name=p,required" usage:"Part to run"`,
    }
    flags.parse_or_exit(&parsed_args, os.args)

    solve(parsed_args.day, parsed_args.part)
}

solve :: proc(day: int, part: int) {
    if day > len(SOLVERS) || part > len(SOLVERS[day]) {
        fmt.println("Invalid day or part")
        return
    }

    options := setup_solver(day, part)
    part := time.benchmark(&options)
    if (part == time.Benchmark_Error.Okay) {
        fmt.println(options.duration)
    }
}

SolverOptions :: struct {
    day: int,
    part: int,
    solver: proc(input: []byte) -> ReturnValue,
}

setup_solver :: proc(day: int, part: int) -> time.Benchmark_Options {
    solver_options := new(SolverOptions)
    solver_options^ = SolverOptions{day, part, SOLVERS[day - 1][part - 1]}

    options := time.Benchmark_Options{}
    options.user_data = solver_options
    options.bench = proc(options: ^time.Benchmark_Options, allocator: runtime.Allocator) -> (err: time.Benchmark_Error) {
        sb, e := strings.builder_make()
        if e != nil {
            fmt.eprintln("Bad", e)
            return nil
        }

        solver_options := (cast(^SolverOptions)options.user_data)^
        filepath := fmt.sbprintf(&sb, "inputs/day%02d/part%d.txt", solver_options.day, solver_options.part)
        data, e2 := os.read_entire_file(filepath, context.allocator)
        if e2 != nil {
            fmt.eprintln("Unable to read file", e)
            return nil
        }
        defer delete(data, context.allocator)

        fmt.println(solver_options.solver(data))
        return nil
    }

    return options
}