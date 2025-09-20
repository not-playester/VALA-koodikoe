# Multiples of A and B

This program finds all multiples of two numbers **A** and **B** that are **less than a goal number**.  

- Reads an input file containing rows with three numbers:  
  ```
  A B goal
  ```
- For each row, finds all multiples of `A` or `B` that are `< goal`.  
- Prints results to the screen and writes them to an output file.  
- Results are **sorted by how many multiples were found (ascending order)**.  
- Handles errors gracefully:  
  - If a row has too many/few numbers.  
  - If values are not integers.  
  - If input/output files can’t be read/written.  

---

## Usage

```bash
python my_program.py <input_file> <output_file>
```

- `<input_file>` → file with rows of three numbers (`A B goal`).
- `<output_file>` → store end result.

---

## Example

### Good input file: `input.txt`
```
5 8 31
4 7 20
```

### Run
```bash
python my_program.py input.txt output.txt
```

### Screen output
```
✅ Successful rows:
20:4 7 8 12 14 16
31:5 8 10 15 16 20 24 25 30
```

### Output file: `output.txt`
```
20:4 7 8 12 14 16
31:5 8 10 15 16 20 24 25 30
```

---

## Error Handling

If the input file has incorrect rows, they will be skipped and reported at the end.  

### Bad input file: `input.txt`
```
5 8 31
4 7 20
4 7 20 99
10 kissa 40
3 6 
8 9 52
```

### Run
```bash
python my_program.py input.txt output.txt
```

### Screen output
```
✅ Successful rows:
20:4 7 8 12 14 16
31:5 8 10 15 16 20 24 25 30
52:8 9 16 18 24 27 32 36 40 45 48

⚠ Some rows had problems:
Line 3: expected 3 numbers, got 4
Line 4: all values must be integers
Line 5: expected 3 numbers, got 2
```

### Output file: `output.txt`
```
20:4 7 8 12 14 16
31:5 8 10 15 16 20 24 25 30
52:8 9 16 18 24 27 32 36 40 45 48
```

## Requirements

- Python 3.x
- No external libraries required 
