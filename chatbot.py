import time # python chatbot.py
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
import sys
import shutil
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 125)  
from gtts import gTTS
from playsound import playsound
import os
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from rich.console import Console
console = Console()
from colorama import Fore, Back, Style, init
init(autoreset=True)
from sympy import symbols, integrate, sympify, E  
from sympy import symbols, diff, sympify, E
from sympy.abc import x
def custom_bot_print(msg):
    console.print(msg, style="bold cyan on black ")
def print(msg):
    console.print(msg, style="bold cyan on black ")
width = shutil.get_terminal_size().columns
msg = " "
def speak(text,lang="en"):
    tts= gTTS(text=text, lang=lang, slow=True)
    tts.save("voice.mp3")
    playsound("voice.mp3")
    os.remove("voice.mp3")
    
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 140)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
first_time= True
while True:
    user_input = input(Fore.MAGENTA+"You: ").lower()
    print("``",style="  on cyan on black black \n")
    if first_time:
        console.print("[bold cyan on black ] MATH AI [/]", justify="center")
        console.print("[bold black on black] CREATED BY BADRI[/]", justify="center")
        console.print("[bold cyan on black ] WELCOME BUDDY • HOW CAN I HELP YOU IN MATH  🤖[/]\n", justify="center")
        first_time = False
    
    if ("exit" in user_input or "quit" in user_input or "bye" in user_input or "stop" in user_input):
        speak("Thank you for using Math AI buddy! see you later!") 
        console.print("Thank you for using Math AI buddy! see you later!", style="cyan on black ")
        break 
    elif("hello" in user_input or "hi" in user_input or "hey" in user_input):
        speak("Hello buddy! How can I assist you today?") 
        console.print("Hello buddy! How can I assist you today?", style="  on cyan on black black\n")
        print()
        print()
        
    elif("who are you" in user_input or "what are you" in user_input or "tell me about yourself" in user_input or "introduce yourself" in user_input):
        console.print("Iam  MATH AI  , I can help you with math problems, calculations, and more... How can I assist you today? ") 
        speak("Iam  MATH AI  , I can help you with math problems, calculations, and more... How can I assist you today?")
        print()
        print()
   
    elif("bodmas" in user_input or "bodmas value" in user_input or "calculate bodmas" in user_input or "find bodmas value" in user_input or "calculate bodmas value" in user_input):
        speak("Let's calculate BODMAS expression!")
        expression = input("Enter your BODMAS expression: ")
        result = eval(expression)
        print("Result:", result, style="bold cyan on black black")
        print()
        print()
    
    elif("simple interest" in user_input or "calculate simple interest" in user_input or "find simple interest" in user_input or "find the simple interest " in user_input):
        speak("Let's calculate Simple Interest! ")
        console.print("Principal defines: The initial amount of money that is deposited or loaned.",style="bold black on black")
        console.print("Rate defines: The percentage of interest charged or earned per year.",style="bold black on black")
        console.print("Time defines: The duration for which the money is borrowed or invested, in years.",style="bold black on black")
        principal = float(input("Enter the principal amount (P): "))
        rate = float(input("Enter the rate of interest (R) in percentage: "))
        time = float(input("Enter the time period (T) in years: "))
        simple_interest = (principal * rate * time) / 100
        total=principal + simple_interest
        console.print(f"\n[bold green]Simple Interest for P={principal}, R={rate}%, T={time} THE TOTAL AMOUNT OF SIMPLE INTEREST IS: {total}[/bold green]")    
        
        print("")
    elif("compound interest" in user_input or "calculate compound interest" in user_input or "find compound interest" in user_input or "find the compound interest" in user_input):
        speak("Let's calculate Compound Interest! ")
        console.print("Principal defines: The initial amount of money that is deposited or loaned.",style="bold black on black")
        time.sleep(1)
        console.print("Rate defines: The percentage of interest charged or earned per year.",style="bold black on black")
        time.sleep(1)
        console.print("Time defines: The duration for which the money is borrowed or invested, in years.",style="bold black on black")
        time.sleep(1)
        principal = float(input("Enter the principal amount (P): "))
        rate = float(input("Enter the rate of interest (R) in percentage: "))
        time = float(input("Enter the time period (T) in years: "))
        compound_interest = principal * ((1 + (rate / 100)) ** time - 1)
        total = principal + compound_interest
        console.print(f"\n[bold green]Compound Interest for P={principal}, R={rate}%, T={time} THE TOTAL AMOUNT OF COMPOUND INTEREST IS: {total}[/bold green]")
        
        print("")
    elif (
            "differentiate" in user_input or
            "differentiation" in user_input or
            "find derivative" in user_input or
            "derivative" in user_input):

        from sympy import symbols, diff, sympify
        from sympy.abc import x
        speak("Let's calculate the derivative! ")
        expr_input = input("Enter the expression to differentiate w.r.t x: ")

        try:
            expr = sympify(expr_input, locals={"e": E})
            result = diff(expr, x)
            console.print(f"\n[bold cyan on black ]Derivative of {expr_input} w.r.t x is:[/bold cyan on black ]")
            console.print(result, style="bold yellow on black")
        except Exception as e:
            console.print(f"[bold red on black]Invalid expression! Error: {e}[/bold red on black]")
            continue
        else:
            result = integrate(expr, x)
            console.print(f"\n[bold cyan on black]Indefinite integral of {expr_input} w.r.t x is:[/bold cyan on black]")
            console.print(result, style="cyan on black on  black")
            
            print("-")
    elif("even numbers range"in user_input or\
    "display even number range" in user_input or\
    "find even number range" in user_input or\
    "find even numbers in given range" in user_input or\
    "display even number in given range" in user_input):
        speak("Let's find the even numbers in a given range! ")
        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))
        even_numbers = [num for num in range(start, end + 1)if num % 2 == 0]
        console.print("The even number range are : ",style="bold green on black") 
        console.print(f"\n[ green]Even numbers from {start} to {end}:[/green]")
        console.print(even_numbers,style=" green on black")
    elif("trigonometric formula" in user_input or "trigonometric equation" in user_input or "trigonometry" in user_input or "trig" in user_input
            or "sin" in user_input or "cos" in user_input or "tan" in user_input or "cot" in user_input or "sec" in user_input or "cosec" in user_input):
        speak("Let's calculate trigonomentric values! ")
        console.print("\n Let's calculate trigonometric values! style=")
        console.print("\n")
        angle = float(input("Enter the angle in degrees: "))
        print("")
        radians = math.radians(angle)
        print("\n")
        sin_value = math.sin(radians)
        print("")
        cos_value = math.cos(radians)
        print("")
        tan_value = math.tan(radians)
        print("")
        cot_value = 1 / tan_value if tan_value != 0 else float('inf')
        sec_value = 1 / cos_value if cos_value != 0 else float('inf')
        cosec_value = 1 / sin_value if sin_value != 0 else float('inf')
        console.print(f"\n[bold cyan on black ]]Trigonometric values for {angle} degrees:[/bold cyan on black ]")
        console.print(f"sin({angle}) = {sin_value:.4f}", style=" bold cyan on black ")
        console.print(f"cos({angle}) = {cos_value:.4f}", style=" bold cyan on black ")
        console.print(f"tan({angle}) = {tan_value:.4f}", style=" bold cyan on black ")
        time.sleep(1)
        console.print(f"cot({angle}) = {cot_value:.4f}", style=" bold cyan on black ")
        console.print(f"sec({angle}) = {sec_value:.4f}", style="bold cyan on black ")
        time.sleep(1)
        console.print(f"cosec({angle}) = {cosec_value:.4f}", style="bold cyan on black ")   
        time.sleep(1)
        speak("Trigonometry is a branch of mathematics that deals with the relationship between the angles and sides of a triangle  especially ")
        speak("right-angled triangles It helps us find unknown lengths then angles using formulas then functions like sine sin cosine cos then tangent tan" )            
        console.print("EXAMPLE:", style="bold cyan on black ")
        time.sleep(2)
        console.print("In a right triangle:", style=" cyan on black ")
        console.print("👉 sin(θ) = opposite / hypotenuse",style=" bold cyan on black ")
        time.sleep(1)
        console.print("👉 cos(θ) = adjacent / hypotenuse", style="bold cyan on black ")
        time.sleep(1)
        console.print("👉 tan(θ) = opposite / adjacent", style=" bold cyan on black ")        
        time.sleep(1)     
        console.print("\nTrigonometry is the [bold]mathematical study of angles and sides[/bold] in triangles.", style="bold cyan on black ")
        console.print("\nIt's mainly used in [bold yellow]right-angled triangles[/bold yellow] to understand how sides relate with angles.", style="bold cyan on black ")
        time.sleep(1)
        console.print("\n[bold cyan on black ]✏ Core Trigonometric Ratios:[/bold cyan on black ]")
        time.sleep(1)
        console.print("\n[bold cyan on black ]📐 Real-World Applications:[/bold cyan on black ]")
        console.print("- Finding building heights from shadows 🌇", style="bold cyan on black ")
        console.print("- Calculating angles in architecture 🏗", style="bold cyan on black ")
        console.print("- 3D modeling, animations & satellites 🚀", style="bold cyan on black ")
        time.sleep(1)
        console.print("\nTrigonometry is not just theory... it's math with direction & purpose! 🧭", style="bold cyan on black ")
        console.print("Whether you're an engineer, gamer, or astronaut — Trig is everywhere! 💫\n", style="bold cyan on black ")
        console.print("These functions are used in various fields like physics engineering and computer graphics to solve problems involving angles and distances",style="green on black")               
        console.print("\n[bold cyan on black ]Trigonometry Online Practice & Learning:[/bold cyan on black ]")
        time.sleep(1)
        console.print("[bold cyan on black ] NCERT Explanation:[/ bold cyan on black ] https://ncert.nic.in/textbook.php?jemh1=2-6")
        time.sleep(1)
        console.print("[bold cyan on black ] Khan Academy Lessons:[/bold cyan on black ] https://www.khanacademy.org/math/trigonometry")
        time.sleep(1)
        console.print("[bold cyan on black ] Trigonometric Ratios Practice:[/bold cyan on black ] https://www.cuemath.com/trigonometry/")
        time.sleep(1)
        console.print("[bold cyan on black ] Interactive Triangle Solver:[/bold cyan on black ] https://www.mathsisfun.com/algebra/trig-solving-triangles.html")
        
    elif("linear equation" in user_input or "linear equations" in user_input or "solve linear equation" in user_input):
        speak("Let's solve a linear equation! ")
        console.print("\n[bold cyan on black ]Linear Equation Solver[/bold cyan on black ]")
        console.print("A linear equation is an equation of the form ax + b = 0, where a and b are constants and x is the variable.",style="bold cyan on black ")
        console.print("To solve a linear equation, we isolate the variable x by performing operations on both sides of the equation.",style="bold cyan on black ")
        try:
            a = float(input("Enter the coefficient of x (a): "))
            b = float(input("Enter the constant term (b): "))
            if a == 0:
                raise ValueError("Coefficient 'a' cannot be zero in a linear equation.")
            x = -b / a
            
            console.print(f"\n[bold cyan on black ]The solution to the linear equation is: x = {x}[/bold cyan on black ]")
        except ValueError as e:
            console.print(f"[bold red on black ]Invalid input! Error: {e}[/bold red on black ]")
    elif("quadratic equation" in user_input or "solve quadratic equation" in user_input):
        speak("Let's solve a quadratic equation! ")
        console.print("\n[bold cyan on black ]Quadratic Equation Solver[/bold cyan on black ]")
        console.print("A quadratic equation is of the form ax² + bx + c = 0, where a, b, and c are constants.")
        console.print("The solutions can be found using the quadratic formula: x = (-b ± √(b² - 4ac)) / (2a)")
        try:
            a = float(input("Enter the coefficient of x² (a): "))
            b = float(input("Enter the coefficient of x (b): "))
            c = float(input("Enter the constant term (c): "))
            if a == 0:
                raise ValueError("Coefficient 'a' cannot be zero in a quadratic equation.")
            discriminant = b**2 - 4*a*c
            if discriminant < 0:
                console.print("[bold red on black ]No real solutions exist for this quadratic equation.[/bold red on black ]")
            else:
                root1 = (-b + math.sqrt(discriminant)) / (2*a)
                root2 = (-b - math.sqrt(discriminant)) / (2*a)
                console.print(f"\n[bold cyan on black ]The solutions to the quadratic equation {a}x² + {b}x + {c} = 0 are: x₁ = {root1}, x₂ = {root2}[/bold cyan on black ]")
        except ValueError as e:
            console.print(f"[bold red on black ]Invalid input! Error: {e}[/bold red on black ]")
    elif("ratio" in user_input or "calculate ratio" in user_input or "find ratio" in user_input or "find the ratio" in user_input):
        speak("Let's calculate the ratio! ")
        console.print("\n[bold cyan on black ]Ratio Calculator[/bold cyan on black ]")
        print("A ratio is a relationship between two numbers indicating how many times the first number contains the second.")
        try:
            a = float(input("Hey buddy!, Give the first number (a): "))
            b = float(input("Hey buddy!, Give the second number (b): "))
            if b == 0:
                raise ValueError("The second number cannot be zero in a ratio.")
            ratio = a / b
            console.print(f"\n[bold cyan on black ]The ratio of {a} to {b} is: {ratio:.4f}[/bold cyan on black ]")
        except ValueError as e:
            console.print(f"[bold red on black ]Invalid input! Error: {e}[/bold red on black ]")
            
        
    elif("probability" in user_input or  "find the probability" in user_input ):
        speak("Let's calculate probability! ")
        console.print("\n[bold cyan on black ]Probability Calculator[/bold cyan on black ]")
        print("Probability is the measure of the likelihood that an event will occur. It is calculated as the ratio of the number of favorable outcomes to the total number of possible outcomes.")
        try:
            favorable_outcomes = int(input("Hey buddy!, Give the number of favorable outcomes: "))
            total_outcomes = int(input("Hey buddy!, Give the total number of possible outcomes: "))
            if total_outcomes <= 0:
                raise ValueError("Total outcomes must be greater than zero.")
            probability = favorable_outcomes / total_outcomes
            console.print(f"\n[bold cyan on black ]The probability is: {probability:.4f}[/bold cyan on black ]")
        except ValueError as e:
            console.print(f"[bold red on black]Invalid input! Error: {e}[/bold red on black]")    
    elif (
            "integrate" in user_input or 
            "integration" in user_input or 
            "find the integral" in user_input or 
            "find integral" in user_input):
                                            
        from sympy import symbols, integrate, sympify, E
        from sympy.abc import x
        speak("Let's calculate the integral! ")
        expr_input = input("Enter the expression to integrate w.r.t x: ")
        try:
                expr = sympify(expr_input, locals={"e": E})
        except Exception as e:
                console.print("[bold red on black ]Invalid expression. Please check syntax.[/bold red on black ]")
                continue

        mode = input("Enter mode (definite / indefinite): ").strip().lower()

        if mode == "definite":
            try:
                a = float(input("Enter lower limit: "))
                b = float(input("Enter upper limit: "))
                result = integrate(expr, (x, a, b))
                console.print(f"\n[bold cyan on black]Definite integral of {expr_input} from {a} to {b} is:[/bold cyan on black]")
            except Exception as e:
                console.print("[bold red on black ]Invalid limits! Try again.[/bold red on black ]")
            continue
        else:
            result = integrate(expr, x)
            console.print(f"\n[bold cyan on black ]Indefinite integral of {expr_input} w.r.t x is:[/bold cyan on black ]")
            console.print(result, style="bold green on black")
    elif("priposition" in user_input or "proposition" in user_input or "propositional logic" in user_input or "calculate proposition" in user_input or "find proposition" in user_input):
        speak("Let's calculate proposition! ")
        console.print("\n[bold cyan on black ]Propositional Logic Calculator[/bold cyan on black ]")
        print("Propositional logic deals with propositions that can be either true or false.")
        print("It uses logical operators like AND, OR, NOT, etc. to combine propositions.")
        try:
            prop1 = input("Hey buddy!, Givethe first proposition (e.g., P): ")
            prop2 = input("Hey buddy!, Give the second proposition (e.g., Q): ")
            operator = input("Hey buddy!, Give the logical operator (AND/OR/NOT): ").strip().upper()
            if operator == "AND":
                result = f"{prop1} AND {prop2}"
            elif operator == "OR":
                result = f"{prop1} OR {prop2}"
            elif operator == "NOT":
                result = f"NOT {prop1}"
            else:
                raise ValueError("Invalid operator! Use AND, OR, or NOT.")
            console.print(f"\n[bold cyan on black ]The result of the proposition is: {result}[/bold cyan on black ]")
        except ValueError as e:
            console.print(f"[bold red on black ]Invalid input! Error: {e}[/bold red on black ]")
    elif("factorial" in user_input or "find factorial" in user_input or "calculate factorial" in user_input or "factorial of number" in user_input):
        speak("Let's calculate the factorial! ")
        try:
            num = int(input("Hey buddy!, Give a non-negative integer: "))
            if num < 0:
                console.print("[bold red on black ]Factorial is not defined for negative numbers.[/bold red on black ]")
                continue
            factorial = math.factorial(num)
            console.print(f"\n[bold cyan on black ]Factorial of {num} is: {factorial}[/bold cyan on black ]")
        except ValueError:
            console.print("[bold red on black ]Invalid input! Please enter a valid non-negative integer.[/bold red on black ]")
    elif("odd numbers range"in user_input or\
    "display odd number range" in user_input or\
    "find odd number range" in user_input or\
    "find odd numbers in given range" in user_input or\
    "display odd number in given range" in user_input):
        speak("Let's find the odd numbers in a given range! ")
        start = int(input("Enter the starting number: "))
        end = int(input("Enter the ending number: "))
        odd_numbers = [num for num in range(start, end + 1)if num % 2 != 0]
        console.print("The odd number range are : ",style="bold cyan on black ")
        console.print(f"\n[bold cyan on black ]odd numbers from {start} to {end}:[/bold cyan on black ]")
        console.print(odd_numbers,style="bold cyan on black ")    
    elif ("perimeter of square" in user_input or
        "find perimeter of square" in user_input or
        "calculate perimeter of square" in user_input or
        "square perimeter" in user_input):
        speak("Let's calculate the perimeter of a square! ")
        console.print("\n[bold cyan on black ]Perimeter of Square Calculator[/bold cyan on black ]")
        try:
            side = float(input("Enter the side length of the square: "))
            perimeter = 4 * side
            console.print(f"\n[bold cyan on black]Perimeter of the square is: {perimeter}[/bold cyan on black]")
        except ValueError:
                console.print("[bold red on black]Invalid input! Please enter a valid number.[/bold red on black]")
    elif ("perimeter of circle" in user_input or
        "find perimeter of circle" in user_input or
        "calculate perimeter of circle" in user_input or
        "circle perimeter" in user_input):
        speak("Let's calculate the perimeter of a circle! ")
        console.print("\n[bold cyan on black]Perimeter of Circle Calculator[/bold cyan on black]")
        radius = float(input("Enter the radius of the circle: "))
        perimeter = 2 * math.pi * radius
        print(f"The perimeter of the circle is: {perimeter}")
    elif("area of cube" in user_input or "find the area of cube" in user_input or "calculate area of cube" in user_input or "cube area" in user_input):
        speak("Let's calculate the area of a cube! ")
        console.print("\n[bold cyan on black]Area of Cube Calculator[/bold cyan on black]")
        try:
            side = float(input("Hey buddy!, Give the side length of the cube: "))
            area = 6 * (side ** 2)
            console.print(f"\n[bold cyan on black]Area of the cube is: {area}[/bold cyan on black]")
        except ValueError:
            console.print("[bold red on black]Invalid input! Please enter a valid number.[/bold red on black]")
    elif("volume of cube" in user_input or "find the volume of cube" in user_input or "calculate volume of cube" in user_input or "cube volume" in user_input):
        speak("Let's calculate the volume of a cube! ")
        console.print("\n[bold cyan on black]Volume of Cube Calculator[/bold cyan on black]")
        try:
            side = float(input("Hey buddy!, Give the side length of the cube: "))
            volume = side ** 3
            console.print(f"\n[bold cyan on black]Volume of the cube is: {volume}[/bold cyan on black]")
        except ValueError:
            console.print("[bold red on black]Invalid input! Please enter a valid number.[/bold red on black]")
    elif("area of parallelogram" in user_input or "find the area of parallelogram" in user_input or "calculate area of parallelogram" in user_input or "parallelogram area" in user_input):        
        speak("Let's calculate the area of a parallelogram! ")
        console.print("\n[bold cyan on black]Area of Parallelogram Calculator[/bold cyan on black]")
        try:
            base = float(input("Hey buddy!, Give the base of the parallelogram: "))
            height = float(input("Hey buddy!, Give the height of the parallelogram: "))
            area = base * height
            console.print(f"\n[bold cyan on black]Area of the parallelogram is: {area}[/bold cyan on black]")
        except ValueError:
            console.print("[bold red on black]Invalid input! Please enter valid numbers.[/bold red on black]")
    elif("area of trapezium" in user_input or "find the area of trapezium" in user_input or "calculate area of trapezium" in user_input or "trapezium area" in user_input):
        speak("Let's calculate the area of a trapezium! ")
        console.print("\n[bold cyan on black]Area of Trapezium Calculator[/bold cyan on black]")
        try:
            base1 = float(input("Hey buddy!, Give the length of base 1: "))
            base2 = float(input("Hey buddy!, Give the length of base 2: "))
            height = float(input("Hey buddy!, Give the height of the trapezium: "))
            area = 0.5 * (base1 + base2) * height
            console.print(f"\n[bold cyan on black]Area of the trapezium is: {area}[/bold cyan on black]")
        except ValueError:
            console.print("[bold red on black]Invalid input! Please enter valid numbers.[/bold red on black]") 
    elif("area of rhombus" in user_input or "find the area of rhombus" in user_input or "calculate area of rhombus" in user_input or "rhombus area" in user_input):
        speak("Let's calculate the area of a rhombus! ")
        console.print("\n[bold cyan on black]Area of Rhombus Calculator[/bold cyan on black]")
        try:
            diagonal1 = float(input("Hey buddy!, Give the length of diagonal 1: "))
            diagonal2 = float(input("Hey buddy!, Give the length of diagonal 2: "))
            area = 0.5 * diagonal1 * diagonal2
            console.print(f"\n[bold cyan on black]Area of the rhombus is: {area}[/bold cyan on black]")
        except ValueError:
            console.print("[bold red on black]Invalid input! Please enter valid numbers.[/bold red on black]")
    elif("volueme of cylinder" in user_input or "find the volume of cylinder" in user_input or "calculate volume of cylinder" in user_input or "cylinder volume" in user_input):
        speak("Let's calculate the volume of a cylinder! ")
        console.print("\n[bold cyan on black]Volume of Cylinder Calculator[/bold cyan on black]")
        try:
            radius = float(input("Hey buddy!, Give the radius of the cylinder: "))
            height = float(input("Hey buddy!, Give the height of the cylinder: "))
            volume = math.pi * (radius ** 2) * height
            console.print(f"\n[bold cyan on black]Volume of the cylinder is: {volume}[/bold cyan on black]")
        except ValueError:
            console.print("[bold red on black]Invalid input! Please enter valid numbers.[/bold red on black]")
    elif("volume of cone" in user_input or "find the volume of cone" in user_input or "calculate volume of cone" in user_input or "cone volume" in user_input):
        speak("Let's calculate the volume of a cone! ")
        console.print("\n[bold cyan on black]Volume of Cone Calculator[/bold cyan on black]")
        try:
            radius = float(input("Hey buddy!, Give the radius of the cone: "))
            height = float(input("Hey buddy!, Give the height of the cone: "))
            volume = (1/3) * math.pi * (radius ** 2) * height
            console.print(f"\n[bold cyan on black]Volume of the cone is: {volume}[/bold cyan on black]")
        except ValueError:
            console.print("[bold red on black]Invalid input! Please enter valid numbers.[/bold red on black]")
    elif("volume of sphere" in user_input or "find the volume of sphere" in user_input or "calculate volume of sphere" in user_input or "sphere volume" in user_input):
        speak("Let's calculate the volume of a sphere! ")
        console.print("\n[bold cyan on black]Volume of Sphere Calculator[/bold cyan on black]")
        try:
            radius = float(input("Hey buddy!, Give the radius of the sphere: "))
            volume = (4/3) * math.pi * (radius ** 3)
            console.print(f"\n[bold cyan on black]Volume of the sphere is: {volume}[/bold cyan on black]")
        except ValueError:
            console.print("[bold red on black]Invalid input! Please enter a valid number.[/bold red on black]")
    elif("stardard deviation" in user_input or "calculate standard deviation" in user_input or "find standard deviation" in user_input or "standard deviation of data" in user_input):
        speak("Let's calculate the standard deviation! ")
        console.print("\n[bold cyan on black]Standard Deviation Calculator[/bold cyan on black]")
        try:
            data = input("Enter the data points separated by commas: ")
            data_points = [float(x.strip()) for x in data.split(",")]
            if len(data_points) == 0:
                raise ValueError("No data points provided.")
            mean = sum(data_points) / len(data_points)
            variance = sum((x - mean) ** 2 for x in data_points) / len(data_points)
            std_deviation = math.sqrt(variance)
            console.print(f"\n[bold cyan on black]Standard Deviation of the given data is: {std_deviation}[/bold cyan on black]")
        except ValueError as e:
            console.print(f"[bold red on black]Invalid input! Error: {e}[/bold red on black]")
    elif("variance" in user_input or "calculate variance" in user_input or "find variance" in user_input or "variance of data" in user_input):
        speak("Let's calculate the variance! ")
        console.print("\n[bold cyan on black]Variance Calculator[/bold cyan on black]")
        try:
            data = input("Enter the data points separated by commas: ")
            data_points = [float(x.strip()) for x in data.split(",")]
            if len(data_points) == 0:
                raise ValueError("No data points provided.")
            mean = sum(data_points) / len(data_points)
            variance = sum((x - mean) ** 2 for x in data_points) / len(data_points)
            console.print(f"\n[bold cyan on black]Variance of the given data is: {variance}[/bold cyan on black]")
        except ValueError as e:
            console.print(f"[bold red on black]Invalid input! Error: {e}[/bold red on black]")
    elif("mean" in user_input or "calculate mean" in user_input or "find mean" in user_input or "mean of data" in user_input):
        speak("Let's calculate the mean! ")
        console.print("\n[bold cyan on black]Mean Calculator[/bold cyan on black]")
        try:
            data = input("Enter the data points separated by commas: ")
            data_points = [float(x.strip()) for x in data.split(",")]
            if len(data_points) == 0:
                raise ValueError("No data points provided.")
            mean = sum(data_points) / len(data_points)
            console.print(f"\n[bold cyan on black]Mean of the given data is: {mean}[/bold cyan on black]")
        except ValueError as e:
            console.print(f"[bold red on black]Invalid input! Error: {e}[/bold red on black]")
    elif("median" in user_input or "calculate median" in user_input or "find median" in user_input or "median of data" in user_input):
        speak("Let's calculate the median! ")
        console.print("\n[bold cyan on black]Median Calculator[/bold cyan on black]")
        try:
            data = input("Enter the data points separated by commas: ")
            data_points = [float(x.strip()) for x in data.split(",")]
            if len(data_points) == 0:
                raise ValueError("No data points provided.")
            data_points.sort()
            n = len(data_points)
            if n % 2 == 0:
                median = (data_points[n // 2 - 1] + data_points[n // 2]) / 2
            else:
                median = data_points[n // 2]
            console.print(f"\n[bold cyan on black]Median of the given data is: {median}[/bold cyan on black]")
        except ValueError as e:
            console.print(f"[bold red on black]Invalid input! Error: {e}[/bold red on black]")
    elif("mode" in user_input or "calculate mode" in user_input or "find mode" in user_input or "mode of data" in user_input):
        speak("Let's calculate the mode! ")
        console.print("\n[bold cyan on black]Mode Calculator[/bold cyan on black]")
        try:
            data = input("Enter the data points separated by commas: ")
            data_points = [x.strip() for x in data.split(",")]
            if len(data_points) == 0:
                raise ValueError("No data points provided.")
            frequency = {}
            for item in data_points:
                frequency[item] = frequency.get(item, 0) + 1
            max_freq = max(frequency.values())
            modes = [key for key, value in frequency.items() if value == max_freq]
            console.print(f"\n[bold cyan on black]Mode(s) of the given data is/are: {', '.join(modes)}[/bold cyan on black]")
        except ValueError as e:
            console.print(f"[bold red on black]Invalid input! Error: {e}[/bold red on black]")
    elif("area of triangle" in user_input or "find the area of triangle" in user_input or "calculate area of triangle" in user_input or "triangle area" in user_input):
        speak("Let's calculate the area of a triangle! ")
        console.print("\n[bold cyan on black]Area of Triangle Calculator[/bold cyan on black]")
        try:
            base = float(input("Hey buddy!, Give the base of the triangle: "))
            height = float(input("Hey buddy!, Give the height of the triangle: "))
            area = 0.5 * base * height
            console.print(f"\n[bold cyan on black]Area of the triangle is: {area}[/bold cyan on black]")
        except ValueError:
            console.print("[bold red on black]Invalid input! Please enter valid numbers.[/bold red on black]")
    elif("area of circle" in user_input or "find the area of circle" in user_input or "calculate area of circle" in user_input or "circle area" in user_input):
        speak("Let's calculate the area of a circle! ")
        console.print("\n[bold cyan on black]Area of Circle Calculator[/bold cyan on black]")
        try:
            radius = float(input("Hey buddy!, Give the radius of the circle: "))
            area = math.pi * (radius ** 2)
            console.print(f"\n[bold cyan on black]Area of the circle is: {area}[/bold cyan on black]")
        except ValueError:
            console.print("[bold red on black]Invalid input! Please enter a valid number.[/bold red on black]")        
    elif("perimeter of triangle" in user_input or "find the perimeter of triangle" in user_input or "calculate perimeter of triangle" in user_input or "triangle perimeter" in user_input):
        speak("Let's calculate the perimeter of a triangle! ")
        console.print("\n[bold cyan on black]Perimeter of Triangle Calculator[/bold cyan on black]")
        try:
            side1 = float(input("Hey buddy!, Give the length of side 1: "))
            side2 = float(input("Hey buddy!, Give the length of side 2: "))
            side3 = float(input("Hey buddy!, Give the length of side 3: "))
            perimeter = side1 + side2 + side3
            console.print(f"\n[bold cyan on black]Perimeter of the triangle is: {perimeter}[/bold cyan on black]")
        except ValueError:
            console.print("[bold red on black]Invalid input! Please enter valid numbers.[/bold red on black]")
    elif ("area of rectangle" in user_input or "find the area of rectangle" in user_input or "find area of rectangle" in user_input):
        speak("Let's calculate the area of a rectangle! ")
        console.print("\n[bold cyan on black]Area of Rectangle Calculator[/bold cyan on black]")
        try:
            length = float(input("Hey buddy!, Give the length of the rectangle: "))
            width = float(input("Hey buddy!, Give the width of the rectangle: "))
            area = length * width
            console.print(f"\n[bold cyan on black]Area of the rectangle is: {area}[/bold cyan on black]")
        except ValueError:
            console.print("[bold red on black]Invalid input! Please enter valid numbers.[/bold red on black]")    
    elif ("perimeter of rectangle" in user_input or
        "find perimeter of rectangle" in user_input or
        "calculate perimeter of rectangle" in user_input or
        "rectangle perimeter" in user_input): 
        speak("Let's calculate the perimeter of a rectangle! ")   
        leng = float(input("Enter the length of the rectangle: "))
        wide = float(input("Enter the width of the rectangle: "))
        perimeter  = 2 * (leng + wide)
        console.print(f"\n[bold cyan on black]Perimeter of the rectangle is: {perimeter}[/bold cyan on black]")
    elif ("area of square" in user_input or "find the area of square" in user_input or "calculate area of square" in user_input or "square area" in user_input):
        speak("Let's calculate the area of a square! ")
        console.print("\n[bold cyan on black]Area of Square Calculator[/bold cyan on black]")
        try:
            side = float(input("Enter the side length of the square: "))
            area = side ** 2
            console.print(f"\n[bold cyan on black]Area of the square is: {area}[/bold cyan on black]")
        except ValueError:
            console.print("[bold red on black]Invalid input! Please enter a valid number.[/bold red on black]")   
    elif ("fibonacci" in user_input or "fibonacci series" in user_input or "print fibonacci" in user_input):
        speak("Let's generate the Fibonacci series! ")
        n = int(input("Enter the number of terms: "))
        a, b = 0, 1
        fibonacci = []
        if n <= 0:
            console.print("Please enter a positive integer.", style="bold red on black ")
            continue
        elif n == 1:
            fibonacci.append(a)
        elif n == 2:
            fibonacci.extend([a, b])
        else:
            for _ in range(n):
                fibonacci.append(a)
                a, b = b, a + b
                console.print(f"\n[bold cyan on black]Fibonacci series of {n} terms:[/bold cyan on black]")
                console.print(fibonacci, style="bold cyan on black ")    
    elif("addition in matrix" in user_input or "matrix addition" in user_input or "addition of matrix" in user_input or "add matrix" in user_input
            or "mulitplication in matrix" in user_input or "matrix multiplication" in user_input 
            or"multiplication of matrix" in user_input or "multiply matrix" in user_input or" subtraction in matrix" in user_input
            or "matrix subtraction" in user_input or "subtraction of matrix" in user_input or "subtract matrix" in user_input or "divison in matrix" in user_input or "matrix division" in user_input or "division of matrix" in user_input or "divide matrix" in user_input):
        speak("Let's perform matrix operations! ")
        def get_matrix_input(name):
            rows = int(input(f"Enter number of rows in Matrix {name}: "))
            cols = int(input(f"Enter number of columns in Matrix {name}: "))
            print(f"Enter elements of Matrix {name} row-wise (space separated):")
            matrix = []
            for i in range(rows):
                while True:
                    row = input(f"Row {i+1}: ").split()
                    if len(row) != cols:
                        print(f"Invalid input. Please enter exactly {cols} values.")
                        continue
                    try:
                        matrix.append(list(map(float, row)))
                        break
                    except ValueError:
                        print("Please enter valid numbers.")
            return np.array(matrix)
        A = get_matrix_input("A")
        B = get_matrix_input("B")
        print("\nChoose Operation:")
        print("Add as Addition")
        print("Sub as Subtraction")
        print("Mult as Multiplication")
        print("Divide as Division (Element-wise)")
        choice = input("Enter choice (Add/Sub/Mult/Divide): ")
        try:
            if choice == 'Add':
                result = A + B
                console.print("\n[bold cyan on black]Matrix Addition Result:[/bold cyan on black]" + str(result))
            elif choice == 'Sub':
                result = A - B
                console.print("\n[bold cyan on black]Matrix Subtraction Result:[/bold cyan on black]"+ str(result))
            elif choice == 'Mult':
                result = np.dot(A, B)
                console.print("\n[bold cyan on black]Matrix Multiplication Result:[/bold cyan on black]"+ str(result))
            elif choice == 'Divide':
                result = A / B
                console.print("\n[bold cyan on black]Matrix Element-wise Division Result:[/bold cyan on black]"+ str(result))
            else:
                print("Invaild choice")
        except Exception as e:
            print("Error occured", e)                     
            
    elif("percentage" in user_input or "calculate percentage" in user_input or "find percentage" in user_input or "calculate the percentage" in user_input or "find the percentage" in user_input):
        console.print(" Let's calculate the percentage! ",style="bold black on black")
        speak("Let's calculate the percentage! ")
        console.print(" PERCENTAGE is a way of expressing a number as a fraction of 100.",style="bold cyan on black ")
        console.print(" value defines: The number you alredy known a part from total e.g. 20/140",style="bold cyan on black ")
        console.print(" here 20 is value ",style= "bold black on black")
        console.print(" Total defines: total value e.g. 20/140 ",style="bold black on black")
        console.print(" here 140 is total value ",style=" bold black on black")
        part = float(input("Hey buddy!, Give the value (e.g., 120): "))
        whole = float(input("Hey buddy!,Give the total (e.g., 40): "))
        percentage = (part* 100) / whole
        console.print(f"\n{part} is {percentage}% of {whole:.2f} \n THE ANSWER IS {percentage:.2f}.\n",style="bold cyan on black ")
        
    elif("prime number" in user_input or "prime number in the range" in user_input or "find prime numbers in range" in user_input or "display the range of prime numbers" in user_input or "display the prime numbers in range" in user_input or "list the prime numbers in range" in user_input or "primenumbers" in user_input or "list out the prime numbers "in user_input or "list out prime numbers" in user_input or "find the prime numbers in range" in user_input or "display the prime numbers" in user_input ):
        console.print(" Enter the range of prime number then you get prime number list intial state to final state. ",style="bold black on black")
        end = int(input("Enter the end range: "))
        console.print(f"\nPrime numbers from 1 to {end} are:\n", style="bold cyan on black ")
        for num in range(2, end + 1):
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                console.print(num, end=" ",style="cyan on black ")
    elif("pythagorean theorem" in user_input or "pythagoras" in user_input or "pythagorean" in user_input or "pythagorean theorem calculator" in user_input):
        speak("Let's calculate using Pythagorean theorem! ")
        console.print("\n[bold cyan on black]Pythagorean Theorem Calculator[/bold cyan on black]")
        console.print("The Pythagorean theorem states that in a right triangle, the square of the length of the hypotenuse is equal to the sum of the squares of the lengths of the other two sides.",style="bold cyan on black")
        try:
            a = float(input("Hey buddy! Give the length of side a: "))
            b = float(input("Hey buddy! Give the length of side b: "))
            c = math.sqrt(a**2 + b**2)
            console.print(f"\n[bold cyan on black]The length of the hypotenuse (c) is: {c}[/bold cyan on black]")
        except ValueError:
            console.print("[bold red on black]Invalid input! Please enter valid numbers.[/bold red on black]")
            
    elif("line graph" in user_input or "linegraph" in user_input or "display the line graph" in user_input 
        or "draw line graph" in user_input or "graph" in user_input or "display the graph" in user_input 
        or "draw the graph" in user_input or "draw graph" in user_input or "display graph" in user_input):
        speak("Let's create a line graph! ")

        console.print("[bold cyan on black]Graph-?[/bold cyan on black] Hey buddy please enter X and Y values.")

        x_input = input("Hey buddy! Give the X values (comma-separated): ")
        y_input = input("Hey buddy! Give the Y values (comma-separated): ")

        x = list(map(str, x_input.split(',')))      # Labels
        y = list(map(int, y_input.split(',')))      # Y values
        x_numeric = list(range(len(x)))             # For plotting

        # Create figure and axis
        fig, ax = plt.subplots()
        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')

        line, = ax.plot([], [], color='white', alpha=0.4,marker='o', linestyle='dashed', linewidth=2)
        bars = ax.bar(x_numeric, [0]*len(y), color='aqua', alpha=0.2)

        ax.set_xlim(-0.5, len(x)-0.5)
        ax.set_ylim(0, max(y) + 10)

        ax.set_title("MATH AI's  Graph", color='white')
        ax.set_xlabel("X - Labels", color='white')
        ax.set_ylabel("Y - Values", color='white')  
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.title.set_color('white')
        plt.xticks(ticks=x_numeric, labels=x, color='white')
        plt.grid(True, linestyle='--', alpha=0.2, color='white')

        # Animate function
        def animate(i):
            line.set_data(x_numeric[:i+1], y[:i+1])
            for j in range(i+1):
                bars[j].set_height(y[j])
            return [line] + list(bars)

        ani = FuncAnimation(fig, animate, frames=len(x), interval=700, repeat=False)
        plt.tight_layout()
        plt.show()
        console.print("[bold cyan on black] Hey buddy!,Your animated  graph is ready![/bold cyan on black]")
    elif("pie chart" in user_input or "piechart" in user_input or"display the piechart" in user_input or"draw pie chart" in user_input 
            or "pie" in user_input or "display pie chart" in user_input or "display piechart" in user_input or "draw the pie chart" in user_input):
        speak("Let's create a pie chart! ")
        labels_input = input("Hey buddy !, Give the  LABELS  which means THE NAME(comma-separated): ")  
        sizes_input = input("Hey buddy!, Give the SIZE which means NUMERIC VALUES (comma-separated): ")    
        labels = [label.strip() for label in labels_input.split(',')]
        sizes = list(map(int, sizes_input.split(',')))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.title("Your Pie Chart")
        plt.axis('equal')
        plt.show()
        console.print(" Hey buddy ! , your pie chart is ready! 🍰",style="bold cyan on black")
        exit()
    else:
        console.print("I can't understand that, please try different keywords buddy.", style="bold red on black ")
        speak("I can't understand that, please try different keywords buddy.")
        input("Press Enter to continue...")
    
    