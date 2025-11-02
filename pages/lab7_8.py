import streamlit as st
from datetime import datetime
import math
import sys

st.set_page_config(page_title="Structures | Python Programs", page_icon="🧩", layout="wide")

# ---- Title ----
st.title("🧩 Structures - Advanced Level Python Programs")
st.markdown("---")

st.write("Here are **20 advanced-level Python programs** covering topics like numbers, strings, lists, tuples, dictionaries, modules, date & time, and functions.")

# ===================== Q1 =====================
st.subheader("Q1️⃣ Program to find factorial using recursion")
code1 = """
# Function to find factorial using recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = 5
print("Factorial of", num, "is:", factorial(num))
"""
st.code(code1, language="python")

# ===================== Q2 =====================
st.subheader("Q2️⃣ Program to count vowels and consonants in a string")
code2 = """
string = "StreamlitApp"
vowels = "aeiouAEIOU"
v_count = sum(1 for c in string if c in vowels)
c_count = len(string) - v_count
print("Vowels:", v_count, "| Consonants:", c_count)
"""
st.code(code2, language="python")

# ===================== Q3 =====================
st.subheader("Q3️⃣ Program to find maximum and minimum in a list")
code3 = """
numbers = [45, 22, 88, 12, 7, 99]
print("Max:", max(numbers))
print("Min:", min(numbers))
"""
st.code(code3, language="python")

# ===================== Q4 =====================
st.subheader("Q4️⃣ Program to reverse a tuple")
code4 = """
tup = (10, 20, 30, 40)
rev_tup = tup[::-1]
print("Reversed tuple:", rev_tup)
"""
st.code(code4, language="python")

# ===================== Q5 =====================
st.subheader("Q5️⃣ Program to merge two dictionaries")
code5 = """
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = dict1 | dict2  # Python 3.9+
print("Merged Dictionary:", merged)
"""
st.code(code5, language="python")

# ===================== Q6 =====================
st.subheader("Q6️⃣ Program to check Armstrong number")
code6 = """
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
"""
st.code(code6, language="python")

# ===================== Q7 =====================
st.subheader("Q7️⃣ Program to count frequency of elements in list")
code7 = """
from collections import Counter
data = [1, 2, 2, 3, 4, 4, 4, 5]
freq = Counter(data)
print(freq)
"""
st.code(code7, language="python")

# ===================== Q8 =====================
st.subheader("Q8️⃣ Program to convert string to list and list to string")
code8 = """
s = "Python"
lst = list(s)
print("String to List:", lst)
print("List to String:", ''.join(lst))
"""
st.code(code8, language="python")

# ===================== Q9 =====================
st.subheader("Q9️⃣ Program to find even and odd numbers using list comprehension")
code9 = """
nums = [1,2,3,4,5,6,7,8,9,10]
even = [n for n in nums if n%2==0]
odd = [n for n in nums if n%2!=0]
print("Even:", even)
print("Odd:", odd)
"""
st.code(code9, language="python")

# ===================== Q10 =====================
st.subheader("Q🔟 Program to check palindrome string")
code10 = """
text = "madam"
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
"""
st.code(code10, language="python")

# ===================== Q11 =====================
st.subheader("Q11️⃣ Program to find sum of digits of a number")
code11 = """
num = 12345
sum_digits = sum(int(d) for d in str(num))
print("Sum of digits:", sum_digits)
"""
st.code(code11, language="python")

# ===================== Q12 =====================
st.subheader("Q12️⃣ Program to find largest word in a string")
code12 = """
sentence = "Python makes coding interesting"
words = sentence.split()
largest = max(words, key=len)
print("Largest word:", largest)
"""
st.code(code12, language="python")

# ===================== Q13 =====================
st.subheader("Q13️⃣ Program to demonstrate default arguments in a function")
code13 = """
def greet(name="User"):
    print("Hello,", name)

greet()
greet("Sundram")
"""
st.code(code13, language="python")

# ===================== Q14 =====================
st.subheader("Q14️⃣ Program to demonstrate exit() function")
code14 = """
import sys
print("Program Started")
sys.exit("Exiting the program manually")
print("This line will not execute")
"""
st.code(code14, language="python")

# ===================== Q15 =====================
st.subheader("Q15️⃣ Program to print current date and time")
code15 = """
from datetime import datetime
now = datetime.now()
print("Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))
"""
st.code(code15, language="python")

# ===================== Q16 =====================
st.subheader("Q16️⃣ Program to calculate area of circle using math module")
code16 = """
import math
r = 7
area = math.pi * r ** 2
print("Area of Circle:", area)
"""
st.code(code16, language="python")

# ===================== Q17 =====================
st.subheader("Q17️⃣ Program to remove duplicates from a list")
code17 = """
nums = [1,2,2,3,4,4,5]
unique = list(set(nums))
print("Unique List:", unique)
"""
st.code(code17, language="python")

# ===================== Q18 =====================
st.subheader("Q18️⃣ Program to sort dictionary by value")
code18 = """
d = {'a':3,'b':1,'c':2}
sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
print("Sorted Dict:", sorted_dict)
"""
st.code(code18, language="python")

# ===================== Q19 =====================
st.subheader("Q19️⃣ Program to check leap year")
code19 = """
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
"""
st.code(code19, language="python")

# ===================== Q20 =====================
st.subheader("Q20️⃣ Program to create a module and import it")
code20 = """
# Create a file named mymodule.py with:
# def say_hello(name):
#     print("Hello", name)

# Then import and use it:
import mymodule
mymodule.say_hello("Sundram")
"""
st.code(code20, language="python")

# --- Navigation Buttons (Previous, Home, Next) ---
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⬅️ Previous"):
        st.switch_page("pages/lab6.py")  # Previous page

with col2:
    if st.button("🏠 Home"):
        st.switch_page("py_programs.py")  # Go to Home

with col3:
    if st.button("➡️ Next"):
        st.switch_page("pages/lab9_10.py")  # Next page

# ---- Footer ----
st.markdown("---")
st.caption("💡 Created by Sundram Gupta | Advanced Python Practice 💻")


# ---- Footer ----
st.markdown("---")
st.caption("💡 Made with ❤️ using Streamlit | Practice • Learn • Build • Repeat 🔁")

