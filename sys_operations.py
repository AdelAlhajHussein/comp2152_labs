import os
import sys
import platform
import socket

#lab 9 - Question 3.a.a, 3.a.b
# Machine type and processor type
print(platform.machine())
print(platform.architecture())

# Lab 9 - Question 3.a.c., 3.a.d.
# Set and Get socket timeout
print(socket.getdefaulttimeout())
socket.setdefaulttimeout(50)
print(socket.getdefaulttimeout())

# Lab 9 - Question 3.a.e.
# OS name
print(os.name)
print(platform.system())

#Lab 9 - Question 3.a.f.
#Process ID
print(os.getpid())

# Lab 9 - Question 3.b.a.
# File Description
# Open (or create) a file named fdpractice.txt
f_name = "fdpractise.txt"
# with open("fdpractise.txt", "a+") as f:
#    print(f.readline())
#    f.write("Hello, world")

# f1 = open(f_name, "r")
# print(f1)
# f1.close()

f = os.open(f_name, os.O_RDWR | os.O_CREAT)
print(f)

f_obj = os.fdopen(f, "a+")
print(f_obj)

print()

# Lab 9 - Question 3.b.e
# Forking
print("Before Fork:", os.getpid())
p = os.fork()
print("After Fork:", os.getpid())

if p == 0:
    print("Child Process")
    print("Parent Process PID:", os.getpid())
else:
    print("Parent Process")
    os.wait()
    print("Child Process PID:", p)


print("Last line")