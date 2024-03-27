<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">

### Abstract

A simple C library for handling both common and complex dynamic string functionality.

### Implementation

<fstr/> takes advantage of a novel string implementation. It uses a character array with a pointer to the last character of the string. This allows for strings that support inline `\0` and length that only requires one subtraction to calculate. The <fstr/> type is dynamically allocated, and most functions take care to only allocate when strictly necessary.

### Getting Started
> "Good code is its own best documentation" 

\- Steve McConnell

<fstr/> was made with the intention of simplicity, it's well commented, and intuitively designed. The header files contain helpful descriptions will be your friend throughout using `fstr.h`.

[Quick Start Guide](getting_started.md)

### Quick Examples 
> Creating and using string:

```C
#include "fstr.h"

int main(){
    fstr* str = fstr_from_C("Hello World"); //(1)
    fstr_println(str);
    fstr_free(str);
}
```

> Parsing an integer from a string:

```C
#include <stdio.h>
#include "fstr.h"
#include "fstr_parse.h"

int main() {
    fstr *str = fstr_from_C(" 1234 ");
    int64_t value = 0;
    if (fstr_try_to_i64(str, &value)) {
        printf("%lld", value);
    } else {
        printf("Failed to parse fstr: ");
        fstr_print(str);
    }
}

```
