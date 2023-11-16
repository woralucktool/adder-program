def add_numbers(num1, num2):
  """Adds two numbers and returns the sum."""
  return num1 + num2

def main():
  num1 = int(input("Enter the first number: "))
  num2 = int(input("Enter the second number: "))

  sum = add_numbers(num1, num2)
  print("The sum of the two numbers is:", sum)

if __name__ == "__main__":
  main()
  
