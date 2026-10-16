import math

def main():
    while True:
        print("\n\n\n\n")
        print("--------------------WELCOME--TO--BCALC:V_1--------------------")
        print("\n\nThis is a calculator app in which you can calculate-----\n")

        print(r"A\---------ARITHMETIC & BASICS---------")
        print("1. Percentage Calculation")
        print("2. Percentage of a Number")
        print("3. Average")
        print("4. Time")
        print("5. Speed")
        print("6. Distance")
        print("7. Ratio")

        print(r"B\---------FINANCIAL CALCULATIONS---------")
        print("8. Profit")
        print("9. Loss")
        print("10. Profit Percentage")
        print("11. Loss Percentage")
        print("12. Simple Interest")
        print("13. Compound Interest")

        print(r"C\---------RECTANGLE---------")
        print("14. Area of a Rectangle")
        print("15. Perimeter of a Rectangle")
        print("16. Diagonal of a Rectangle")
        print("17. Aspect Ratio of a Rectangle")
        print("18. Circumradius of a Rectangle")
        print("19. Center Coordinates of a Rectangle")
        print("20. Length from Area and Breadth")
        print("21. Breadth from Area and Length")
        print("22. Length from Perimeter and Breadth")
        print("23. Breadth from Perimeter and Length")
        print("24. Length from Diagonal and Breadth")
        print("25. Breadth from Diagonal and Length")

        print(r"D\---------SQUARE---------")
        print("26. Area of a Square")
        print("27. Perimeter of a Square")
        print("28. Diagonal of a Square")
        print("29. Inradius of a Square")
        print("30. Circumradius of a Square")
        print("31. Side from Area of a Square")
        print("32. Side from Perimeter of a Square")
        print("33. Side from Diagonal of a Square")

        print(r"E\---------CIRCLE---------")
        print("34. Radius of a Circle")
        print("35. Diameter of a Circle")
        print("36. Area of a Circle")
        print("37. Circumference of a Circle")
        print("38. Radius from Area of a Circle")
        print("39. Radius from Circumference of a Circle")
        print("40. Area of a Sector")
        print("41. Perimeter of a Sector")
        print("42. Arc Length of a Circle")
        print("43. Chord Length of a Circle")
        print("44. Distance from Center to Chord")
        print("45. Area of a Segment of a Circle")
        print("46. Area of an Annulus")

        print(r"F\---------TRIANGLE---------")
        print("47. Perimeter of a Triangle")
        print("48. Area of a Triangle (Base & Height)")
        print("49. Area of a Triangle (Heron's Formula)")
        print("50. Area of a Triangle (Two Sides & Included Angle - SAS)")
        print("51. Area of a Triangle Using Coordinates (Shoelace Formula)")
        print("52. Hypotenuse of a Right Triangle")
        print("53. Base or Perpendicular of a Right Triangle")
        print("54. Inradius of a Right Triangle")
        print("55. Area of an Equilateral Triangle")
        print("56. Perimeter of an Equilateral Triangle")
        print("57. Height of an Equilateral Triangle")
        print("58. Inradius of an Equilateral Triangle")
        print("59. Circumradius of an Equilateral Triangle")
        print("60. Area of an Isosceles Triangle")
        print("61. Perimeter of an Isosceles Triangle")
        print("62. Inradius of a Triangle (General)")
        print("63. Circumradius of a Triangle (General)")
        print("64. Altitude from Area and Side")
        print("65. Length of Median of a Triangle")
        print("66. Third Angle of a Triangle (Given Two Angles)")

        print(r"G\---------UNIT CONVERSION---------")
        print("67. Centimetres to Metres")
        print("68. Metres to Kilometres")
        print("69. Grams to Kilograms")
        print("70. Kilograms to Grams")
        print("71. Celsius to Fahrenheit")
        print("72. Fahrenheit to Celsius")
        print("0. Exit")

        choice = input("\nEnter your choice (0-72): ")

        if choice == '0':
            print("\nExiting BCALC:V_1. Goodbye!\n")
            break

       
        elif choice == '1':
            part = float(input("Enter part value: "))
            total = float(input("Enter total value: "))
            print(f"Percentage: {(part / total) * 100}%")

        elif choice == '2':
            num = float(input("Enter number: "))
            per = float(input("Enter percentage: "))
            print(f"Result: {(num * per) / 100}")

        elif choice == '3':
            nums = list(map(float, input("Enter numbers separated by space: ").split()))
            print(f"Average: {sum(nums) / len(nums)}")

        elif choice == '4':
            d = float(input("Enter distance: "))
            s = float(input("Enter speed: "))
            print(f"Time: {d / s}")

        elif choice == '5':
            d = float(input("Enter distance: "))
            t = float(input("Enter time: "))
            print(f"Speed: {d / t}")

        elif choice == '6':
            s = float(input("Enter speed: "))
            t = float(input("Enter time: "))
            print(f"Distance: {s * t}")

        elif choice == '7':
            a = float(input("Enter first number (a): "))
            b = float(input("Enter second number (b): "))
            gcd = math.gcd(int(a), int(b))
            print(f"Ratio: {a/gcd} : {b/gcd}")

  
        elif choice == '8':
            sp = float(input("Enter Selling Price: "))
            cp = float(input("Enter Cost Price: "))
            print(f"Profit: {sp - cp}")

        elif choice == '9':
            cp = float(input("Enter Cost Price: "))
            sp = float(input("Enter Selling Price: "))
            print(f"Loss: {cp - sp}")

        elif choice == '10':
            profit = float(input("Enter Profit amount: "))
            cp = float(input("Enter Cost Price: "))
            print(f"Profit Percentage: {(profit / cp) * 100}%")

        elif choice == '11':
            loss = float(input("Enter Loss amount: "))
            cp = float(input("Enter Cost Price: "))
            print(f"Loss Percentage: {(loss / cp) * 100}%")

        elif choice == '12':
            p = float(input("Enter Principal amount: "))
            r = float(input("Enter Annual Interest Rate (%): "))
            t = float(input("Enter Time (years): "))
            print(f"Simple Interest: {(p * r * t) / 100}")

        elif choice == '13':
            p = float(input("Enter Principal amount: "))
            r = float(input("Enter Annual Interest Rate (%): "))
            t = float(input("Enter Time (years): "))
            n = float(input("Enter number of times interest applied per time period: "))
            print(f"Compound Interest: {p * (1 + (r / (100 * n)))**(n * t) - p}")

       
        elif choice == '14':
            l = float(input("Enter Length: "))
            b = float(input("Enter Breadth: "))
            print(f"Area of Rectangle: {l * b}")

        elif choice == '15':
            l = float(input("Enter Length: "))
            b = float(input("Enter Breadth: "))
            print(f"Perimeter of Rectangle: {2 * (l + b)}")

        elif choice == '16':
            l = float(input("Enter Length: "))
            b = float(input("Enter Breadth: "))
            print(f"Diagonal of Rectangle: {math.sqrt(l**2 + b**2)}")

        elif choice == '17':
            l = float(input("Enter Length: "))
            b = float(input("Enter Breadth: "))
            gcd = math.gcd(int(l), int(b))
            print(f"Aspect Ratio: {int(l/gcd)}:{int(b/gcd)}")

        elif choice == '18':
            l = float(input("Enter Length: "))
            b = float(input("Enter Breadth: "))
            print(f"Circumradius of Rectangle: {math.sqrt(l**2 + b**2) / 2}")

        elif choice == '19':
            x1 = float(input("Enter X1 coordinate: "))
            y1 = float(input("Enter Y1 coordinate: "))
            x2 = float(input("Enter X2 coordinate: "))
            y2 = float(input("Enter Y2 coordinate: "))
            print(f"Center Coordinates: {((x1+x2)/2, (y1+y2)/2)}")

        elif choice == '20':
            area = float(input("Enter Area: "))
            b = float(input("Enter Breadth: "))
            print(f"Length: {area / b}")

        elif choice == '21':
            area = float(input("Enter Area: "))
            l = float(input("Enter Length: "))
            print(f"Breadth: {area / l}")

        elif choice == '22':
            peri = float(input("Enter Perimeter: "))
            b = float(input("Enter Breadth: "))
            print(f"Length: {(peri / 2) - b}")

        elif choice == '23':
            peri = float(input("Enter Perimeter: "))
            l = float(input("Enter Length: "))
            print(f"Breadth: {(peri / 2) - l}")

        elif choice == '24':
            diag = float(input("Enter Diagonal: "))
            b = float(input("Enter Breadth: "))
            print(f"Length: {math.sqrt(diag**2 - b**2)}")

        elif choice == '25':
            diag = float(input("Enter Diagonal: "))
            l = float(input("Enter Length: "))
            print(f"Breadth: {math.sqrt(diag**2 - l**2)}")

       
        elif choice == '26':
            s = float(input("Enter Side: "))
            print(f"Area of Square: {s**2}")

        elif choice == '27':
            s = float(input("Enter Side: "))
            print(f"Perimeter of Square: {4 * s}")

        elif choice == '28':
            s = float(input("Enter Side: "))
            print(f"Diagonal of Square: {s * math.sqrt(2)}")

        elif choice == '29':
            s = float(input("Enter Side: "))
            print(f"Inradius of Square: {s / 2}")

        elif choice == '30':
            s = float(input("Enter Side: "))
            print(f"Circumradius of Square: {(s * math.sqrt(2)) / 2}")

        elif choice == '31':
            area = float(input("Enter Area: "))
            print(f"Side from Area: {math.sqrt(area)}")

        elif choice == '32':
            peri = float(input("Enter Perimeter: "))
            print(f"Side from Perimeter: {peri / 4}")

        elif choice == '33':
            diag = float(input("Enter Diagonal: "))
            print(f"Side from Diagonal: {diag / math.sqrt(2)}")

        # --- CIRCLE (34-46) ---
        elif choice == '34':
            d = float(input("Enter Diameter: "))
            print(f"Radius: {d / 2}")

        elif choice == '35':
            r = float(input("Enter Radius: "))
            print(f"Diameter: {2 * r}")

        elif choice == '36':
            r = float(input("Enter Radius: "))
            print(f"Area of Circle: {math.pi * (r**2)}")

        elif choice == '37':
            r = float(input("Enter Radius: "))
            print(f"Circumference: {2 * math.pi * r}")

        elif choice == '38':
            area = float(input("Enter Area: "))
            print(f"Radius from Area: {math.sqrt(area / math.pi)}")

        elif choice == '39':
            circ = float(input("Enter Circumference: "))
            print(f"Radius from Circumference: {circ / (2 * math.pi)}")

        elif choice == '40':
            r = float(input("Enter Radius: "))
            theta = float(input("Enter Angle in degrees: "))
            print(f"Area of Sector: {(theta / 360) * math.pi * (r**2)}")

        elif choice == '41':
            r = float(input("Enter Radius: "))
            theta = float(input("Enter Angle in degrees: "))
            arc = (theta / 360) * 2 * math.pi * r
            print(f"Perimeter of Sector: {arc + (2 * r)}")

        elif choice == '42':
            r = float(input("Enter Radius: "))
            theta = float(input("Enter Angle in degrees: "))
            print(f"Arc Length: {(theta / 360) * 2 * math.pi * r}")

        elif choice == '43':
            r = float(input("Enter Radius: "))
            theta = float(input("Enter Angle in degrees (theta): "))
            print(f"Chord Length: {2 * r * math.sin(math.radians(theta / 2))}")

        elif choice == '44':
            r = float(input("Enter Radius: "))
            chord = float(input("Enter Chord length: "))
            print(f"Distance to Chord: {math.sqrt(r**2 - (chord / 2)**2)}")

        elif choice == '45':
            r = float(input("Enter Radius: "))
            theta = float(input("Enter Angle in degrees: "))
            sector_area = (theta / 360) * math.pi * (r**2)
            triangle_area = 0.5 * (r**2) * math.sin(math.radians(theta))
            print(f"Area of Segment: {sector_area - triangle_area}")

        elif choice == '46':
            R = float(input("Enter Outer Radius (R): "))
            r = float(input("Enter Inner Radius (r): "))
            print(f"Area of Annulus: {math.pi * (R**2 - r**2)}")

       
        elif choice == '47':
            a = float(input("Enter Side a: "))
            b = float(input("Enter Side b: "))
            c = float(input("Enter Side c: "))
            print(f"Perimeter of Triangle: {a + b + c}")

        elif choice == '48':
            base = float(input("Enter Base: "))
            height = float(input("Enter Height: "))
            print(f"Area of Triangle: {0.5 * base * height}")

        elif choice == '49':
            a = float(input("Enter Side a: "))
            b = float(input("Enter Side b: "))
            c = float(input("Enter Side c: "))
            s = (a + b + c) / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            print(f"Area (Heron's Formula): {area}")

        elif choice == '50':
            a = float(input("Enter Side a: "))
            b = float(input("Enter Side b: "))
            angle_c = float(input("Enter Included Angle C (in degrees): "))
            area = 0.5 * a * b * math.sin(math.radians(angle_c))
            print(f"Area (SAS): {area}")

        elif choice == '51':
            x1 = float(input("Enter X1: "))
            y1 = float(input("Enter Y1: "))
            x2 = float(input("Enter X2: "))
            y2 = float(input("Enter Y2: "))
            x3 = float(input("Enter X3: "))
            y3 = float(input("Enter Y3: "))
            area = 0.5 * abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
            print(f"Area (Shoelace Formula): {area}")

        elif choice == '52':
            p = float(input("Enter Perpendicular: "))
            b = float(input("Enter Base: "))
            print(f"Hypotenuse: {math.sqrt(p**2 + b**2)}")

        elif choice == '53':
            hyp = float(input("Enter Hypotenuse: "))
            other = float(input("Enter other side (Base/Perpendicular): "))
            print(f"Missing side: {math.sqrt(hyp**2 - other**2)}")

        elif choice == '54':
            p = float(input("Enter Perpendicular: "))
            b = float(input("Enter Base: "))
            hyp = math.sqrt(p**2 + b**2)
            print(f"Inradius of Right Triangle: {(p + b - hyp) / 2}")

        elif choice == '55':
            a = float(input("Enter Side of Equilateral Triangle: "))
            print(f"Area: {(math.sqrt(3) / 4) * (a**2)}")

        elif choice == '56':
            a = float(input("Enter Side of Equilateral Triangle: "))
            print(f"Perimeter: {3 * a}")

        elif choice == '57':
            a = float(input("Enter Side of Equilateral Triangle: "))
            print(f"Height: {(math.sqrt(3) / 2) * a}")

        elif choice == '58':
            a = float(input("Enter Side of Equilateral Triangle: "))
            print(f"Inradius: {a / (2 * math.sqrt(3))}")

        elif choice == '59':
            a = float(input("Enter Side of Equilateral Triangle: "))
            print(f"Circumradius: {a / math.sqrt(3)}")

        elif choice == '60':
            a = float(input("Enter equal side (a): "))
            b = float(input("Enter base (b): "))
            height = math.sqrt(a**2 - (b**2 / 4))
            print(f"Area of Isosceles Triangle: {0.5 * b * height}")

        elif choice == '61':
            a = float(input("Enter equal side (a): "))
            b = float(input("Enter base (b): "))
            print(f"Perimeter of Isosceles Triangle: {(2 * a) + b}")

        elif choice == '62':
            area = float(input("Enter Area: "))
            s = float(input("Enter Semi-perimeter: "))
            print(f"Inradius: {area / s}")

        elif choice == '63':
            a = float(input("Enter Side a: "))
            b = float(input("Enter Side b: "))
            c = float(input("Enter Side c: "))
            area = float(input("Enter Area: "))
            print(f"Circumradius: {(a * b * c) / (4 * area)}")

        elif choice == '64':
            area = float(input("Enter Area: "))
            base = float(input("Enter Base: "))
            print(f"Altitude: {(2 * area) / base}")

        elif choice == '65':
            a = float(input("Enter Side a: "))
            b = float(input("Enter Side b: "))
            c = float(input("Enter Side c: "))
            median = 0.5 * math.sqrt(2 * b**2 + 2 * c**2 - a**2)
            print(f"Length of Median (to side a): {median}")

        elif choice == '66':
            angle1 = float(input("Enter first angle: "))
            angle2 = float(input("Enter second angle: "))
            print(f"Third Angle: {180 - (angle1 + angle2)}")

       
        elif choice == '67':
            cm = float(input("Enter length in Centimetres: "))
            print(f"Metres: {cm / 100}")

        elif choice == '68':
            m = float(input("Enter length in Metres: "))
            print(f"Kilometres: {m / 1000}")

        elif choice == '69':
            g = float(input("Enter weight in Grams: "))
            print(f"Kilograms: {g / 1000}")

        elif choice == '70':
            kg = float(input("Enter weight in Kilograms: "))
            print(f"Grams: {kg * 1000}")

        elif choice == '71':
            c = float(input("Enter temperature in Celsius: "))
            print(f"Fahrenheit: {(c * 9/5) + 32}")

        elif choice == '72':
            f = float(input("Enter temperature in Fahrenheit: "))
            print(f"Celsius: {(f - 32) * 5/9}")

        else:
            print("Invalid choice! Please try again.")
            continue

        
        while True:
            action = input("\nPress 0 to exit or R (or r) to restart: ").strip()
            if action == '0':
                print("\nExiting BCALC:V_1. Goodbye!\n")
                return
            elif action.lower() == 'r':
                break
            else:
                print("Invalid input! Please press 0 to exit or R to restart.")

if __name__ == "__main__":
    main()
