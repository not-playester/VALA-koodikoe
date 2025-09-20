import sys

def find_multiples(a, b, limit):
    # Return sorted list of multiples of a or b less than limit.
    multiples = set()
    for n in range(1, limit):
        if n % a == 0 or n % b == 0:
            multiples.add(n)
    return sorted(multiples)

def main():
    if len(sys.argv) != 3:
        print("Usage: python my_program.py input.txt output.txt")
        sys.exit(1)

    input_file, output_file = sys.argv[1], sys.argv[2]
    results = []
    errors = []

    try:
        with open(input_file, "r") as f:
            for line_number, line in enumerate(f, start=1):
                if not line.strip():
                    continue  # skip empty lines

                parts = line.strip().split()

                # Check if row has exactly 3 numbers
                if len(parts) != 3:
                    errors.append(f"Line {line_number}: expected 3 numbers, got {len(parts)}")
                    continue  # skip this line, but continue processing others

                # Validate all parts are integers
                try:
                    a, b, limit = map(int, parts)
                except ValueError:
                    errors.append(f"Line {line_number}: all values must be integers")
                    continue # skip this line, but continue processing others

                multiples = find_multiples(a, b, limit)
                results.append((limit, multiples))
    except FileNotFoundError:
        print(f"Error: input file '{input_file}' not found.")
        sys.exit(1)

    # Sort results by number of multiples
    results.sort(key=lambda x: len(x[1]))

    # Write successful results to file
    try:
        with open(output_file, "w") as f:
            for limit, multiples in results:
                line = f"{limit}:{' '.join(map(str, multiples))}"
                f.write(line + "\n")
    except IOError:
        print(f"Error: could not write to output file '{output_file}'.")
        sys.exit(1)

    # --- Print to screen with section headers ---
    if results:
        print("✅ Successful rows:")
        for limit, multiples in results:
            line = f"{limit}:{' '.join(map(str, multiples))}"
            print(line)

    if errors:
        print("\n⚠ Some rows had problems:")
        for err in errors:
            print(err)

if __name__ == "__main__":
    main()
