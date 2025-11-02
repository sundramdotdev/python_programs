import streamlit as st

st.title("Welcome to Python programs")


# ---------------------------
# Main Heading
# ---------------------------
st.title("🧮 Operators")
st.write("10 beginner-level Python programs demonstrating different operators. Each question (Q1–Q10) has a Run button. Every button uses a unique key to avoid Streamlit widget errors.")

# Helper: display outputs in a consistent way
def show_output(lines):
    for line in lines:
        st.write(line)

# ---------------------------
# Q1
# ---------------------------
st.subheader("Q1. Arithmetic Operators")

st.code("""
# Arithmetic operators perform mathematical operations
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
""", language='python')

if st.button("Run Q1 - Arithmetic", key="run_q1"):
    a, b = 10, 3
    show_output([
        f"Addition: {a + b}",
        f"Subtraction: {a - b}",
        f"Multiplication: {a * b}",
        f"Division: {a / b}",
        f"Floor Division: {a // b}",
        f"Modulus: {a % b}",
        f"Exponentiation: {a ** b}",
    ])

# ---------------------------
# Q2
# ---------------------------
st.subheader("Q2. Comparison Operators")

st.code("""
# Comparison operators compare two values and return Boolean results
x = 5
y = 8

print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)
""", language='python')

if st.button("Run Q2 - Comparison", key="run_q2"):
    x, y = 5, 8
    show_output([
        f"x == y: {x == y}",
        f"x != y: {x != y}",
        f"x > y: {x > y}",
        f"x < y: {x < y}",
        f"x >= y: {x >= y}",
        f"x <= y: {x <= y}",
    ])

# ---------------------------
# Q3
# ---------------------------
st.subheader("Q3. Logical Operators")

st.code("""
# Logical operators: and, or, not
a = True
b = False

print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)
""", language='python')

if st.button("Run Q3 - Logical", key="run_q3"):
    a, b = True, False
    show_output([
        f"a and b: {a and b}",
        f"a or b: {a or b}",
        f"not a: {not a}",
    ])

# ---------------------------
# Q4
# ---------------------------
st.subheader("Q4. Assignment Operators")

st.code("""
# Assignment operators are used to assign and update values
a = 10
a += 5  # a = a + 5
a -= 3  # a = a - 3
a *= 2  # a = a * 2
a /= 4  # a = a / 4
print(a)
""", language='python')

if st.button("Run Q4 - Assignment", key="run_q4"):
    a = 10
    a += 5
    after_add = a
    a -= 3
    after_sub = a
    a *= 2
    after_mul = a
    a /= 4
    after_div = a
    show_output([
        f"After += 5: {after_add}",
        f"After -= 3: {after_sub}",
        f"After *= 2: {after_mul}",
        f"After /= 4: {after_div}",
    ])

# ---------------------------
# Q5
# ---------------------------
st.subheader("Q5. Bitwise Operators")

st.code("""
# Bitwise operators work on binary representation of integers
a = 5   # 0b0101
b = 3   # 0b0011

print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT a:", ~a)
print("Left Shift (a<<1):", a << 1)
print("Right Shift (a>>1):", a >> 1)
""", language='python')

if st.button("Run Q5 - Bitwise", key="run_q5"):
    a, b = 5, 3
    show_output([
        f"AND: {a & b}",
        f"OR: {a | b}",
        f"XOR: {a ^ b}",
        f"NOT a: {~a}",
        f"Left Shift (a<<1): {a << 1}",
        f"Right Shift (a>>1): {a >> 1}",
    ])

# ---------------------------
# Q6
# ---------------------------
st.subheader("Q6. Membership Operators")

st.code("""
# Membership operators check presence in a collection
fruits = ['apple', 'banana', 'mango']

print('apple' in fruits)      # True
print('orange' not in fruits) # True
""", language='python')

if st.button("Run Q6 - Membership", key="run_q6"):
    fruits = ['apple', 'banana', 'mango']
    show_output([
        f"Is 'apple' in fruits? {'apple' in fruits}",
        f"Is 'orange' not in fruits? {'orange' not in fruits}",
    ])

# ---------------------------
# Q7
# ---------------------------
st.subheader("Q7. Identity Operators")

st.code("""
# Identity operators compare object identity (memory location)
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)      # True
print(x is z)      # False (different objects)
print(x is not z)  # True
""", language='python')

if st.button("Run Q7 - Identity", key="run_q7"):
    x = [1, 2, 3]
    y = x
    z = [1, 2, 3]
    show_output([
        f"x is y: {x is y}",
        f"x is z: {x is z}",
        f"x is not z: {x is not z}",
    ])

# ---------------------------
# Q8
# ---------------------------
st.subheader("Q8. Operator Precedence Example")

st.code("""
# Precedence determines which operations run first
result = 10 + 2 * 5   # multiplication first -> 20
result2 = (10 + 2) * 5  # parentheses change order -> 60
""", language='python')

if st.button("Run Q8 - Precedence", key="run_q8"):
    result = 10 + 2 * 5
    result2 = (10 + 2) * 5
    show_output([
        f"Result (10 + 2 * 5): {result}",
        f"Result2 ((10 + 2) * 5): {result2}",
    ])

# ---------------------------
# Q9
# ---------------------------
st.subheader("Q9. Using Operators in Conditions")

st.code("""
# Combining comparison and logical operators in conditions
age = 18
marks = 75

if age >= 18 and marks > 60:
    print("You are eligible!")
else:
    print("Not eligible.")
""", language='python')

if st.button("Run Q9 - Conditions", key="run_q9"):
    age, marks = 18, 75
    if age >= 18 and marks > 60:
        show_output(["You are eligible!"])
    else:
        show_output(["Not eligible."])

# ---------------------------
# Q10
# ---------------------------
st.subheader("Q10. Chained Comparisons")

st.code("""
# Chained comparisons make multiple comparisons readable
x = 10
print(5 < x < 15)  # True if x > 5 AND x < 15
""", language='python')

if st.button("Run Q10 - Chained", key="run_q10"):
    x = 10
    show_output([f"5 < x < 15 : {5 < x < 15}"])

# ---------------------------
# End of File
# ---------------------------
# --- Next Page Button ---
if st.button("Next ➡️"):
    st.switch_page("pages/lab4.py") # You can change to 'operators.py' or 'data_types.py'
if st.button("Home 🏠"):
    st.switch_page("py_programs.py")
# --- Footer ---
st.markdown("---")
st.caption("🧡 Made with Streamlit | 📚 Practice • Learn • Improve")

