package lib

import "flag"

type CmdArgs struct {
	IsTest bool
	Quest  uint
	Part   uint
}

func ParseArgs() CmdArgs {
	var args = CmdArgs{}
	flag.BoolVar(&args.IsTest, "t", false, "Whether to run input using test.txt or not")
	flag.UintVar(&args.Quest, "q", 0, "Quest to run")
	flag.UintVar(&args.Part, "p", 0, "Part of this quest to run")
	flag.Parse()
	return args
}
