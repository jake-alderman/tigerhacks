import customtkinter

customtkinter.set_appearance_mode("dark")

customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def login():
    print("test")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)
label = customtkinter.CTkLabel(master=frame, text="test")
label.pack(pady=12, padx=10)

    
root.mainloop()