import streamlit as st
import math

# --- Page Configuration ---
st.set_page_config(page_title="Scientific Calculator", page_icon="🧮", layout="centered")

# --- Title ---
st.title("🧮 Smooth Scientific Calculator")
st.markdown("### Perform basic and advanced mathematical operations with ease!")

# --- Input Fields ---
st.header("Enter Numbers:")
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number (optional)", value=0.0)

# --- Operation Selection ---
st.header("Choose an Operation")
operation = st.selectbox(
    "Select operation type",
    (
        "Addition (+)",
        "Subtraction (-)",
        "Multiplication (×)",
        "Division (÷)",
        "Power (xⁿ)",
        "Square Root (√x)",
        "Logarithm (log₁₀)",
        "Natural Log (ln)",
        "Sine (sin)",
        "Cosine (cos)",
        "Tangent (tan)",
        "Factorial (n!)"
    )
)

# --- Calculate Button ---
if st.button("Calculate ✨"):
    try:
        # Basic arithmetic operations
        if operation == "Addition (+)":
            result = num1 + num2
        elif operation == "Subtraction (-)":
            result = num1 - num2
        elif operation == "Multiplication (×)":
            result = num1 * num2
        elif operation == "Division (÷)":
            if num2 == 0:
                st.error("❌ Cannot divide by zero!")
                st.stop()
            result = num1 / num2
        elif operation == "Power (xⁿ)":
            result = math.pow(num1, num2)
        elif operation == "Square Root (√x)":
            if num1 < 0:
                st.error("❌ Cannot find square root of a negative number!")
                st.stop()
            result = math.sqrt(num1)
        elif operation == "Logarithm (log₁₀)":
            if num1 <= 0:
                st.error("❌ Logarithm undefined for non-positive numbers!")
                st.stop()
            result = math.log10(num1)
        elif operation == "Natural Log (ln)":
            if num1 <= 0:
                st.error("❌ Natural log undefined for non-positive numbers!")
                st.stop()
            result = math.log(num1)
        elif operation == "Sine (sin)":
            result = math.sin(math.radians(num1))
        elif operation == "Cosine (cos)":
            result = math.cos(math.radians(num1))
        elif operation == "Tangent (tan)":
            result = math.tan(math.radians(num1))
        elif operation == "Factorial (n!)":
            if num1 < 0 or not float(num1).is_integer():
                st.error("❌ Factorial is only defined for non-negative integers!")
                st.stop()
            result = math.factorial(int(num1))
        else:
            result = "Unknown operation"

        # --- Display result ---
        st.success(f"✅ **Result:** {result}")

    except Exception as e:
        st.error(f"⚠️ Error: {e}")

# --- Footer ---
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit")
