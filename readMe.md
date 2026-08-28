
# Python Drills — cosmicodearcher
 
## Background
 
I'm a software development fellow at **Learn2Earn**, a two-year project-based engineering program in Lagos, Nigeria. My original track was Go, built on the 01-edu peer-to-peer methodology — completed `ascii-art` (banner-rendering CLI), `ascii-art-web` (HTTP server with `net/http` and `html/template`), `HTTP Haven` (routing and status-code exercises), and `cc-archer`, a Go package manager that resolves GitHub releases via the GitHub API.

Learn2Earn later moved off the 01-edu curriculum and partnered with **Talent Nation**, Nigeria's AI Engineering Fellowship, which starts from the ground up in **Python**. I've continued the Go work independently while picking up Python through the new track.

This repo is where that Python journey lives — starting from zero syntax knowledge in the language, but not from zero as a programmer.

## Why This Repo Exists

Talent Nation's curriculum is theory-first: video and text lessons rather than 01-edu's build-immediately projects. Its practice platform (the Arena) has also been intermittently unavailable, which left long stretches of reading with nothing to type.

So these drills exist to close that gap. Each one is a small, self-contained script that forces a concept into working memory instead of leaving it as something I recognise on a page. Where the Arena was down, the drills replaced it entirely.
 
## Coming From Go — What's Actually Different
 
The mental adjustments this repo has worked through in practice:
 
| Concept | Go | Python |
|---|---|---|
| Typing | Static, compiler-enforced | Dynamic — type belongs to the value, not the name |
| Compilation | `go build` produces a native binary ahead of time | Compiles to bytecode, run by the PVM at runtime |
| Error timing | Type errors caught at compile time | Surface at runtime, on the line that executes |
| Block scope | Braces create scope | Only `def` creates scope — `if`/`for`/`while` don't |
| Division | `int / int` truncates toward zero | `/` always returns float; `//` floors |
| Logical operators | `&&`, `\|\|`, `!` | `and`, `or`, `not` |
| Membership | Loop or `slices.Contains` | `in` operator |
| String methods | `strings.ToUpper(s)` | `s.upper()` — method on the object |
| Entry point | `func main()` required | The file is the program |
| Default arguments | Not supported | `def f(x="default")` |

## Topics Covered

Working through the Talent Nation curriculum, drilled here:

- Variables, primitive types, dynamic typing, name-vs-object binding
- Type casting (`int()`, `float()`, `str()`) and safe conversion with `try`/`except`
- Operators, precedence, associativity, short-circuit evaluation
- Conditionals, guard clauses, `if`/`elif`/`else` branching
- Loops (`for`/`range`, `while`), `break`/`continue`, nested loops
- Strings: indexing, slicing, methods, f-strings, manual character processing
- Functions: parameters, defaults, keyword arguments, scope and lifetime
- Higher-order functions: `map()`, `filter()`, `sorted()`, lambdas, list comprehensions
- Shell and streams: stdout/stderr, redirection, exit codes, PATH, headless execution
 
## Structure
 
Each drill is a standalone `.py` file, numbered in the order it was written. Commit messages document what was built and, where relevant, what bug or misconception got caught and fixed along the way — Go instincts don't always transfer cleanly, and that's usually the more useful part to remember later.
 
## Status
 
Actively learning — this repo will grow alongside the Talent Nation curriculum, lesson by lesson.
