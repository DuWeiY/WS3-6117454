# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def serial_sum(x,y=None):
    num=0
    if y is None:
        for i in range(x+1):
            num += i
        return num
    else:
        for i in range(x,y+1):
            num += i
        return num


print(serial_sum(4))
print(serial_sum(2,4))