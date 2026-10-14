# CLAUDE.md — py_drills / Part 1 project guide

Context for any Claude session building the end-of-Part-1 project with Gackmar.
This file grows as the Talent Nation curriculum progresses. The project is built
only after all of Part 1 (Python & Foundations, Modules 1–7) is complete. The same
pattern repeats for later parts: finish the part, then build its project.

## Working agreement

Carried over from LEARNING.md.

- **Drills during lessons are small.** A short working example of each newly learnt
  concept, nothing big. One review for correctness; done when it runs correctly.
- **Project is build mode.** Claude drafts; Gackmar reviews every line until he can
  explain and defend it.
- **Concepts listed below are internalised.** Use them freely. Anything *not* listed is
  new: stop, explain it with one example, and let Gackmar write it (learn mode).
- **Diagnosis is his.** When something breaks, give the evidence path (what to run,
  compare, inspect), not the cause.
- **Fix + concise why.** No roundabout explanations. Standalone examples use names
  that don't appear in his code.
- Standard library only unless the project says otherwise.
- Commits carry no `Co-Authored-By` or other AI attribution trailer.

## Background

- Strong Go background (01-edu track: ascii-art suite, ascii-art-web, cc-archer package
  manager). Values explicit structure, small entry points, one responsibility per file.
- Environment: Linux (Omarchy, dual-booted with Windows), Python 3.12+. See the repo
  README for details. Indent with **spaces**, never tabs.

### Go → Python differences already covered

| Concept | Go | Python |
|---|---|---|
| Typing | Static | Dynamic — type belongs to the value |
| Errors | `(value, err)` enforced | Exceptions; tuple pattern optional, not enforced |
| Block scope | Braces | Only `def` creates scope |
| Division | `int/int` truncates | `/` → float; `//` floors |
| Logic | `&&` `\|\|` `!` | `and` `or` `not` (return operands) |
| Zero values | `var x bool` → `false` | No declaration; unassigned name → `NameError` |
| Ternary | none | `a if cond else b` |
| Chained comparison | not allowed | `18 <= age <= 65` |

## Concepts covered

### Fundamentals (original Lessons 1–15)
Type casting with `try/except ValueError`; f-strings (`:.2f`, `end=`, `sep=`); string methods
(`.strip()`, `.split()`, `.join()`, `.replace()`, `.startswith()`, `.removeprefix()`, `.partition()`);
slicing and negative indices; functions with defaults, keyword args, `*args`, `**kwargs`;
LEGB scope; higher-order functions, `map()`, `filter()`, `sorted()`, lambdas; list comprehensions;
dicts incl. `{**d, "k": v}`; `sys.stderr`, `sys.exit()`; `input()`; `is` vs `==`; `id()`.

### Branching (9.1.x)
- `elif` = mutual exclusivity; consecutive `if`s = independent checks. Separate `if`s re-read
  state an earlier block may have mutated.
- First match wins. Specific before general; compound `A and B` before its parts, or it's dead.
- Truthiness: falsy = `False`, `None`, `0`, `0.0`, `""`, `[]`, `()`, `{}`, `set()`. Everything else
  truthy (`"0"`, `" "`, `-1`). Use `if items:` / `if not items:`; test explicitly when 0 or `None`
  is real data.
- Never `== True` / `== False`.
- Guard clauses = early exit (`return`, `continue`): plain `if`, no `elif`, no trailing `else`.
- Guard order: dependency, security, specificity, cost. Don't merge guards with distinct messages.

### Loops (10.1.x)
- `for` runs until its iterable is exhausted; `while` until a condition flips.
- `while True` + `break` when the exit is only knowable mid-body.
- `continue` in a `while` must come after the state update, or the loop hangs.
- `break` exits only the innermost loop; outer exit via a flag or a function `return`.
- `for/else`: `else` runs only if no `break` fired.
- `enumerate(xs, start=1)` over `range(len(xs))`; `range(len())` only to assign by index.
- `range` is a lazy sequence: `len()`, indexing, O(1) `in`. `reversed(range(...))`.
- Prefer `sum()`, `max()`, `"".join()` over manual accumulators; string `+=` in a loop is quadratic.
- Don't rely on the loop variable after the loop (unbound if the iterable was empty).

### Functions, data, and design (from drills)
- Return the same shape on every path. `(value, error)` tuples, unpacked at the call site.
- A variable must be assigned on every path that later reads it.
- Don't catch an exception you can't handle; a bare `return` gives `None` and crashes the caller.
- Dynamic key access: `parcel[rule["field"]]`. Rules as data; operators as data via
  `operator.gt` etc. stored in a dict.
- `[x]` is a one-item list; `list(x)` iterates `x` (a string becomes its characters).
- Assignment never copies: two names, one object (aliasing).
- Don't rebind a name to a different type mid-function.
- Partitions must sum to the whole (resolved + abandoned + unreached == len(queue)).
  Derive values from what you already track rather than maintaining extra counters.

### AI concepts (10.2.x)
- Rules when you can state them and must justify each decision; fitted models when you
  can't state them but have labelled examples.
- Real systems are hybrids: a rules layer (policy, cheap, auditable) in front of a model layer.
- Rules come first and produce the data that later trains the model.
- Models optimise exactly what they're measured on (objective function problem).
- Models can learn proxies that test well and fail in deployment.
- A trained model is still deterministic; generation varies only through sampling.

## Known slips to catch in review
- `&&` / `||` instead of `and` / `or`
- String methods called as functions (`strip(s)`)
- Hardcoded literals where a named variable exists
- Off-by-one: `len(x) - 1` is the last index; `== MAX` vs `> MAX`
- Stale state across loop iterations
- Order of operations: measuring or checking before mutating
- Shadowing built-ins (`list`, `input`)
- Bare `except:`
- Overwriting a bool with display text, then testing it (truthy string)

## Not yet covered (Part 1 remaining)
- Module 1 remainder: 10.3 (algorithms, programs & rules) onward
- Module 2: 16.1 lambda (formal), 17.1 recursion
- Module 3: built-in data structures
- Module 4: object-oriented programming
- Module 5: advanced data structures & algorithms
- Module 6: advanced Python features
- Module 7: modules, environments, testing, concurrency

## Project requirements (to be finalised after Part 1)
- Exercises concepts from every Part 1 module.
- Real input (files or an API) and real output, not hardcoded sample data.
- Tests with `pytest` for core logic (Module 7).
- Small entry point; logic in modules; one responsibility per file.
