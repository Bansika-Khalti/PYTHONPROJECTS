# Python project using int, float, string, boolean, concatenation

# --- Input numbers ---
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# --- Arithmetic operations ---
sum_result = num1 + num2
diff_result = num1 - num2
mult_result = num1 * num2
div_result = num1 / num2

# --- Boolean check ---
is_greater = num1 > num2

# --- Text output with concatenation ---
print("\nResults:")
print("Sum: " + str(sum_result))
print("Difference: " + str(diff_result))
print("Multiplication: " + str(mult_result))
print("Division: " + str(div_result))
print("Is first number greater than second? " + str(is_greater))

# --- Example of text concatenation ---
name = input("\nEnter your name: ")
greeting = "Hello, " + name + "! Your calculations are complete."
print(greeting)