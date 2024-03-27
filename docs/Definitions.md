<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">


### String : `fstr` :

The type `fstr` is a struct containing three fields; `end`, `error`, and `*data`. `end` is the pointer to the last character of the string. This is how we determine length. `error` is the `STR_ERROR` which we can use to check for errors after function calls. `*data` is the pointer to the start of our character array. Unlike common C character arrays this is not null terminated.

```C
typedef struct {
    //The address of the last character in our string, inclusive.
    usize end;
    //Whether an error occurred on the string operation
    STR_ERR error;
    //The starting pointer of our string data
    chr *data;
} fstr;

```

### Character : `chr` :

The character type in `fstr.h` is designed to be as flexible as possible. As such we use a macro defining chr as char. Many functions have support for `wchar_t` directly or incidentally, as such you can change the macro definition of `chr` to use `wchar_t` for projects that require wide characters.

> <warning> Using `wchar_t` may or may not break functions. </warning>

```C
#define chr char
//OR
#define chr wchar_t
```

---

### Unsigned Values : `usize`:

`usize` is a basic macro wrapper around `uintptr_t` with the goal being to increase flexibility and cross platform support. `usize` is often used for lengths, counts, and pointers.

```C
#define usize uintptr_t
```

---

### Errors : `STR_ERR` :

`STR_ERR` is an `enum : uint8_t` type that allows the user to respond to errors raised by function calls. `fstr.h` functions will always try to recover gracefully, even in the case of null arguments, and its up to the user to check for errors raised by these functions. The `fstr` struct has the field `STR_ERR error` which gets assigned with a value in the case of an error.

```C
typedef enum : uint8_t {
    STR_ERR_None = 0,
    STR_ERR_IndexOutOfBounds = 1,
    STR_ERR_AllocFailed = 2,
    STR_ERR_ReallocFailed = 3,
    STR_ERR_NullStringArg = 4,
    STR_ERR_INCORRECT_CHAR_POINTER = 5
} STR_ERR;

```
