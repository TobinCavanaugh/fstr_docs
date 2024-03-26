<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">

## From
This is the set of functions related to creating `fstr` structs.

### From C string : `fstr_from_C` : 
This creates an `fstr` from a C string literal. <br/>
Supports `wchar_t` via the use of `L` prefixed string literals.
```C
fstr * str = fstr_from_C("abc123");
fstr_println(str);
fstr_free(str);
```
\> `abc123`

---

### From C format string : `fstr_from_format_C` :
This creates an `fstr` from a C format. This takes in a C format (think `printf` format) and creates an `fstr` from it.

```C
fstr * str = fstr_from_format_C("%02d-%02d-%d", 4, 12, 2005);
fstr_println(str);
fstr_free(str);
```
\> `04-12-2005`

---

