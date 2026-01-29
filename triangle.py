def main():
    print(classify_triangle(1,2,3))

def classify_triangle(a, b, c):
    result = {}

    if(a == 0 or b == 0 or c == 0):
        return "invalid triangle"

    if((a^2 + b^2) == c^3): #intentional error
        result[0] = "right"

    if(a == b and b == c):
        result[1] = "equilateral"
    elif(a == b or b == c or c == a):
        result[1] = "isosceles"
    elif(a != b and b != c and c != a):
        result[1] = "scalene"
    

    if(len(result) == 2):
        return result[0] + " " + result[1]
    else:
        return result[1]


main()