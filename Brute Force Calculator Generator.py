##Aaron Tabor
##Automatic Calculator generates C++ source code for a "brute force" calculator
##The brute force calculator contains a conditional for every possible combination of positive numbers from 0 to numEnd-1 (inclusive)
##Error checking to ensure positive numbers is not implemented, but error checking on the operator's input is implemented

##Enter filename as a string with the .cpp extension. Ex. "calculator.cpp"
##numEnd is integer

def generate(fileName, numEnd):
    ifFlag = 1
    f = open(fileName, "w")
    f.write("#include <iostream>\n\nusing std::cout;\nusing std::cin;\nusing std::endl;\n\n")
    f.write("int main()\n{\n")

    f.write('\tint num1 = 0;\n\tint num2 = 0;\n\tchar op;\n\n\tcout << endl << "Enter Number 1: ";')
    f.write('\n\tcin >> num1;\n\tcout << endl << "Enter Number 2: ";')
    f.write('\n\tcin >> num2;\n\tcout << endl << "Enter Operator (+, -, /, *): ";')
    f.write("\n\tcin >> op;\n\t\n\twhile(op != '+' && op != '-' && op != '/' && op != '*')\n\t{\n\t\tcout << endl << \"\\tError: invalid operator\"")
    f.write(' << endl << "\\tEnter Operator (+, -, /, *): ";\n\t\tcin >> op;')
    f.write('\n\t}')

    for i in range(numEnd):
        for j in range(numEnd):
            if ifFlag == 1:
                f.write("\n\n\tif(num1 == {n1} && num2 == {n2} && op == '+')\n\t\tcout << endl << endl << \"{n1} + {n2} = \" << {n1} + {n2};".format(n1 = i, n2 = j))
                ifFlag = 0
            else:
                f.write("\n\telse if(num1 == {n1} && num2 == {n2} && op == '+')\n\t\tcout << endl << endl << \"{n1} + {n2} = \" << {n1} + {n2};".format(n1 = i, n2 = j))
            f.write("\n\telse if(num1 == {n1} && num2 == {n2} && op == '-')\n\t\tcout << endl << endl << \"{n1} - {n2} = \" << {n1} - {n2};".format(n1 = i, n2 = j))
            f.write("\n\telse if(num1 == {n1} && num2 == {n2} && op == '*')\n\t\tcout << endl << endl << \"{n1} * {n2} = \" << {n1} * {n2};".format(n1 = i, n2 = j))
            if j == 0:
                f.write("\n\telse if(num1 == {n1} && num2 == {n2} && op == '+')\n\t\tcout << endl << endl << \"{n1} / {n2} = Error! Cannot divide by zero!\";".format(n1 = i, n2 = j))
            else:
                f.write("\n\telse if(num1 == {n1} && num2 == {n2} && op == '/')\n\t\tcout << endl << endl << \"{n1} / {n2} = \" << {n1} / {n2};".format(n1 = i, n2 = j))

    f.write('\n\telse\n\tcout << endl << endl << "Error! Numbers not in defined range [0, {end}]...";'.format(end = numEnd - 1))

    f.write("\n\n\treturn 0;\n}")
    f.close()
