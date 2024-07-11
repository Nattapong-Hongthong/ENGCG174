# ฟังก์ชัน Recursive เพื่อพิมพ์ดาวจากน้อยไปมาก
def print_stars_increasing(n):
    if n > 0:
        print_stars_increasing(n - 1)  
        print('*' * n)

# ฟังก์ชัน Recursive ดาวจากมากไปน้อย
def print_stars_decreasing(n):
    if n > 0:
        print('*' * n)
        print_stars_decreasing(n - 1)  

# ฟังก์ชัน Recursive ดาวตรงกลาง
def print_centered_pattern_recursive(n, current=1):
    if current <= n:
        print(' ' * (n - current) + '* ' * current)
        print_centered_pattern_recursive(n, current + 1)  

# ฟังก์ชัน Recursive ดาวตรงกลางกลับด้าน
def print_reversed_centered_pattern_recursive(n, current=None):
    if current is None:
        current = n
    if current > 0:
        print(' ' * (n - current) + '* ' * current)
        print_reversed_centered_pattern_recursive(n, current - 1)  

# ฟังก์ชัน Recursive ดาวจากน้อยไปมาก 
def print_stars_increasing_no_space(n, current=1):
    if current <= n:
        print(' ' * (n - current) + '*' * current)
        print_stars_increasing_no_space(n, current + 1)  

# รับค่าจากผู้ใช้
rows = int(input("ป้อนจำนวนเต็ม: "))
# print ออกมา
print_stars_increasing(rows)
print("---------------------------------------")
print_stars_decreasing(rows)
print("---------------------------------------")
print_centered_pattern_recursive(rows)
print("---------------------------------------")
print_reversed_centered_pattern_recursive(rows)
print("---------------------------------------")
print_stars_increasing_no_space(rows)