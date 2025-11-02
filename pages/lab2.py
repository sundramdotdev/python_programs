import streamlit as st

st.title("Welcome to Python programs")

# ---------------------------

# ---------------------------
# Main Heading
# ---------------------------
st.title("🧠 Data Types in Python")
# ---------------------------
# Q1
# ---------------------------
st.subheader("Q1. Display the type of different data values")

st.code("""
# Program to display the type of different data values

a = 10          # Integer
b = 3.14        # Float
c = "Python"    # String
d = True        # Boolean
e = [1, 2, 3]   # List

# Printing the types
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
""", language='python')

if st.button("Run Q1"):
    a, b, c, d, e = 10, 3.14, "Python", True, [1, 2, 3]
    st.write(type(a), type(b), type(c), type(d), type(e))


# ---------------------------
# Q2
# ---------------------------
st.subheader("Q2. Add two numbers entered by the user")

st.code("""
# Program to add two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum is:", num1 + num2)
""", language='python')

if st.button("Run Q2"):
    num1, num2 = 5, 7
    st.write("Sum is:", num1 + num2)


# ---------------------------
# Q3
# ---------------------------
st.subheader("Q3. Convert integer to float and vice versa")

st.code("""
# Type conversion between int and float

x = 5
y = 3.7

# Converting types
a = float(x)
b = int(y)

print(a)
print(b)
""", language='python')

if st.button("Run Q3"):
    x, y = 5, 3.7
    st.write(float(x), int(y))


# ---------------------------
# Q4
# ---------------------------
st.subheader("Q4. Create and print a list of fruits")

st.code("""
# Working with lists

fruits = ["Apple", "Banana", "Mango"]
print("Fruit list:", fruits)
print("First fruit:", fruits[0])
""", language='python')

if st.button("Run Q4"):
    fruits = ["Apple", "Banana", "Mango"]
    st.write("Fruit list:", fruits)
    st.write("First fruit:", fruits[0])


# ---------------------------
# Q5
# ---------------------------
st.subheader("Q5. Create and print a tuple of numbers")

st.code("""
# Tuple example (immutable data type)

numbers = (1, 2, 3, 4, 5)
print("Tuple elements:", numbers)
""", language='python')

if st.button("Run Q5"):
    numbers = (1, 2, 3, 4, 5)
    st.write("Tuple elements:", numbers)


# ---------------------------
# Q6
# ---------------------------
st.subheader("Q6. Create and print a dictionary")

st.code("""
# Dictionary example (key-value pairs)

student = {
    "name": "Shubham",
    "age": 19,
    "course": "Python"
}
print(student)
print("Student name:", student["name"])
""", language='python')

if st.button("Run Q6"):
    student = {"name": "Shubham", "age": 19, "course": "Python"}
    st.write(student)
    st.write("Student name:", student["name"])


# ---------------------------
# Q7
# ---------------------------
st.subheader("Q7. Create and print a set")

st.code("""
# Set example (unordered and unique)

colors = {"red", "green", "blue", "red"}
print("Set elements:", colors)
""", language='python')

if st.button("Run Q7"):
    colors = {"red", "green", "blue", "red"}
    st.write("Set elements:", colors)


# ---------------------------
# Q8
# ---------------------------
st.subheader("Q8. Working with Boolean values")

st.code("""
# Boolean data type example

a = True
b = False
print("a AND b:", a and b)
print("a OR b:", a or b)
print("NOT a:", not a)
""", language='python')

if st.button("Run Q8"):
    a, b = True, False
    st.write("a AND b:", a and b)
    st.write("a OR b:", a or b)
    st.write("NOT a:", not a)


# ---------------------------
# Q9
# ---------------------------
st.subheader("Q9. Convert string to list")

st.code("""
# Converting string to list

text = "PYTHON"
letters = list(text)
print("List of letters:", letters)
""", language='python')

if st.button("Run Q9"):
    text = "PYTHON"
    letters = list(text)
    st.write("List of letters:", letters)


# ---------------------------
# Q10
# ---------------------------
st.subheader("Q10. Check data type dynamically")

st.code("""
# Checking data type using isinstance()

x = 100
y = "Sundram gupta"
z = [1, 3, 8]

print(isinstance(x, int))
print(isinstance(y, str))
print(isinstance(z, list))
""", language='python')

if st.button("Run Q10"):
    x, y, z = 100, "Sundram gupta", [1, 3, 8]
    st.write(isinstance(x, int))
    st.write(isinstance(y, str))
    st.write(isinstance(z, list))   

# --- Next Page Button ---
if st.button("Next ➡️"):
    st.switch_page("pages/lab3.py") # You can change to 'operators.py' or 'data_types.py'
if st.button("Home 🏠"):
    st.switch_page("py_programs.py")
# --- Footer ---
st.markdown("---")
st.caption("🧡 Made with Streamlit | 📚 Practice • Learn • Improve")
