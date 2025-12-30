import tkinter as tk  # Library for creating GUI (display)

# This function will be executed when the "Calculate" button is pressed.
def calculate():
    # Get price value from input
    price = float(price_entry.get())

    # Get the discount value from the input
    discount = float(discount_entry.get())

    # Calculating the price after discount
    final_price = price * (1 - discount / 100)

    # Displays results to labels
    result_label.config(text=f"Final Price: Rp. {final_price:.2f}")

# Create the main window
root = tk.Tk()
root.title("Discount Calculator")
root.geometry("500x360")

# Frame to center all components to the center
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Application title
tk.Label(frame, text="Discount Calculator", font=("Arial", 14, "bold")).pack(pady=10)

# Label and price input
tk.Label(frame, text="Original Price:").pack()
price_entry = tk.Entry(frame, width=25)
price_entry.pack(pady=4)

# Discount labels and input
tk.Label(frame, text="Discount (%)").pack()
discount_entry = tk.Entry(frame, width=25)
discount_entry.pack(pady=4)

# Label to display results
result_label = tk.Label(frame, text="Final Price: -", font=("Arial", 10, "bold"))
result_label.pack(pady=12)

# Button to calculate
tk.Button(frame, text="Calculate", width=20, command=calculate).pack()

# Run the application
root.mainloop()