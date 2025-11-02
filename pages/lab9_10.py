import streamlit as st
import re
import tkinter as tk

st.set_page_config(page_title="Introduction to Advanced Python", page_icon="🚀", layout="wide")

# ---- Title ----
st.title("🚀 Introduction to Advanced Python")
st.markdown("---")
st.write("""
Explore **20 advanced Python programs** covering:
- 🧱 Objects & Classes  
- 🧬 Inheritance  
- 🔍 Regular Expressions  
- ⚡ Event-Driven Programming  
- 🖥️ GUI Programming (Tkinter)
""")
st.markdown("---")

# ---- Helper to create code blocks with run buttons ----
def show_program(q_num, title, code):
    st.subheader(f"Q{q_num}️⃣ {title}")
    st.code(code, language="python")
    run_key = f"run_{q_num}"
    if st.button(f"▶️ Run Q{q_num}", key=run_key):
        st.info("Output (see console for GUI or RE results):")
        try:
            exec(code)
        except Exception as e:
            st.error(e)

# ========================= OBJECTS & CLASSES =========================

show_program(1, "Create a class and an object",
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

s1 = Student("Sundram", 19)
s1.display()
""")

show_program(2, "Use of class variables and instance variables",
"""
class Car:
    wheels = 4  # class variable

    def __init__(self, brand):
        self.brand = brand  # instance variable

c1 = Car("BMW")
c2 = Car("Audi")

print(c1.brand, Car.wheels)
print(c2.brand, Car.wheels)
""")

show_program(3, "Constructor and Destructor demo",
"""
class Demo:
    def __init__(self):
        print("Constructor Called!")
    def __del__(self):
        print("Destructor Called!")

obj = Demo()
del obj
""")

show_program(4, "Multiple Objects with methods",
"""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def show(self):
        print(f"{self.name} earns {self.salary}")

e1 = Employee("Amit", 25000)
e2 = Employee("Riya", 30000)
e1.show()
e2.show()
""")

# ========================= INHERITANCE =========================

show_program(5, "Single Inheritance",
"""
class Parent:
    def func1(self):
        print("This is parent class")

class Child(Parent):
    def func2(self):
        print("This is child class")

obj = Child()
obj.func1()
obj.func2()
""")

show_program(6, "Multiple Inheritance",
"""
class A:
    def displayA(self):
        print("Class A")

class B:
    def displayB(self):
        print("Class B")

class C(A, B):
    def displayC(self):
        print("Class C inherits A and B")

obj = C()
obj.displayA()
obj.displayB()
obj.displayC()
""")

show_program(7, "Multilevel Inheritance",
"""
class Grandparent:
    def show_gp(self):
        print("Grandparent")

class Parent(Grandparent):
    def show_p(self):
        print("Parent")

class Child(Parent):
    def show_c(self):
        print("Child")

c = Child()
c.show_gp()
c.show_p()
c.show_c()
""")

show_program(8, "Method Overriding",
"""
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

obj = Dog()
obj.sound()
""")

show_program(9, "super() keyword example",
"""
class A:
    def show(self):
        print("Class A Method")

class B(A):
    def show(self):
        super().show()
        print("Class B Method")

b = B()
b.show()
""")

show_program(10, "Hierarchical Inheritance Example",
"""
class Vehicle:
    def type(self):
        print("This is a vehicle")

class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels")

class Bike(Vehicle):
    def wheels(self):
        print("Bike has 2 wheels")

c = Car()
b = Bike()
c.type(); c.wheels()
b.type(); b.wheels()
""")

# ========================= REGULAR EXPRESSIONS =========================

show_program(11, "Find all digits in a string using re",
"""
import re
text = "Python1234is56great"
result = re.findall(r"\\d+", text)
print(result)
""")

show_program(12, "Check if email is valid",
"""
import re
email = "test@gmail.com"
pattern = r'^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$'
if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")
""")

show_program(13, "Substitute words using re.sub()",
"""
import re
text = "I love Python"
new_text = re.sub("Python", "Streamlit", text)
print(new_text)
""")

show_program(14, "Split string using regex",
"""
import re
text = "apple,banana;cherry orange"
parts = re.split(r'[; ,]', text)
print(parts)
""")

show_program(15, "Find position of first digit in string",
"""
import re
s = "abc123xyz"
m = re.search(r'\\d', s)
if m:
    print("First digit position:", m.start())
""")

# ========================= EVENT DRIVEN PROGRAMMING =========================

show_program(16, "Simple event-driven counter",
"""
count = 0
def on_click():
    global count
    count += 1
    print("Button clicked", count, "times")

# simulate events
on_click()
on_click()
""")

show_program(17, "Keyboard event simulation",
"""
def key_press(key):
    print(f"Key '{key}' pressed!")

# simulate key presses
for k in ['A', 'B', 'C']:
    key_press(k)
""")

show_program(18, "Mouse event simulation",
"""
def mouse_click(x, y):
    print(f"Mouse clicked at ({x},{y})")

mouse_click(10, 20)
mouse_click(50, 100)
""")

# ========================= GUI PROGRAMMING (TKINTER) =========================

show_program(19, "Simple GUI Window using Tkinter",
"""
import tkinter as tk

root = tk.Tk()
root.title("Simple GUI")
label = tk.Label(root, text="Hello Sundram 👋", font=("Arial", 16))
label.pack()
root.mainloop()
""")

show_program(20, "Button click example in Tkinter",
"""
import tkinter as tk

def say_hello():
    print("Button Clicked! Hello Sundram 👋")

win = tk.Tk()
win.title("Button Demo")
btn = tk.Button(win, text="Click Me", command=say_hello)
btn.pack(pady=20)
win.mainloop()
""")
# --- Navigation Buttons (Previous, Home, Next) ---
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⬅️ Previous"):
        st.switch_page("pages/lab7_8.py")  # Previous page

with col2:
    if st.button("🏠 Home"):
        st.switch_page("py_programs.py")  # Go to Home

with col3:
    if st.button("➡️ Next"):
        st.success("🎉 You have reached the last page!")


# ---- Footer ----
st.markdown("---")
st.caption("💡 Created by Sundram Gupta | Advanced Python Practice 💻")
