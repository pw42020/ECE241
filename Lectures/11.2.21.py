"""
Lecture 15: State Machines
    Objective
        Understand how pattern matching can be performed with regular expressions
        Learn how state machines can be used to implement regular expressions
    Regular Expressions
        Method to describe patterns of text
            Character-by-character processing
            Special operators
                | : alternatives
                . : arbitrary character
                * : zero or more repetitions
                + : one or more repetitions
                () : precedence
        Examples
            abcd
                abcd matches, aabcddoes not match
            a*bcd
                aabcd matches, bcd matches, cd does not match
            (ab|bb)cd
                abcd matches, bbcd matches, abbbcd does not match
            (ab|bb)*cd
                abbbcd matches, bbabcd matches, cd matches, ababcd matches, abbb does not match
        Use of Regular Expressions
            Compiler
                Interpreting characters in program
                Regular expressions for numbers, keywords, etc.
                Example toolL flex
            Networking
                Checking network traffic for attacks
                Regular expressions for attack patterns
                Example tool: snort database
    State Machine
        Regular expression can be matched with a state machine (or finite automaton)
        State machine is special case of directed graph
            Nodes represent state
            Edges represent transitions (based on input)
        State machines can be constructed for any kind of regular expression



"""