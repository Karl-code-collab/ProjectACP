import tkinter as tk
import mysql.connector
import customtkinter as ctk
from admin import Admin
from donor import Donor
from requestor import Requestor
from stocks import Stocks


#main file run here
class BloodDonationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("BetaMax - A Blood Donation Management System")
        self.root.geometry("1200x700")
        self.root.iconbitmap('blood-donation.ico')
        self.root.resizable(False, False)

        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="blood_donation_db"

        )
        self.cursor = self.db.cursor()

        #declaration for the other files
        self.admin = Admin(self.root, self.db, self.cursor, self)
        self.donor = Donor(self.root, self.db, self.cursor, self)
        self.requestor = Requestor(self.root, self.db, self.cursor, self)
        self.stocks = Stocks(self.root, self.db, self.cursor, self)

        self.front_page()

    #front page
    def front_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.geometry("1200x700")

        main_container = tk.Frame(self.root)
        main_container.pack(fill="both", expand=True)

        left_frame = tk.Frame(main_container, bg="#F5F5F5")
        left_frame.pack(side="left", fill="both", expand=True)

        right_frame = tk.Frame(main_container, bg="#2B2B3E")
        right_frame.pack(side="right", fill="both", expand=True)

        title_container = tk.Frame(left_frame, bg="#F5F5F5")
        title_container.place(relx=0.5, rely=0.45, anchor="center")

        system_name = tk.Label(title_container, text="BetaMax", font=("Helvetica", 40, "bold"), bg="#F5F5F5", fg="#2B2B3E")
        system_name.pack()

        system_label = tk.Label(title_container, text="A Blood Donation\nManagement System", font=("Helvetica", 20), bg="#F5F5F5", fg="#2B2B3E", justify="center")
        system_label.pack(pady=(10, 0))

        button_container = tk.Frame(right_frame, bg="#2B2B3E")
        button_container.place(relx=0.5, rely=0.5, anchor="center")

        button_width = 300
        button_height = 50
        button_color = "#2ECC71"
        font_color = ("Helvetica", 16)

        avail_button = ctk.CTkButton(button_container, text="Check Availability", fg_color=button_color, text_color="white", font=font_color, width=button_width, height=button_height, corner_radius=15,
                                    command=self.stocks.show_stocks_frame)
        avail_button.pack(pady=10)

        donate_button = ctk.CTkButton(button_container, text="Donate Blood", fg_color=button_color, text_color="white", font=font_color, width=button_width, height=button_height, corner_radius=15,
                                    command=self.donor.show_login_frame)
        donate_button.pack(pady=10)

        request_button = ctk.CTkButton(button_container, text="Request Blood", fg_color=button_color, text_color="white", font=font_color, width=button_width, height=button_height, corner_radius=15,
                                    command=self.requestor.show_login_req_frame)
        request_button.pack(pady=10)

        admin_button = ctk.CTkButton(button_container, text="Manage (Admin only)", fg_color=button_color, text_color="white", font=font_color, width=button_width, height=button_height, corner_radius=15,
                                    command=self.admin.admin_login_frame)
        admin_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = BloodDonationSystem(root)
    root.mainloop()

