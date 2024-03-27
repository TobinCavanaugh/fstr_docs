<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">

This is a set of functions relating to appending to `fstr` types

### Append C string : `fstr_append_C` :

<div class="arguments">
  <div class="ret">void</div>
  <div class="arg">fstr * str</div>
  <div class="arg">chr * buf</div>
</div>

This function appends a C style string (or literal) `buf` to our `fstr`.
<br/> This supports `wchar_t`.
<supwchr/>

```C
fstr * str = fstr_from_C("Hello");
fstr_append_C(str, " Cruel World");
fstr_println(str);
fstr_free(str);
```

<output>Hello Cruel World</output>

---

### Append string : `fstr_append` :

<div class="arguments">
  <div class="ret">void</div>
  <div class="arg">fstr * str</div>
  <div class="arg">fstr * buf</div>
</div>

This function appends our `fstr * buf` contents to our `str`.

```C
fstr * str = fstr_from_C("Fancy");
fstr * other = fstr_from_C(" Strings");
fstr_append(str, other);
fstr_println(str);
fstr_free(str);
fstr_free(other);
```

<output>Fancy Strings</output>

---
### Append Character : `fstr_append_chr` :

<div class="arguments">
  <div class="ret">void</div>
  <div class="arg">fstr * str</div>
  <div class="arg">chr c</div>
</div>

This function appends the character `c` to our `str`.
This supports `wchar_t`

```C
fstr * str = fstr_from_C("10 + 10 = ");
fstr_append_chr(str, '2');
fstr_append_chr(str, '0');
fstr_println(str);
fstr_free(str);
```
<output>10 + 10 = 20</output>

---
### Insert string : `fstr_insert` :
<div class="arguments">
<div class="ret">void</div>
<div class="arg">fstr * str</div>
<div class="arg">usize index</div>
<div class="arg">fstr * add</div>
</div>

This function inserts the `fstr * add` at the `index` within `str`.

```C
fstr * str = fstr_from_C("0123456789");
fstr * add = fstr_from_C("abc");
fstr_insert(str, 1, add);
fstr_print(str);
fstr_free(str);
fstr_free(add);
```
<output>0abc123456789</output>

---
### Insert C String : `fstr_insert_C` :
<div class="arguments">
<div class="ret">void</div>
<div class="arg">fstr * str</div>
<div class="arg">usize index</div>
<div class="arg">chr * add</div>
</div>

This function inserts the `chr * add` at the `index` within `str`.

```C
fstr * str = fstr_from_C("0123456789");
chr * add = "abc";
fstr_insert_C(str, 1, add);
fstr_print(str);
fstr_free(str);
```
<output>0abc123456789</output>

---

### Append Format C : `fstr_append_format_C`

<div class="arguments">
<div class="ret">void</div>
<div class="arg">fstr * str</div>
<div class="arg">chr * format</div>
<div class="arg">...</div>
</div>

This function appends a C string constructed from a format (think `printf()`). 

```C
#include <time.h>

fstr * str = fstr_from_C("Info) ");
fstr_append_format_C(str, "Unix Time is: %llus", time(NULL));
fstr_println(str);
fstr_free(str);
```
<output>Info) Unix Time is: 1711501044s</output>

---

### Pad String : `fstr_pad` :

<div class="arguments">
<div class="ret">void</div>
<div class="arg">fstr * str</div>
<div class="arg">usize targetLength</div>
<div class="arg">chr pad</div>
<div class="arg">int8_t side</div>
</div>

This function pads an `fstr` to reach the particular length `targetLength` by placing the padding character repeatedly on a particular `side`

In this and other cases;

- `side < 0` : For padding to occur on the left side
- `side > 0` : For padding to occur on the right side
- `side == 0`: For padding to occur on both sides

In the case that both sides padding cannot be equal in length, the extra character will be placed on the right side. If this is an issue, call this function with `targetLength - 1` and use `fstr_insert` with `index = 0` to pad the extra character to the length.

In the case that `targetLength` is `<=` the length of `str`, nothing will be done.

```C
fstr * str = fstr_from_C("Centered");
fstr_pad(str, 16, '-', 0);
fstr_insert_C(str, 0, "|");
fstr_insert_C(str, fstr_length(str), "|");
fstr_println(str);
fstr_free(str);
```
<output>|----Centered----|</output>

---