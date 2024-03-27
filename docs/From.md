<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">

This is the set of functions related to creating `fstr` structs.

### From C string : `fstr_from_C` :

<div class="arguments">
  <div class="ret">fstr *</div>
  <div class="arg">chr * str</div>
</div>

This creates an `fstr` from a C string literal. <br/>
Supports `wchar_t` via the use of `L` prefixed string literals.

```C
fstr * str = fstr_from_C("abc123");
fstr_println(str);
fstr_free(str);
```

<output>abc123</output>

---

### From C format string : `fstr_from_format_C` :

<div class="arguments">
  <div class="ret">fstr *</div>
  <div class="arg">chr * format</div>
  <div class="arg">...</div>
</div>

This creates an `fstr` from a C format. This takes in a C format (think `printf` format) and creates an `fstr` from it. This takes a variable amount of arguments.


```C
fstr * str = fstr_from_format_C("%02d-%02d-%d", 4, 12, 2005);
fstr_println(str);
fstr_free(str);
```

<output>04-12-2005</output>

---

### From Length : `fstr_from_length` :

<div class="arguments">
  <div class="ret">fstr *</div>
  <div class="arg">u64 length</div>
  <div class="arg">chr fill </div>
</div>

This creates an `fstr` of a particular length filled with a particular `chr`.

```C
fstr * str = fstr_from_length(10, '!');
fstr_println(str);
fstr_free(str);
```

<output>!!!!!!!!!!</output>
