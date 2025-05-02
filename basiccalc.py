firstnumber= float(input("what is your first number? "))
secondnumber= float(input("what is your second number? "))
operation= (input("what is your operation sign (+, -, *, /)? "))
if operation=="+":
 result= firstnumber + secondnumber
 print(f"your result is {result}")
elif operation=="-":
 result= secondnumber - firstnumber
 print(f"your result is {result}")
elif operation== "*":
  result= firstnumber * secondnumber
  print(f"your result is {result}")
elif operation== "/":
  result= secondnumber - firstnumber
  print(f"your result is {result}")
else:
  print("invalid operation")
