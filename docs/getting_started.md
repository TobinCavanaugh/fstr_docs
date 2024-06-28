<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">
<br/>
1. Grab the latest release of the `fstr` project from [https://github.com/TobinCavanaugh/fstr/releases](https://github.com/TobinCavanaugh/fstr/releases) by downloading the `fstr.h` and `fstr.c` files to your project source directory.
<br/>
<br/>
2. Include `fstr.h` in the file you wish to use `fstr` functionality in. 
<br/>
<br/>
3. Reference `fstr.c` in your build tool. For CMake, list `fstr.c` as one of the arguments in `add_executable`. <br/>
<br/>
4. To create `fstr*` structs use the [from](From) functions.
<br/>
<br/>
5. Remember to use `fstr_free` to free your strings when they're done being used.<br/>