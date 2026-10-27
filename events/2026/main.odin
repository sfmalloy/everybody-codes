package ec2026

import "core:time"
import "core:strings"
import "core:fmt"
import "core:os"
import "core:flags"

import "base:runtime"

SOLVERS := [12][3](#type proc(input: []byte) -> ReturnValue){
    [3](#type proc(input: []byte) -> ReturnValue){ solve1_1, solve1_2, solve1_3 },
    [3](#type proc(input: []byte) -> ReturnValue){ solve2_1, solve2_2, solve2_3 },
    [3](#type proc(input: []byte) -> ReturnValue){ solve3_1, solve3_2, solve3_3 },
    [3](#type proc(input: []byte) -> ReturnValue){ solve4_1, solve4_2, solve4_3 },
    [3](#type proc(input: []byte) -> ReturnValue){ solve5_1, solve5_2, solve5_3 },
    [3](#type proc(input: []byte) -> ReturnValue){ solve6_1, solve6_2, solve6_3 },
    [3](#type proc(input: []byte) -> ReturnValue){ solve7_1, solve7_2, solve7_3 },
    [3](#type proc(input: []byte) -> ReturnValue){ solve8_1, solve8_2, solve8_3 },
    [3](#type proc(input: []byte) -> ReturnValue){ solve9_1, solve9_2, solve9_3 },
    [3](#type proc(input: []byte) -> ReturnValue){ solve10_1, solve10_2, solve10_3 },
    [3](#type proc(input: []byte) -> ReturnValue){ solve11_1, solve11_2, solve11_3 },
    [3](#type proc(input: []byte) -> ReturnValue){ solve12_1, solve12_2, solve12_3 },
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
    if day < 1 || part < 1 || day > len(SOLVERS) || part > len(SOLVERS[day]) {
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