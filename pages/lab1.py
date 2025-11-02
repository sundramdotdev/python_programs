import streamlit as st

st.title("LAB 1")
st.subheader('Q1.'  \
' WAPP to find the largest of three numbers.')
st.code("""# Largest of three numbers
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))
        
if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest", b)
else:
    print("Largest", c) """)

st.subheader("Q1" \
"WAPP to check whether a number is prime or not.")
st.code("""num = int(input('Enter a number: '))
if num > 1:
    for i range(2, num):
        if num % i == 0:
        print(num,'is not prime')
    else:
        print(num, 'is prime')
else:
    print(num,'is not prime')
 """)

st.subheader("Q3." \
"WAPP to find factorial of a number using recursion.")
st.code("""def factorial(n):
    if n == 0 or n == 1:  #Base case
        return 1
    return n * factorial(n - 1)  # Recursive call

n = int(input('Enter a number: '))
print("Factorial:", factorial(n))
""")

st.subheader("Q4." \
"WAPP to print Fibonacci series up to N terms.")
st.code("""n = int(input("Enter a number: "))
a, b = 0, 1
print("Fibonacci series:", end=" ")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
""")

st.subheader("Q5." \
"WAPP to check if a string ia palindrome.")
st.code("""s = input("Enter a word: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
        """)

st.subheader("Q6." \
"WAPP to calculate sum of digits of a number")
st.code("""num = int(input("Enter a number: "))
s = 0
while num > 0:
    s += num % 10
    num //= 10
print("Sum of digits:", s)
""")

st.subheader("Q7." \
"WAPP to to count vowels in a given string.")
st.code("""s = input("Enter a word: ")
vowels = "aeiou"
count = o
for ch in s:
    if ch in vowels:
        count += 1
print("Number of vowels:", count)       
""")

st.subheader("Q8." \
"WAPP to reverse a number.")
st.code("""num = int(input("Enter a number: "))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("Reversed number:", rev)
""")

st.subheader("Q9." \
"WAPP to add two matrices.")
st.code("""A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

result = [[0, 0], [0, 0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]

print("Matrix Addison:")
for row in result:
    print(row)
""")

st.subheader("Q10." \
"WAPP to count frequency of words in a given string.")
st.code("""s = input("Enter a sentence: ")
freq = {}

for word in s:
    freq[word] = freq.get(word, 0) + 1
        
print("Word Frequency:")
for k, v in freq.items():
    print(k, ":", v)
""")

# --- Next Page Button ---
if st.button("Next ➡️"):
    st.switch_page("pages/lab2.py") # You can change to 'operators.py' or 'data_types.py'
if st.button("Home 🏠"):
    st.switch_page("py_programs.py") # You can change to 'operators.py' or 'data_types.py'


# --- Footer ---
st.markdown("---")
st.caption("🧡 Made with Streamlit | 📚 Practice • Learn • Improve")
