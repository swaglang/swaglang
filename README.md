# SwagLang

**Compiler:** ANTLR4 frontend --> LLVM IR backend (Python implementation)

## Table of Contents

1. [Introduction](#1-introduction)
2. [Language Overview](#2-language-overview)
3. [Installation and Setup](#3-installation-and-setup)
4. [Quick Start](#4-quick-start)
5. [Syntax](#5-syntax)
6. [Variables and Data Types](#6-variables-and-data-types)
7. [Operators](#7-operators)
8. [Control Flow](#8-control-flow)
9. [Functions](#9-functions)
10. [Interfaces](#10-interfaces)
11. [Error Handling](#11-error-handling)
12. [Standard Library](#12-standard-library)
13. [Examples](#13-examples)
14. [Best Practices](#14-best-practices)
15. [FAQ and Common Issues](#15-faq-and-common-issues)

## 1. Introduction

SwagLang is a statically-typed, compiled programming language with a syntax that swags.
It targets LLVM IR, enabling native code generation and cross-platform compatibility.
SwagLang emphasizes clarity through explicit mutability annotations, structured control flow, and a straightforward swag
system.

**Key characteristics:**

- Statically typed with type inference
- Explicit mutability (`let` for mutable, `const` for immutable)
- Multiple return values from functions
- Interface-based structural typing
- `defer` for deterministic cleanup
- Compiles to LLVM IR

## 2. Language Overview

SwagLang programs are composed of top-level declarations: functions, interfaces, and global variables.
Execution begins at the `main` function. All statements are newline-terminated within code blocks.

```swag
void main() {
    println("Hello, world!")
}
```

The compiler pipeline consists of four stages:

1. **Lexing.** Tokenisation via ANTLR4
2. **Parsing.** Grammar-based AST construction
3. **Semantic analysis.** Type checking, scope resolution, and error reporting
4. **LLVM codegen.** LLVM IR emission for native compilation

## 3. Installation and Setup

### Prerequisites

- Python 3.11 or later
- ANTLR4 Python runtime (`antlr4-python3-runtime`)
- LLVM toolchain (`llc`, `clang`) for compiling the emitted IR

### Installing Dependencies

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains:

```
antlr4-python3-runtime
```

### Running the Compiler

The compiler reads a `.swag` source file and emits LLVM IR to standard output:

```bash
python main.py <source_file.swag>
```

To compile the LLVM IR to a native binary, pipe it through `llc` and link with `clang`:

```bash
python main.py program.swag > program.ll
llc -filetype=obj program.ll -o program.o
clang program.o -o program
./program
```

### File Extension

SwagLang source files use the `.swag` extension.

## 4. Quick Start

The following example demonstrates core SwagLang features: variable declarations, functions, loops, and basic I/O.

```swag
int add(x: int, y: int) {
    return x + y
}

void main() {
    const a = 10
    let b = 20
    b += 5

    let result = add(a, b)
    println(result)

    let i = 0
    while i < 3 {
        println(i)
        i++
    }
}
```

**Output:**

```
35
0
1
2
```

---

## 5. Syntax

### 5.1 Statements and Newlines

Each statement inside a function body must be followed by a newline. Blank lines are permitted between statements.
The compiler uses newlines as statement terminators within code blocks.

```swag
void main() {
    let x = 1
    let y = 2
    println(x + y)
}
```

There is no semicolon terminator at the end of statements.
Semicolons are used exclusively inside `for` loop headers.

### 5.2 Comments

SwagLang supports two comment styles:

```swag
// This is an inline comment

/*
   This is a
   block comment
*/
```

Both comment styles are discarded by the lexer and do not affect compilation.

### 5.3 Identifiers

Identifiers must start with a letter or underscore, followed by any combination of letters, digits, and underscores.

```
identifier  ::= [a-zA-Z_][a-zA-Z0-9_]*
```

**Valid identifiers:** `x`, `myVar`, `_count`, `user123`

**Invalid identifiers:** `1value`, `my-var`, `for` (reserved keyword)

### 5.4 Keywords

The following are reserved keywords and cannot be used as identifiers:

| Category         | Keywords                                            |
|------------------|-----------------------------------------------------|
| Types            | `int`, `float`, `string`, `bool`, `error`           |
| Access modifiers | `const`, `let`                                      |
| Control flow     | `if`, `else if`, `else`, `for`, `in`, `while`, `do` |
| Loop control     | `break`, `continue`                                 |
| Functions        | `return`, `void`, `defer`                           |
| Collections      | `map`, `set`                                        |
| Interfaces       | `interface`, `extends`                              |
| Literals         | `true`, `false`, `null`                             |

### 5.5 Code Blocks

A code block is enclosed in curly braces. Each statement within a block must occupy its own line:

```swag
{
    stmt1
    stmt2
    stmt3
}
```

---

## 6. Variables and Data Types

### 6.1 Primitive Types

| Type     | Description                          | Example literals      |
|----------|--------------------------------------|-----------------------|
| `int`    | 64-bit signed integer                | `0`, `42`, `-7`       |
| `float`  | 64-bit double-precision float        | `3.14`, `0.5`, `-1.0` |
| `string` | Mutable UTF-8 string                 | `"hello"`, `""`       |
| `bool`   | Boolean value                        | `true`, `false`       |
| `error`  | Error value (assignable from string) | Used as return type   |

### 6.2 Collection Types

| Type            | Syntax      | Description                           |
|-----------------|-------------|---------------------------------------|
| Array           | `T[]`       | Ordered, indexed, homogeneous         |
| Multi-dim array | `T[][]`     | Nested arrays                         |
| Map             | `map<K, V>` | Key-value associative collection      |
| Set             | `set<T>`    | Unordered collection of unique values |

### 6.3 Variable Declaration

Variables are declared with an access modifier (`let` or `const`), followed by the variable name, an optional type
annotation, and an initialiser.

**Syntax:**

```
(let | const) name [: type] = expr
```

```swag
let x = 42               // type inferred as int, very swag
const pi: float = 3.14   // explicit type annotation
let name: string = "Bob"
```

**`let`** declares a mutable variable. Its value can be reassigned.

**`const`** declares an immutable binding. Attempting to reassign a `const` variable is a compile-time error.

```swag
const limit = 100
limit = 200  // Error: cannot assign to const 'limit'
```

### 6.4 Type Inference

When no type annotation is provided, the compiler infers the variable's type from the initialiser expression. The
inferred type is fixed at declaration and cannot change.

```swag
let count = 0        // inferred: int
let ratio = 0.5      // inferred: float
let active = true    // inferred: bool
let msg = "hello"    // inferred: string
```

Type annotations are required when the initialiser cannot unambiguously determine the type, such as when
assigning `null` or a struct literal to a named interface type.

### 6.5 Global Variables

Variables declared at the top level (outside any function) are global. They follow the same syntax as local declarations
and support both `let` and `const`.

```swag
const version = 1
let counter = 0

void main() {
    counter += 1
    println(counter)
}
```

### 6.6 Assignment

Mutable variables are reassigned using `=` or compound assignment operators.

```swag
let x = 5
x = 10
x += 3
x -= 1
```

The left-hand side of an assignment can include array indexing and field access:

```swag
let arr: int[] = [1, 2, 3]
arr[0] = 99

let point = {x: 0, y: 0}
point.x = 10
```

### 6.7 Array Literals

Arrays are written with square brackets and comma-separated values. Trailing commas are permitted.

```swag
let nums: int[] = [1, 2, 3, 4]
let matrix: int[][] = [[1, 2], [3, 4]]
let empty: string[] = []
```

### 6.8 Map Literals

Maps use double curly braces with `key: value` pairs separated by commas.

```swag
let scores: map<string, int> = {{"alice": 95, "bob": 87}}
```

**Note:** The double-brace syntax (`{{ }}`) distinguishes a map literal from a struct literal.

### 6.9 Set Literals

Sets use the `#[` prefix and `]` suffix:

```swag
let primes: set<int> = #[2, 3, 5, 7]
let tags: set<string> = #["go", "rust", "swag"]
```

### 6.10 Struct Literals

A struct literal is written with single curly braces and `name: value` pairs. Struct literals are used to construct
values that satisfy an interface.

```swag
interface Point {
    x: int
    y: int
}

let p: Point = {x: 10, y: 20}
```

Struct literals can also be assigned without an explicit type annotation, in which case the compiler synthesises an
anonymous type from the field names:

```swag
let origin = {x: 0, y: 0}
```

### 6.11 Null

The `null` literal represents an absent value. It is assignable to any variable whose declared type is a user-defined (
interface) type or `error`.

```swag
interface Config {
    timeout: int
}

let cfg: Config = null
```

---

## 7. Operators

### 7.1 Arithmetic Operators

| Operator | Name           | Types                          | Result                                                                 |
|----------|----------------|--------------------------------|------------------------------------------------------------------------|
| `+`      | Addition       | `int`, `float`, `string`       | Same as operands (or `float` if mixed numeric); `string` concatenation |
| `-`      | Subtraction    | `int`, `float`                 | Same or `float`                                                        |
| `*`      | Multiplication | `int`, `float`; `string * int` | Same or `float`; `string` repetition                                   |
| `/`      | Division       | `int`, `float`                 | Same or `float`                                                        |
| `%`      | Modulo         | `int`, `float`                 | Same or `float`                                                        |
| `**`     | Exponentiation | `int`, `float`                 | Always `float`                                                         |

**Numeric widening:** When an `int` and a `float` are combined in an arithmetic expression, the `int` is implicitly
widened to `float`. The result type is `float`.

```swag
let a = 2 ** 10    // 1024.0 (float)
let b = "abc" * 3  // "abcabcabc" (string)
let c = 1 + 2.0    // 3.0 (float)
```

### 7.2 Comparison Operators

All comparison operators yield `bool`.
2
| Operator | Description | Valid Types |
|----------|-----------------------|------------------------------|
| `==`     | Equal to | Any same type; mixed numeric |
| `!=`     | Not equal to | Any same type; mixed numeric |
| `<`      | Less than | `int`, `float`, `string`     |
| `>`      | Greater than | `int`, `float`, `string`     |
| `<=`     | Less than or equal | `int`, `float`, `string`     |
| `>=`     | Greater than or equal | `int`, `float`, `string`     |

```swag
let isEqual = (1 == 1)       // true
let ordered = ("a" < "b")    // true
```

### 7.3 Logical Operators

| Operator | Description | Operand Types  | Result |
|----------|-------------|----------------|--------|
| `&&`     | Logical AND | `bool`, `bool` | `bool` |
| `\|\|`   | Logical OR  | `bool`, `bool` | `bool` |
| `!`      | Logical NOT | Truthy type    | `bool` |

**Truthy types** — types that can appear in a boolean context (condition of `if`, `while`, or operand
of `!`): `bool`, `int`, `float`, `string`, arrays, and sets.

```swag
let a = true && false   // false
let b = !true           // false
let c = 0               // falsy in conditions
```

### 7.4 Postfix Operators

| Operator | Description | Applies to               |
|----------|-------------|--------------------------|
| `++`     | Increment   | Mutable numeric variable |
| `--`     | Decrement   | Mutable numeric variable |

```swag
let i = 0
i++    // i is now 1
i--    // i is now 0
```

Postfix operators are statements, not expressions. They cannot be used inside a larger expression.

### 7.5 Assignment Operators

| Operator | Equivalent to     |
|----------|-------------------|
| `=`      | Simple assignment |
| `+=`     | `x = x + expr`    |
| `-=`     | `x = x - expr`    |
| `*=`     | `x = x * expr`    |
| `/=`     | `x = x / expr`    |
| `%=`     | `x = x % expr`    |

All compound assignment operators require a mutable (`let`) left-hand side.

### 7.6 Ternary Operator

SwagLang supports the ternary conditional expression:

```
condition ? true_expr : false_expr
```

```swag
let max = a > b ? a : b
let label = count == 1 ? "item" : "items"
```

The condition must be a truthy type. Both branches must be type-compatible.

### 7.7 Operator Precedence

From highest to lowest precedence:

| Level | Operators                        |
|-------|----------------------------------|
| 1     | `!`, unary `-`                   |
| 2     | `**` (right-associative)         |
| 3     | `*`, `/`, `%`                    |
| 4     | `+`, `-`                         |
| 5     | `<`, `>`, `==`, `!=`, `<=`, `>=` |
| 6     | `&&`                             |
| 7     | `\|\|`                           |
| 8     | `? :`  (ternary)                 |

Use parentheses to override precedence explicitly.

---

## 8. Control Flow

### 8.1 `if` / `else if` / `else`

**Syntax:**

```
if condition {
    // ...
} else if condition {
    // ...
} else {
    // ...
}
```

The condition is any expression of a truthy type. Parentheses around the condition are not required.

```swag
let score = 85

if score >= 90 {
    println("A")
} else if score >= 75 {
    println("B")
} else {
    println("C")
}
```

### 8.2 `while` Loop

A `while` loop executes its body as long as the condition is truthy.

```swag
let n = 5
while n > 0 {
    println(n)
    n--
}
```

### 8.3 `do`-`while` Loop

A `do`-`while` loop executes its body at least once before evaluating the condition.

**Syntax:**

```
do {
    // ...
} while (condition)
```

Note that the condition in a `do`-`while` loop is wrapped in parentheses, unlike the `while` loop.

```swag
let x = 0
do {
    println(x)
    x++
} while (x < 3)
```

**Output:** `0`, `1`, `2`

### 8.4 `for` Loop

The `for` loop has a C-style three-part header: initialiser, condition, and update.

**Syntax:**

```
for init ; condition ; update {
    // ...
}
```

Each part is optional. Omitting all three parts creates an infinite loop.

```swag
for i = 0 ; i < 5 ; i++ {
    println(i)
}
```

The initialiser does not use an access modifier keyword. It declares a variable scoped to the loop.

```swag
for count = 10 ; count > 0 ; count -= 2 {
    println(count)
}
```

**Infinite loop:**

```swag
for ; ; {
    // runs forever until break
}
```

### 8.5 `for`-`in` Loop

The `for`-`in` loop iterates over arrays, sets, or maps.

**Syntax:**

```
for variable in iterable {
    // ...
}
```

The loop variable is implicitly declared and scoped to the loop body. It is immutable.

```swag
let fruits: string[] = ["apple", "banana", "cherry"]
for fruit in fruits {
    println(fruit)
}
```

For maps, the loop variable receives the **key** on each iteration.

```swag
let ages: map<string, int> = {{"alice": 30, "bob": 25}}
for name in ages {
    println(name)
}
```

For sets, the loop variable receives each **element**.

```swag
let nums: set<int> = #[1, 2, 3]
for n in nums {
    println(n)
}
```

The `for`-`in` construct also supports function calls as the iterable expression.

### 8.6 `break` and `continue`

`break` exits the innermost enclosing loop immediately.

`continue` skips the remainder of the current loop iteration and proceeds to the next.

Both statements are only valid inside a loop body. Using them outside a loop is a compile-time error.

```swag
let i = 0
while true {
    if i == 5 {
        break
    }
    if i % 2 == 0 {
        i++
        continue
    }
    println(i)
    i++
}
```

### 8.7 `defer`

The `defer` statement schedules an expression to execute when the enclosing function returns, regardless of how it
returns. Deferred expressions execute in last-in, first-out order.

```swag
void processFile() {
    defer println("done")
    println("processing")
}
// Output: processing
//         done
```

`defer` is particularly useful for cleanup tasks that must always run:

```swag
void example() {
    defer println("cleanup 1")
    defer println("cleanup 2")
    println("working")
}
// Output: working
//         cleanup 2
//         cleanup 1
```

---

## 9. Functions

### 9.1 Declaration

A function is declared with a return type, a name, a parameter list, and a code block.

**Syntax:**

```
return_type functionName(param1: type1, param2: type2) {
    // body
}
```

```swag
int square(n: int) {
    return n * n
}

string greet(name: string) {
    return "Hello, " + name
}
```

### 9.2 Return Types

A function's return type appears before its name. The supported return type forms are:

| Form            | Syntax                | Description                |
|-----------------|-----------------------|----------------------------|
| Single return   | `type`                | Returns one value          |
| Void            | `void`                | Returns nothing            |
| Multiple return | `(type1, type2, ...)` | Returns two or more values |

```swag
void printLine(msg: string) {
    println(msg)
}

(int, error) divide(a: int, b: int) {
    if b == 0 {
        return 0, "division by zero"
    }
    return a / b, null
}
```

### 9.3 Parameters

Parameters are declared as `name: type` pairs, separated by commas. Trailing commas are permitted. Parameters are always
mutable within the function body.

```swag
float average(a: float, b: float, c: float) {
    return (a + b + c) / 3.0
}
```

### 9.4 Calling Functions

Functions are called by name with arguments enclosed in parentheses.

```swag
let result = square(5)
let greeting = greet("world")
printLine("Starting...")
```

### 9.5 Multiple Return Values

A function declared with a tuple return type returns multiple values simultaneously. Multiple return values are captured
using the multi-variable declaration syntax.

```swag
(int, error) safeDivide(a: int, b: int) {
    if b == 0 {
        return 0, "cannot divide by zero"
    }
    return a / b, null
}

void main() {
    let result, err = safeDivide(10, 2)
    let bad, err2 = safeDivide(10, 0)
    println(result)
}
```

Multiple return values can also be assigned to existing variables:

```swag
let x, y = safeDivide(10, 3)
x, y = safeDivide(5, 1)
```

### 9.6 Nested Functions

Functions may be declared inside other functions. A nested function is scoped to the enclosing function body and can be
called by any code within that scope after its declaration.

```swag
void main() {
    int double(n: int) {
        return n * 2
    }
    println(double(5))
}
```

### 9.7 Forward References

At the top level, function declarations are hoisted before the main analysis pass. A top-level function may therefore
call another top-level function that is declared later in the file.

```swag
void main() {
    greet()
}

void greet() {
    println("Hello!")
}
```

### 9.8 Recursion

SwagLang supports recursive functions. There is no special syntax required.

```swag
int factorial(n: int) {
    if n <= 1 {
        return 1
    }
    return n * factorial(n - 1)
}
```

---

## 10. Interfaces

### 10.1 Declaration

Interfaces define a named structural type composed of typed fields. Any struct literal that provides all required fields
satisfies an interface.

**Syntax:**

```
interface Name {
    field: Type
    optionalField?: Type
}
```

```swag
interface User {
    name: string
    age: int
    email?: string
}
```

Fields marked with `?` are optional. Struct literals satisfying the interface may omit optional fields.

### 10.2 Instantiation

An interface value is created by assigning a struct literal to a variable of the interface type. The struct literal must
supply all required (non-optional) fields.

```swag
let u: User = {name: "Alice", age: 30}
```

### 10.3 Field Access

Fields are accessed via the dot operator.

```swag
println(u.name)
println(u.age)
```

Nested access is supported:

```swag
interface Address {
    city: string
}

interface Person {
    name: string
    address: Address
}

let p: Person = {name: "Bob", address: {city: "Berlin"}}
println(p.address.city)
```

### 10.4 Inheritance with `extends`

An interface may extend one or more parent interfaces. The child interface inherits all fields from its parents. Own
fields take precedence over inherited fields of the same name.

```swag
interface Animal {
    name: string
    sound: string
}

interface Pet extends Animal {
    owner: string
}

let cat: Pet = {name: "Mochi", sound: "meow", owner: "Alice"}
```

Multiple inheritance is supported:

```swag
interface Flyable {
    maxAltitude: int
}

interface Swimmable {
    maxDepth: int
}

interface Duck extends Flyable, Swimmable {
    name: string
}
```

Circular inheritance is a compile-time error.

### 10.5 Null Assignment

An interface-typed variable may be assigned `null` to represent an absent value.

```swag
let config: Config = null
```

---

## 11. Error Handling

SwagLang uses the `error` type for explicit error propagation. Functions that can fail conventionally
return `(result, error)` as multiple return values.

### 11.1 The `error` Type

`error` is a primitive type that holds an error message string. It is assignable from a `string` literal or from
another `error` value. Assigning `null` to an `error` variable represents the absence of an error.

```swag
(int, error) parseInt(s: string) {
    // hypothetical parsing logic
    return 0, "not yet implemented"
}
```

### 11.2 Returning Errors

A function signals an error by returning a non-null `error` value. The caller is responsible for checking the returned
error.

```swag
(float, error) safeSqrt(n: float) {
    if n < 0.0 {
        return 0.0, "cannot take square root of negative number"
    }
    return n ** 0.5, null
}

void main() {
    let result, err = safeSqrt(-4.0)
    if err != null {
        println("Error occurred")
    } else {
        println(result)
    }
}
```

### 11.3 Error Propagation

SwagLang does not have built-in exception throwing or catching. All error propagation is explicit through return values.
This design makes error paths visible in the source code.

### 11.4 Semantic Error Categories

The compiler reports the following categories of semantic errors:

| Kind                | Description                                                  |
|---------------------|--------------------------------------------------------------|
| `NameError`         | Reference to an undefined variable or function               |
| `TypeError`         | Type mismatch in assignment, call, or operation              |
| `ControlFlowError`  | `break`/`continue` outside a loop; `return` outside function |
| `InterfaceError`    | Unknown parent interface; circular inheritance               |
| `RedefinitionError` | Duplicate declaration in the same scope                      |

## 12. Standard Library

SwagLang currently provides a small set of built-in functions. These are always available and require no import.

### 12.1 `println`

Prints a value followed by a newline.

```
void println(value: T)
```

`println` is polymorphic: it accepts `int`, `float`, `string`, and `bool` values.

```swag
println("Hello, world!")
println(42)
println(3.14)
println(true)
```

### 12.2 `print`

Prints a value without a trailing newline.

```
void print(value: T)
```

`print` accepts the same types as `println`.

```swag
print("Hello, ")
print("world")
println("!")
// Output: Hello, world!
```

### 12.3 `len`

Returns the length of a string.

```
int len(s: string)
```

```swag
let n = len("hello")   // 5
println(n)
```

**Note:** `len` currently operates on `string` only. Array or collection length retrieval is not yet provided by a
builtin.

---

## 13. Examples

### 13.1 Hello, World

```swag
void main() {
    println("Hello, world!")
}
```

### 13.2 Fibonacci

```swag
int fib(n: int) {
    if n <= 1 {
        return n
    }
    return fib(n - 1) + fib(n - 2)
}

void main() {
    let i = 0
    while i <= 10 {
        println(fib(i))
        i++
    }
}
```

### 13.3 FizzBuzz

```swag
void main() {
    for i = 1 ; i <= 30 ; i++ {
        if i % 15 == 0 {
            println("FizzBuzz")
        } else if i % 3 == 0 {
            println("Fizz")
        } else if i % 5 == 0 {
            println("Buzz")
        } else {
            println(i)
        }
    }
}
```

### 13.4 Working with Arrays

```swag
int sum(nums: int[]) {
    let total = 0
    for n in nums {
        total += n
    }
    return total
}

void main() {
    let numbers: int[] = [10, 20, 30, 40, 50]
    let result = sum(numbers)
    println(result)   // 150
}
```

### 13.5 Using Interfaces

```swag
interface Rectangle {
    width: float
    height: float
}

float area(r: Rectangle) {
    return r.width * r.height
}

float perimeter(r: Rectangle) {
    return 2.0 * (r.width + r.height)
}

void main() {
    let rect: Rectangle = {width: 5.0, height: 3.0}
    println(area(rect))
    println(perimeter(rect))
}
```

### 13.6 Error Handling Pattern

```swag
(int, error) divide(a: int, b: int) {
    if b == 0 {
        return 0, "division by zero"
    }
    return a / b, null
}

void main() {
    let result, err = divide(10, 2)
    if err != null {
        println("Error")
    } else {
        println(result)
    }

    let bad, err2 = divide(5, 0)
    if err2 != null {
        println("Caught error")
    }
}
```

### 13.7 Using `defer`

```swag
void readData() {
    println("Opening resource")
    defer println("Closing resource")

    println("Reading data")
    println("Processing data")
}

void main() {
    readData()
}
// Output:
// Opening resource
// Reading data
// Processing data
// Closing resource
```

### 13.8 Map Operations

```swag
void main() {
    let inventory: map<string, int> = {{"apples": 10, "bananas": 5, "oranges": 8}}

    for item in inventory {
        println(item)
    }
}
```

### 13.9 Nested Interfaces with Inheritance

```swag
interface Named {
    name: string
}

interface Contact extends Named {
    email: string
    phone?: string
}

void printContact(c: Contact) {
    println(c.name)
    println(c.email)
}

void main() {
    let contact: Contact = {name: "Alice", email: "alice@example.com"}
    printContact(contact)
}
```

### 13.10 Recursive Data Processing

```swag
int max(a: int, b: int) {
    return a > b ? a : b
}

int arrayMax(arr: int[]) {
    let best = arr[0]
    for val in arr {
        best = max(best, val)
    }
    return best
}

void main() {
    let data: int[] = [3, 17, 2, 42, 8, 1]
    println(arrayMax(data))   // 42
}
```

---

## 14. Best Practices

### 14.1 Prefer `const` by Default

Declare variables with `const` unless mutation is explicitly required. Immutable bindings prevent accidental
reassignment and communicate intent clearly.

```swag
// Preferred
const maxRetries = 3

// Only when mutation is needed
let attempts = 0
```

### 14.2 Annotate Types at Interface Boundaries

While type inference handles most local variables, always annotate the types of function parameters and return types
explicitly. At interface and function boundaries, explicit types serve as documentation and catch mismatches early.

```swag
// Good: explicit types at boundary
float computeRatio(count: int, total: int) {
    let ratio = count / total   // local inference is fine
    return ratio
}
```

### 14.3 Use Multiple Return Values for Fallible Operations

Instead of special sentinel values or global error flags, return `(result, error)` pairs. This pattern keeps error
handling local and explicit.

```swag
(string, error) readConfig(path: string) {
    // ...
    return "", "file not found"
}
```

### 14.4 Use `defer` for Cleanup

Pair resource acquisition with a deferred cleanup call immediately after acquisition. This ensures cleanup runs even if
the function exits early.

```swag
void processResource() {
    openResource()
    defer closeResource()

    // rest of the function; closeResource always runs
}
```

### 14.5 Keep Functions Small and Focused

Write functions that perform a single, well-defined task. Prefer multiple small functions over one large function with
many branches.

### 14.6 Avoid Shadowing

Do not redeclare a variable with the same name in a nested scope if the outer variable is still needed. While the
language allows shadowing through nested function scopes, it reduces code clarity.

### 14.7 Use Optional Fields Sparingly

In interface definitions, mark fields optional only when their absence is a meaningful, expected state — not as a
shortcut to avoid initialisation. Overuse of optional fields complicates struct literal construction and makes code
harder to reason about.

### 14.8 Group Related Declarations

Place related global variables and interface declarations together. Declare helper functions near the functions that use
them, or group them at the bottom of the file given that top-level declarations support forward references.

*This documentation is based on the SwagLang current release. Behaviour described here reflects the most swaggest you
can imagine. 