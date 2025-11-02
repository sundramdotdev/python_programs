import streamlit as st

# ---------------------------
# Streamlit Page Setup
# ---------------------------
st.set_page_config(page_title="Python Flow Control - Beginner Level", layout="wide")

# ---------------------------
# Page Title
# ---------------------------
st.title("🔁 Flow Control")
st.write("This Streamlit app shows **10 beginner-level Python programs** demonstrating flow control statements such as `if`, `else`, `elif`, `for`, `while`, and more — each with explanations and unique run buttons.")

# Helper function for displaying outputs
def show_output(lines):
    for line in lines:
        st.write(line)

# ---------------------------
# Q1
# ---------------------------
st.subheader("Q1. Check if a number is positive, negative, or zero")

st.code("""
# Using if-elif-else to check number type
num = 5
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
""", language='python')

if st.button("Run Q1", key="q1"):
    num = 5
    if num > 0:
        show_output(["Positive number"])
    elif num == 0:
        show_output(["Zero"])
    else:
        show_output(["Negative number"])

# ---------------------------
# Q2
# ---------------------------
st.subheader("Q2. Find the largest of two numbers")

st.code("""
# Using if-else to compare two numbers
a = 10
b = 20
if a > b:
    print("A is greater")
else:
    print("B is greater")
""", language='python')

if st.button("Run Q2", key="q2"):
    a, b = 10, 20
    if a > b:
        show_output(["A is greater"])
    else:
        show_output(["B is greater"])

# ---------------------------
# Q3
# ---------------------------
st.subheader("Q3. Check if a number is even or odd")

st.code("""
# Using modulus operator with if-else
num = 7
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
""", language='python')

if st.button("Run Q3", key="q3"):
    num = 7
    if num % 2 == 0:
        show_output(["Even number"])
    else:
        show_output(["Odd number"])

# ---------------------------
# Q4
# ---------------------------
st.subheader("Q4. Check if a year is a leap year")

st.code("""
# Leap year: divisible by 4 but not by 100, except divisible by 400
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
""", language='python')

if st.button("Run Q4", key="q4"):
    year = 2024
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        show_output(["Leap Year"])
    else:
        show_output(["Not a Leap Year"])

# ---------------------------
# Q5
# ---------------------------
st.subheader("Q5. Print numbers from 1 to 5 using a for loop")

st.code("""
# Using a for loop with range()
for i in range(1, 6):
    print(i)
""", language='python')

if st.button("Run Q5", key="q5"):
    show_output([i for i in range(1, 6)])

# ---------------------------
# Q6
# ---------------------------
st.subheader("Q6. Calculate the sum of first 10 natural numbers using a while loop")

st.code("""
# Using while loop
i = 1
total = 0
while i <= 10:
    total += i
    i += 1
print("Sum:", total)
""", language='python')

if st.button("Run Q6", key="q6"):
    i, total = 1, 0
    while i <= 10:
        total += i
        i += 1
    show_output([f"Sum: {total}"])

# ---------------------------
# Q7
# ---------------------------
st.subheader("Q7. Print multiplication table of 5")

st.code("""
# Using for loop to print table of 5
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
""", language='python')

if st.button("Run Q7", key="q7"):
    num = 5
    show_output([f"{num} x {i} = {num*i}" for i in range(1, 11)])

# ---------------------------
# Q8
# ---------------------------
st.subheader("Q8. Demonstrate the use of break statement")

st.code("""
# The loop stops when i == 3
for i in range(1, 6):
    if i == 3:
        break
    print(i)
""", language='python')

if st.button("Run Q8", key="q8"):
    output = []
    for i in range(1, 6):
        if i == 3:
            break
        output.append(i)
    show_output(output)

# ---------------------------
# Q9
# ---------------------------
st.subheader("Q9. Demonstrate the use of continue statement")

st.code("""
# The loop skips printing when i == 3
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
""", language='python')

if st.button("Run Q9", key="q9"):
    output = []
    for i in range(1, 6):
        if i == 3:
            continue
        output.append(i)
    show_output(output)

# ---------------------------
# Q10
# ---------------------------
st.subheader("Q10. Find factorial of a number using for loop")

st.code("""
# Factorial using for loop
num = 5
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial:", fact)
""", language='python')

if st.button("Run Q10", key="q10"):
    num, fact = 5, 1
    for i in range(1, num + 1):
        fact *= i
    show_output([f"Factorial: {fact}"])

# ---------------------------
# End of File
# ---------------------------
# --- Next Page Button ---
if st.button("Next ➡️"):
    st.switch_page("pages/lab5.py") # You can change to 'operators.py' or 'data_types.py'
if st.button("Home 🏠"):
    st.switch_page("py_programs.py")
# --- Footer ---
st.markdown("---")
st.caption("🧡 Made with Streamlit | 📚 Practice • Learn • Improve")
