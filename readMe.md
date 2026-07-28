
# Python Drills — cosmicodearcher
 
## Background
 
I'm a software development fellow at **Learn2Earn**, a two-year intensive project-based engineering program in Lagos, Nigeria, running on the 01-edu peer-to-peer methodology. My original track was Go — completed `ascii-art` (banner-rendering CLI), `ascii-art-web` (HTTP server with `net/http` and `html/template`), `HTTP Haven` (routing/status-code exercises), and currently building `cc-archer`, a real Go package manager resolving GitHub releases via the GitHub API.
 
Learn2Earn recently switched curriculums to **Talent Nation**, Nigeria's AI Engineering Fellowship, which starts from the ground up in **Python**.
 
This repo is where that Python journey lives — starting from zero syntax knowledge in the language, but not from zero as a programmer.
 
## Coming From Go — What's Actually Different
 
A few mental adjustments that this repo tracks as they get worked out in practice:
 
| Concept | Go | Python |
|---|---|---|
| Typing | Static, compiler-enforced | Dynamic, type attached to the value, not the name |
| Compilation | `go build` → binary, ahead of time | Interpreted line-by-line, no separate build step |
| Block scope | `{ }` creates real scope | Indentation is visual only — `if`/`for`/`while` don't create scope |
| Division | `int / int` truncates | `/` always returns a float |
| Blocks | Braces | Colon (`:`) + consistent indentation |
 
## Structure
 
Each drill is a standalone `.py` file, numbered in the order it was written. Commit messages document what was built and, where relevant, what bug or misconception got caught and fixed along the way — Go instincts don't always transfer cleanly, and that's usually the more useful part to remember later.
 
## Status
 
Actively learning — this repo will grow alongside the Talent Nation curriculum, lesson by lesson.