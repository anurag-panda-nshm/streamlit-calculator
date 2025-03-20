import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, integrate, sympify

# Add custom CSS for consistent styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
        font-family: Arial, sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# Navigation bar
st.sidebar.title("Navigation")
st.sidebar.markdown("---")  # Add a separator
app_mode = st.sidebar.radio("Choose the app mode:", [
    "Graphing Calculator", 
    "Integration Calculator", 
    "Derivative Calculator", 
    "Trigonometric Calculator", 
    "Simple Calculator"
])

if app_mode == "Graphing Calculator":
    st.title("📈 Graphing Calculator")
    st.markdown("---")  # Add a separator
    st.write("Enter a mathematical function to plot its graph.")

    # Input for the mathematical function
    function = st.text_input(
        "Function (use 'x' as the variable, e.g., x**2 + 2*x - 3):", 
        "x**2", 
        help="Enter a valid mathematical expression using 'x' as the variable."
    )

    # Input for the range of x-axis
    col1, col2 = st.columns(2)
    with col1:
        x_min = st.number_input("X-axis minimum value:", value=-10)
    with col2:
        x_max = st.number_input("X-axis maximum value:", value=10)

    # Plot the graph
    if st.button("Plot Graph"):
        try:
            # Generate x values
            x = np.linspace(x_min, x_max, 500)
            # Evaluate the function
            y = eval(function)
            
            # Create the plot
            plt.figure(figsize=(8, 6))
            plt.plot(x, y, label=f"y = {function}")
            plt.title("Graph of the Function")
            plt.xlabel("x")
            plt.ylabel("y")
            plt.axhline(0, color='black', linewidth=0.5, linestyle="--")
            plt.axvline(0, color='black', linewidth=0.5, linestyle="--")
            plt.grid(color='gray', linestyle='--', linewidth=0.5)
            plt.legend()
            
            # Display the plot
            st.pyplot(plt)
        except Exception as e:
            st.error(f"⚠️ An error occurred: {e}")

elif app_mode == "Integration Calculator":
    st.title("∫ Integration Calculator")
    st.markdown("---")
    st.write("Calculate definite and indefinite integrals of a mathematical function.")

    # Input for the mathematical function
    function = st.text_input("Function (use 'x' as the variable, e.g., x**2 + 2*x - 3):", "x**2")
    x = symbols('x')  # Define the variable

    # Indefinite integral
    if st.button("Calculate Indefinite Integral"):
        try:
            indefinite_integral = integrate(sympify(function), x)
            st.write(f"The indefinite integral of {function} is:")
            st.latex(f"\\int {function} \\, dx = {indefinite_integral}")
        except Exception as e:
            st.error(f"⚠️ An error occurred: {e}")

    st.markdown("---")
    st.write("Calculate definite integral:")
    lower_limit = st.number_input("Lower limit:", value=0.0)
    upper_limit = st.number_input("Upper limit:", value=1.0)

    if st.button("Calculate Definite Integral"):
        try:
            definite_integral = integrate(sympify(function), (x, lower_limit, upper_limit))
            st.write(f"The definite integral of {function} from {lower_limit} to {upper_limit} is:")
            st.latex(f"\\int_{{{lower_limit}}}^{{{upper_limit}}} {function} \\, dx = {definite_integral}")
        except Exception as e:
            st.error(f"⚠️ An error occurred: {e}")

elif app_mode == "Derivative Calculator":
    st.title("𝑓'(x) Derivative Calculator")
    st.markdown("---")
    st.write("Calculate the derivative of a mathematical function.")

    # Input for the mathematical function
    function = st.text_input("Function (use 'x' as the variable, e.g., x**2 + 2*x - 3):", "x**2")
    x = symbols('x')  # Define the variable

    # Calculate derivative
    if st.button("Calculate Derivative"):
        try:
            derivative = sympify(function).diff(x)
            st.write(f"The derivative of {function} is:")
            st.latex(f"\\frac{{d}}{{dx}}({function}) = {derivative}")
        except Exception as e:
            st.error(f"⚠️ An error occurred: {e}")

elif app_mode == "Trigonometric Calculator":
    st.title("📐 Trigonometric Calculator")
    st.markdown("---")
    st.write("Calculate the values of sin, cos, tan, cot, cosec, and sec for a given angle.")

    # Input for the angle in degrees
    angle = st.number_input("Enter the angle in degrees:", value=0.0)

    # Calculate trigonometric values
    if st.button("Calculate Trigonometric Values"):
        try:
            angle_rad = np.radians(angle)  # Convert angle to radians
            sin_val = np.sin(angle_rad)
            cos_val = np.cos(angle_rad)
            tan_val = np.tan(angle_rad)
            cot_val = 1 / tan_val if tan_val != 0 else "undefined"
            sec_val = 1 / cos_val if cos_val != 0 else "undefined"
            cosec_val = 1 / sin_val if sin_val != 0 else "undefined"

            # Display results
            st.write(f"sin({angle}°) = {sin_val}")
            st.write(f"cos({angle}°) = {cos_val}")
            st.write(f"tan({angle}°) = {tan_val}")
            st.write(f"cot({angle}°) = {cot_val}")
            st.write(f"sec({angle}°) = {sec_val}")
            st.write(f"cosec({angle}°) = {cosec_val}")
        except Exception as e:
            st.error(f"⚠️ An error occurred: {e}")

elif app_mode == "Simple Calculator":
    st.title("🧮 Simple Calculator")
    st.markdown("---")
    st.write("Perform basic arithmetic operations: addition, subtraction, multiplication, and division.")

    # Input for numbers
    num1 = st.number_input("Enter the first number:", value=0.0)
    num2 = st.number_input("Enter the second number:", value=0.0)

    # Select operation
    operation = st.selectbox("Select operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

    # Perform calculation
    if st.button("Calculate"):
        try:
            if operation == "Addition":
                result = num1 + num2
                st.write(f"The result of {num1} + {num2} is {result}")
            elif operation == "Subtraction":
                result = num1 - num2
                st.write(f"The result of {num1} - {num2} is {result}")
            elif operation == "Multiplication":
                result = num1 * num2
                st.write(f"The result of {num1} × {num2} is {result}")
            elif operation == "Division":
                if num2 != 0:
                    result = num1 / num2
                    st.write(f"The result of {num1} ÷ {num2} is {result}")
                else:
                    st.error("Division by zero is not allowed.")
        except Exception as e:
            st.error(f"⚠️ An error occurred: {e}")
else:
    st.title("Welcome to the Streamlit Calculator!")
    st.markdown("---")
    st.write("Use the sidebar to navigate between different calculators.")
