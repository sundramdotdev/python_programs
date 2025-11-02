import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Advance Patterns", page_icon="🌟", layout="centered")

# --- Main Heading ---
st.title("🌟 Patterns – Advanced Flow Control in Python")
st.markdown("### 💡 Explore Star & Numeric Patterns with Advanced Logic")

st.markdown("---")

# ============================
#         Q1 to Q10
# ============================

# --- Pattern Programs (5 Star/Numeric) ---
st.subheader("Q1️⃣: Star Pyramid Pattern")
st.code("""
# Print pyramid pattern of stars
rows = 5
for i in range(rows):
    print(' ' * (rows - i - 1) + '*' * (2 * i + 1))
""", language="python")

st.subheader("Q2️⃣: Inverted Star Pyramid Pattern")
st.code("""
# Inverted pyramid of stars
rows = 5
for i in range(rows, 0, -1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))
""", language="python")

st.subheader("Q3️⃣: Numeric Increasing Triangle Pattern")
st.code("""
# Numbers increase in each row
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
""", language="python")

st.subheader("Q4️⃣: Numeric Palindrome Pyramid")
st.code("""
# Print numeric palindrome pyramid pattern
rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(' ', end='')
    for j in range(1, i + 1):
        print(j, end='')
    for j in range(i - 1, 0, -1):
        print(j, end='')
    print()
""", language="python")

st.subheader("Q5️⃣: Diamond Star Pattern")
st.code("""
# Diamond pattern using two loops
rows = 5
for i in range(rows):
    print(' ' * (rows - i - 1) + '*' * (2 * i + 1))
for i in range(rows - 2, -1, -1):
    print(' ' * (rows - i - 1) + '*' * (2 * i + 1))
""", language="python")

# --- Divider ---
st.markdown("### 🔁 Other Advanced Flow Control Programs")

# --- 5 Other Flow Control Programs ---
st.subheader("Q6️⃣: Program to Check Prime Numbers in Range")
st.code("""
# Check and print prime numbers from 10 to 50
for num in range(10, 51):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=' ')
""", language="python")

st.subheader("Q7️⃣: Fibonacci Series using Loop")
st.code("""
# Generate Fibonacci sequence up to n terms
n = 10
a, b = 0, 1
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
""", language="python")

st.subheader("Q8️⃣: Armstrong Number Checker")
st.code("""
# Check if a number is an Armstrong number
num = 153
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
""", language="python")

st.subheader("Q9️⃣: Factorial using Recursion")
st.code("""
# Recursive function to find factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = 6
print("Factorial of", num, "is", factorial(num))
""", language="python")

st.subheader("Q🔟: Sum of Digits using While Loop")
st.code("""
# Find the sum of digits of a number
num = 9876
total = 0
while num > 0:
    total += num % 10
    num //= 10
print("Sum of digits =", total)
""", language="python")

# --- Divider Line ---
st.markdown("---")

# --- Navigation Buttons (Previous, Home, Next) ---
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⬅️ Previous"):
        st.switch_page("pages/lab5.py")  # Previous page

with col2:
    if st.button("🏠 Home"):
        st.switch_page("py_programs.py")  # Go to Home

with col3:
    if st.button("➡️ Next"):
        st.switch_page("pages/lab7_8.py")

# --- Footer ---
st.markdown("---")
st.caption("🌟 Patterns & Flow Control • 💡 Practice • 🧠 Learn • 🚀 Master Python")
