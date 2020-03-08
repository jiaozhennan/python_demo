import os
import pickle


# 持久化
man = []
other = []

try:
    data = open('sketch.txt')

    for each_line in data:
        try:
            role, line_spoken = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass

    data.close()
except IOError as err:
    print('The data file is missing!' + str(err))

# print(man)
# print(other)

try:
    with open('man_data.txt', 'w') as man_file, open('other_date.txt', 'w') as other_file:
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)
except IOError:
    print('File error.')
except pickle.PickleError as perr:
    print('Picking error:' + str(perr))


"""
try:
    man_file = open('man_data.txt', 'w')
    other_file = open('other_date.txt', 'w')
    man_file.write(str(man))
    other_file.write(str(other))
    # print(other, file=other_file)
    # print(man, file=man_file)
except IOError:
    print('File error.')
finally:
    man_file.close()
    other_file.close()
"""



"""
# 异常处理
try:
    data = open('sketch.txt')

    for each_line in data:
        try:
            role, line_spoken = each_line.split(':', 1)
            print(role, end='')
            print(' said:', end='')
            print(line_spoken, end='')

        except ValueError:
            pass

    data.close()

except IOError:
    print('The data file is missing!')


"""




"""

# 异常处理
try:
    data = open('sketch.txt')

    for each_line in data:
        try:
            role, line_spoken = each_line.split(':', 1)
            print(role, end='')
            print(' said:', end='')
            print(line_spoken, end='')

        except:
            pass
        
    data.close()

except:
    print('The data file is missing!')

"""



"""

# 逻辑判断
import os

if os.path.exists('sketch.txt'):
    data = open('sketch.txt')

    for each_line in data:
        if not each_line.find(':') == -1:
            role, line_spoken = each_line.split(':', 1)
            print(role, end='')
            print(' said ', end='')
            print(line_spoken, end='')
    data.close()
else:
    print("The data file is missing!")

"""