
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator:  "))
    result = a/b
    print(result)
except Exception as e:
    print(f"An error occured. {e}")

finally:
    print("Closed of operation")
print("End of execution")
