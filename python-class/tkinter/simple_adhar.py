import tkinter as tk
from tkinter import messagebox

# Function to submit form
def submit_form():
    name = name_entry.get()
    dob = dob_entry.get()
    gender = gender_var.get()
    address = address_entry.get("1.0", tk.END)
    mobile = mobile_entry.get()

    if name and dob and gender and address.strip() and mobile:
        messagebox.showinfo("Form Submitted", f"Aadhaar Form Submitted Successfully!\n\nName: {name}\nDOB: {dob}\nGender: {gender}\nMobile: {mobile}")
    else:
        messagebox.showwarning("Incomplete", "Please fill all the fields.")

# Create main window
root = tk.Tk()
root.title("Aadhaar Card Application Form")
root.geometry("400x500")
root.config(padx=20, pady=20)

# Heading
tk.Label(root, text="Aadhaar Card Application", font=("Arial", 16, "bold")).pack(pady=10)

# Name
tk.Label(root, text="Full Name").pack(anchor="w")
name_entry = tk.Entry(root, width=40)
name_entry.pack(pady=5)

# DOB
tk.Label(root, text="Date of Birth (DD/MM/YYYY)").pack(anchor="w")
dob_entry = tk.Entry(root, width=40)
dob_entry.pack(pady=5)

# Gender
tk.Label(root, text="Gender").pack(anchor="w")
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack(anchor="w")
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack(anchor="w")
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other").pack(anchor="w")

# Address
tk.Label(root, text="Address").pack(anchor="w")
address_entry = tk.Text(root, width=30, height=4)
address_entry.pack(pady=5)

# Mobile
tk.Label(root, text="Mobile Number").pack(anchor="w")
mobile_entry = tk.Entry(root, width=40)
mobile_entry.pack(pady=5)

# Submit Button
tk.Button(root, text="Submit Form", bg="green", fg="white", command=submit_form).pack(pady=20)

# Run app
root.mainloop()
