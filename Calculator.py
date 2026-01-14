import tkinter as tk

def disc_calculate():
    try:
        price = float(entry_price.get())
        discount = float(entry_discount.get())
        total = price - (price * discount / 100)
        result.config(text=f"Final Price: Rp. {total:,.2f}")
    except:
        result.config(text="Input tidak valid!")

root = tk.Tk()
root.title("Discount Calculator")
root.geometry("400x300")

tk.Label(root, text="Original Price:").pack(pady=5)
entry_price = tk.Entry(root, width=30)
entry_price.pack()

tk.Label(root, text="Discount (%):").pack(pady=5)
entry_discount = tk.Entry(root, width=30)
entry_discount.pack()

tk.Button(root, text="Calculate", command=disc_calculate).pack(pady=15)

result = tk.Label(root, text="Final Price: Rp. 0.00")
result.pack(pady=10)

root.mainloop()
