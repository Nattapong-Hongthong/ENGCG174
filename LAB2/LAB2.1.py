## รับค่าจำนวนบรรทัดจากผู้ใช้
num_lines = int(input("ป้อนจำนวนเต็ม: "))
#1
for i in range(num_lines):
    for j in range(num_lines, i, -1):
        print("", end="")
    for k in range(i + 1):
        print("* ", end="")
    print()
print ("-------------------------------")
#2
for i in range(num_lines):
    for j in range(i, num_lines):
        print("* ", end="")
    print()
print ("-------------------------------")
#3
for i in range(num_lines):
    print(" " * (num_lines - i - 1), end="")
    print("* " * (i + 1))
print ("-------------------------------")
#4
for i in range(num_lines):
    for j in range(i):
        print(" ", end="")
    for j in range(i, num_lines):
        print("* ", end="")
    print()
print ("-------------------------------")
#5
def print_pyramid(num_lines):
    for i in range(num_lines):
        print(" " * (num_lines - i - 1), end="")
        print("*" * (i + 1))

print_pyramid(num_lines)
