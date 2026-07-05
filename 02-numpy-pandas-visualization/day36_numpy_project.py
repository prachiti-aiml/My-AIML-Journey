#Day 36:Numpy Project - Matrix Calculator

import numpy as np
def show_menu():
    print("\n     MATRIX CALCULATOR       ")
    print("1.Add matrices")
    print("2.Subtract matrices")
    print("3.Multiply matrices")
    print("4.Transpose a matrix")
    print("5.Determinant of a matrix")
    print("6.Inverse of a matrix")
    print("7.Matrix Statistics")
    print("8.Exit")

def get_matrix(name):
    rows = int(input("Enter rows for " + name + ":"))
    cols = int(input("Enter columns for " + name + ":"))
    print("Enter values row by row (space seperated):")
    data = []
    for i in range(rows):
        row = list(map(float,input("Row" + str(i+1) + ":").split()))
        data.append(row)
    return np.array(data)

def add_matrices():
    a = get_matrix("Matrix A")
    b = get_matrix("Matrix B")
    if a.shape == b.shape:
        print("\nResult:\n",a + b)
    else:
        print("Matrices must have same shape to add.")

def subtract_matrices():
    a = get_matrix("Matrix A")
    b = get_matrix("Matrix B")
    if a.shape == b.shape:
        print("\nresult:\n",a - b)
    else:
        print("Matrices must have same shape to subtract.")

def multiply_matrices():
    a = get_matrix("Matrix A")
    b = get_matrix("Matrix B")
    if a.shape[1] == b.shape[0]:
       print("\nResult:\n",np.dot(a,b))
    else:
        print("Columns of A must equal rows of B for multiplication.")

def tranpose_matrix():
    a = get_matrix("Matrix")
    print("\nOriginal:\n",a)
    print("Transposed:\n",a.T)

def determinant_matrix():
    a = get_matrix("Matrix")
    if a.shape[0] == a.shape[1]:
        print("\nDeterminant:",round(np.linalg.det(a),2))
    else:
        print("Matrix must be square for inverse.")

def matrix_statistics():
    a = get_matrix("Matrix")
    print("\nMatrix:\n",a)
    print("Sum:",np.sum(a))
    print("Mean:",np.mean(a)) 
    print("Max:",np.max(a))
    print("Min:",np.min(a))
    print("Std deviation:",round(np.std(a),2))

while True:
    show_menu()
    choice = input("Enter your choice (1-8):")

    if choice == "1":
        add_matrices()
    elif choice == "2":
        subtract_matrices()
    elif choice == "3":
        multiply_matrices()
    elif choice == "4":
        tranpose_matrix()
    elif choice == "5":
        determinant_matrix()
    elif choice == "6":
        inverse_matrix()
    elif choice == "7":
        matrix_statistics()
    elif choice == "8":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.Please enter 1-8.")   