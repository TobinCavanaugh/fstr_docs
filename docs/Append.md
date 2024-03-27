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
fstr_append(str, " Cruel World");
fstr_println(str);
fstr_free(str);
```

<output>Hello Cruel World</output>

---

### Append fstr : `fstr_append` :

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
fstr(free_other);
```

<output>Fancy Strings</output>