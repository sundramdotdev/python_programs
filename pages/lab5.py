import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Advance Level Python", page_icon="⚙️", layout="centered")

# --- Main Title ---
st.title("⚙️ Advance Level Python Programs 🐍")
st.markdown("### 🚀 Explore Advanced Concepts of Flow Control, Data Types & Operators")

st.markdown("---")

# --- Q1 to Q10 Programs ---

st.subheader("Q1️⃣ Program to find factorial using recursion")
st.code("""
def factorial(n):
    # Base case: if n is 1 or 0, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive call
    else:
        return n * factorial(n - 1)

num = 6
print("Factorial of", num, "is", factorial(num))
""", language="python")


st.subheader("Q2️⃣ Program to check if a string is a palindrome")
st.code("""
string = "level"
# Reverse the string and compare
if string == string[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
""", language="python")


st.subheader("Q3️⃣ Program to find sum of even and odd numbers separately in a list")
st.code("""
nums = [10, 3, 5, 8, 12, 7]
even_sum = sum([x for x in nums if x % 2 == 0])
odd_sum = sum([x for x in nums if x % 2 != 0])
print("Even Sum:", even_sum, "Odd Sum:", odd_sum)
""", language="python")


st.subheader("Q4️⃣ Program to find the largest element in a list without using max()")
st.code("""
nums = [12, 45, 23, 78, 56]
largest = nums[0]
for n in nums:
    if n > largest:
        largest = n
print("Largest:", largest)
""", language="python")


st.subheader("Q5️⃣ Program to count frequency of elements using dictionary")
st.code("""
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
freq = {}
for i in items:
    freq[i] = freq.get(i, 0) + 1
print(freq)
""", language="python")


st.subheader("Q6️⃣ Program to find prime numbers in a range using for-else loop")
st.code("""
for num in range(10, 30):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=' ')
""", language="python")


st.subheader("Q7️⃣ Program to demonstrate bitwise operations")
st.code("""
a, b = 10, 4
print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("Left Shift a by 2:", a << 2)
print("Right Shift a by 2:", a >> 2)
""", language="python")


st.subheader("Q8️⃣ Program to swap two numbers without using a third variable")
st.code("""
a, b = 5, 10
a, b = b, a
print("a =", a, "b =", b)
""", language="python")


st.subheader("Q9️⃣ Program to flatten a nested list")
st.code("""
nested = [[1,2], [3,4], [5,6]]
flat = [x for sublist in nested for x in sublist]
print("Flattened List:", flat)
""", language="python")


st.subheader("Q🔟 Program to find common elements in two lists using set")
st.code("""
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
common = list(set(a) & set(b))
print("Common Elements:", common)
""", language="python")


# --- Divider ---
st.markdown("---")

# --- Navigation Buttons ---
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⬅️ Previous"):
        st.switch_page("pages/lab4.py")  # previous page

with col2:
    if st.button("🏠 Home"):
        st.switch_page("py_programs.py")  # main home page file

with col3:
    if st.button("➡️ Next"):
        st.switch_page("pages/lab6.py")  # No next page yet

# --- Footer ---
st.markdown("---")
st.caption("⚙️ Advanced Level • 💡 Practice • 🧠 Learn • 🐍 Python Power")
