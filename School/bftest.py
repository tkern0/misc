import sys#[

def evaluate(code, inputText):
  code     = [i for i in list(code) if i in '.,[]<>+-']
  bracemap = buildbracemap(code)

  cells, codeptr, cellptr = [0], 0, 0

  while codeptr < len(code):
    command = code[codeptr]

    if command == ">":
      cellptr += 1
      if cellptr == len(cells): cells.append(0)

    if command == "<":
      cellptr = 0 if cellptr <= 0 else cellptr - 1

    if command == "+":
      cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0

    if command == "-":
      cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255

    if command == "[" and cells[cellptr] == 0: codeptr = bracemap[codeptr]
    if command == "]" and cells[cellptr] != 0: codeptr = bracemap[codeptr]
    if command == ".": sys.stdout.write(chr(cells[cellptr]))
    if command == ",":
        cells[cellptr] = ord(inputText[:1])
        inputText = inputText[1:]

    codeptr += 1


def buildbracemap(code):
  temp_bracestack, bracemap = [], {}

  for position, command in enumerate(code):
    if command == "[": temp_bracestack.append(position)
    if command == "]":
      start = temp_bracestack.pop()
      bracemap[start] = position
      bracemap[position] = start
  return bracemap

with open(__file__,"r") as f: evaluate(f.read(),input(""))#]
"""
,>++++++[-<-------->],>++++++[-<-------->] input
<<[->>+<<]>[->+<]> add
[->+>>+<<<] dup
<<+>>>>>>+<<<<+++++++++ setup some vars
>[< if non-0
[->-[>]<<] %10(ish)
<[>>>>++++++[->++++++++<]>.<] if on cell 2 print cell 6
<[>++++++[-<++++++++>]<.>>>>++++[->+++++++++<]>++.<] if on cell 3 print '1' and (cell 6 minus 10)
] end if
>>[>] if current cell (6/7 for 1/2 digits) non-0 goto cell 8
>[+++++[->++++++++<]>.<] if on cell 6 print '0'
"""