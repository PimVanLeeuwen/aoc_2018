import importlib
import os

# Dynamically find the correct file for the python rendering
def run_day(day: int, part: int, input_data: str) -> str:
    try:
        module_name = f"days.day{day:02d}"
        day_module = importlib.import_module(module_name)
        func_name = f"solve_part{part}"
        solve_func = getattr(day_module, func_name)
        return solve_func(input_data)
    except ModuleNotFoundError:
        return f"Day {day:02d} not implemented."
    except Exception as e:
        return f"Error running Day {day:02d} Part {part}: {e}"

# load the input
def load_input(day: int) -> str:
    input_path = os.path.join(".inputs", f"day{day:02d}.txt")
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    with open(input_path, "r") as f:
        return f.read().strip()

def main():
    try:
        day = int(input("Enter day (1–25): "))
        part = int(input("Enter part (1 or 2): "))
        input_data = load_input(day)
        result = run_day(day, part, input_data)
        print(f"\nResult for Day {day:02d} Part {part}:\n{result}")
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()