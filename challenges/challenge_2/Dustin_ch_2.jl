# force, mass, acceleration calc

function input(prompt)
    print(prompt)
        readline()
    end

function force_calc( ; f=nothing, m=nothing, a=nothing)
    if f==nothing
        print(m*a)
    elseif m==nothing
        print(f/a)
    elseif a==nothing
        print(f/m)
    end
end

function get_selection()
    println("What would you like to calculate?")
    println("Force (F), Mass (M), Acceleration (A)")
    ans = input("Please enter your selection: ")
    while ans != "F" && ans != "A" && ans != "M" && ans != "Q"
        ans = input("You must select F, M, A, or Q to quit: ")
    end
    return ans
end

function get_values(x)
    if x == "F"
        M = parse(Int, input("Enter Mass: "))
        A = parse(Int, input("Enter Acceleration: "))
        force_calc(m=M, a=A)
    elseif x == "M"
        F = parse(Int, input("Enter Force: "))
        A = parse(Int, input("Enter Acceleration: "))
        force_calc(f=F, a=A)
    else
        F = parse(Int, input("Enter Force: "))
        M = parse(Int, input("Enter Mass: "))
        force_calc(f=F, m=M)
    end
end

selection = get_selection()
if selection == "Q"
    exit()
end
get_values(selection)
