crrcy
===
## Papar Information
- Title:  `crrcy`
- Authors:  `Dzmitry Pahasrsky`
- Description: `crrcy is fast and minimalistic way to convert over 150 currencies in your terminal with just few words`

## Install & Dependence
- python >= 3.10.10
- google_currency >= 1.0.10

## Download

1. First, you need to clone this repo.
2. Second, install package:
  `pip install google-currency`
3. I know that you want to use this like CLI with one command, and for do this, you need to:
 - In terminal, open `bash_profile` or `zsh_profile` (depends what shell you use) using text editor like `nano`:               
  `nano .[YOUR SHELL]_profile`                 
  ATTENTION: As of macOS 10.6 Catalina and its successor Big Sur, Apple has made the zsh shell the default shell, previously it was the bash shell.
 - Now, you need to paste this line of text in file (if you are on MacOS, add `3` after `python`):                 
  `alias crrcy='python [YOUR PATH TO main.py IN REPOSITORY FOLDER]'`
 - And lastly, save this file with `ctlr+X` and update file with this command:                     
  `source ~/.[YOUR SHELL]_profile`
 - If you can type `crrcy -i` in you terminal and not get an error - everything works fine! Now you can use crrcy in a comfortable way! 

## Use

- Before use it, make sure you have alias on this programm (see last step on previous section)
- To use it, you just need to type `crrcy -i` if you want to convert in interactive way, or 
  ```
  crrcy [currency you want to convert] [currency you want to convert to] [amount]
  ```
  to convert in one line.
- For help, use `crrcy -h`

## Directory Hierarchy
```
|—— .gitignore
|—— LICENSE
|—— README.md
|—— main.py
```

### Tested Platform
- software
  ```
  OS: macOS 12.6.6 21G646 x86_64 
  Python: 3.10.10
  google_currency: 1.0.10
  ```
- hardware
  ```
  CPU: Intel i5-5287U (4) @ 2.90GHz 
  GPU: Intel Iris Graphics 6100 
  ```

## License

MIT License

Copyright (c) 2023 Dzmitry Paharski

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
