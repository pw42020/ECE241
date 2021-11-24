'''
Lecture 18: Linear Programming
    Introduction
        Many problems can be formulated as maximizing or minimizing an objective, under limited resources and constraints
        If
            objective can be specified as linear function of certain variables
            constraints on resources can be specified as equalities or inequalities on those variables
        We have a linear programming problem
    Example: Political Problem
        Assume you are a politician trying to win an election
        Your district contains urban, suburban, and rural areas of 100k, 200k, and 50k registered voters respectively
        You would like to win the majority in all areas
        You are aware that advertising on certain issues might help you win the election
        The issues of concern are:
            Building more roads
            Gun control
            Farm subsidies
            Gasoline tax
        You can estimate how many votes you will win or lose from each population segment
            by spending 1k on advertising on each issue
        Your task is to figure out the minimum amount of money to be spent in order to win 50k
            urban, 100k suburban and 25k rural votes
        This can be approached by trial and error but won't be the most efficient most likely
        Instead can use MATRICES AND LINEAR ALGEBRA!!!
    Linear Programming Overview
        Two forms, slack and standard
        Standard
            Maximization of linear function subject to linear inequalities
        Slack
            Maximization of linear function subject ot linear equalities
        for now, maximizing of a linear function with n variables subject to a set of m linear inequalities
        For xs that satisfy all constraints are called a feasible solution to the linear programming program
        Function we wish to optimize is called objective function
        Area surrounded by all constraints defines set of feasible solutions
            Feasible region
            Particular value of objective function at particular point is called objective value
            Feasible region contains infinite number of points
            Find efficient way to find point that achieves maximum objective value without
                explicitly evaluating objective function at every point
        Similarly, in the case of n variables, each constraint defines half-space in n-dimensional space
        Feasible region formed by intersection of these half-spaces is called simplex
        Objective function is not a hyperplane
        Because of convexity, solution will still occur at vertex of simplex
    Applications of Linear Programming
        Has a large number of applications
        One very popular area is Operations Research
        Airline scheduling flight crews
            Many FAA constraints: # of consecutive hours crew can work, work only on particular
                model of aircraft during one month
            Airline wants to schedule crews on all flights using as few crew members as possible
        Oil company deicing where to drill for oil
            Sitting drill at particular location has associated cost based on geological
                surveys an expected payoff on number of barrels
            Limited budget for location new drills but wants to maximize of expected oil to find
    Standard Form
        Always possible to convert minimization or maximization of linear function into standard form
        Not in standard form because
            Objective function might be minimization rather than maximization
            There may be variables without nonnegative constraints
            Equality constraints which have an equal sign rather than a <= sign
    Slack Form
        To efficiently solve a linear problem with simplex algorithm, prefer to extend it in form in which some of the constraints
            are equality constraints
        More precisely, convert it into a form in which nonnegative constraints are only inequality constraints,
            remaining constraints are equalities
        s is called slack variable because it measures slack (or difference) between the left-hand and right hand side of sum
        only if s = bi - sum and s >= 0 can the conversion be applied to each inequality constraint of a linear program
        This results in a linear program wher eonly inequality constraints are nonnegative ones
        Use x(n+i) instead of s to denote slack variable associated with the ith inequality x(n+i) = bi - sum




'''