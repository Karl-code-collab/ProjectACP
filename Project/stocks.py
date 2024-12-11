import tkinter as tk
import customtkinter as ctk
import mysql.connector

class Stocks:
    def __init__(self, root, db, cursor, main_front):
        self.root = root
        self.db = db
        self.cursor = cursor
        self.main = main_front

        #stocks
    def show_stocks_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.stocks_frame = tk.Frame(self.root, bg="#2B2B3E")
        self.stocks_frame.pack(fill="both", expand=True)
        self.root.geometry("1200x700")

        title_label = ctk.CTkLabel(self.stocks_frame, text="BetaMax", font=("Helvetica", 24, "bold"))
        title_label.pack(pady=(20, 10), padx=20, anchor="w")

        subtitle_label = ctk.CTkLabel(self.stocks_frame, text="Available Stocks", font=("Helvetica", 36, "bold"))
        subtitle_label.pack(pady=(10, 30))

        self.cards_frame = ctk.CTkFrame(self.stocks_frame, fg_color="transparent")
        self.cards_frame.pack(pady=20)

        blood_types = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

        try: #retrieving the number of donors with 'Processed' status
            for blood_type in blood_types:
                self.cursor.execute(
                    """SELECT COUNT(*) FROM donor_users WHERE blood_group = %s AND status = 'Processed';""",
                    (blood_type,)
                )
                count = self.cursor.fetchone()[0]

                card = ctk.CTkFrame(self.cards_frame, width=250, height=150, corner_radius=10, fg_color="white")
                card.grid(row=blood_types.index(blood_type) // 4, column=blood_types.index(blood_type) % 4, padx=10, pady=10)

                blood_type_label = ctk.CTkLabel(card, text=blood_type, font=("Helvetica", 36, "bold"), text_color="#2B2B3E")
                blood_type_label.place(relx=0.5, rely=0.3, anchor="center")

                amount_label = ctk.CTkLabel(card, text=str(count), font=("Helvetica", 36, "bold"), text_color="#2B2B3E")
                amount_label.place(relx=0.5, rely=0.7, anchor="center")

        except mysql.connector.Error as err:
            print(f"Something went wrong: {err}")

        back_button_stocks = ctk.CTkButton(self.stocks_frame, text="Back to Menu", width=200, height=40, fg_color="#3498DB", hover_color="#2980B9", font=("Helvetica", 16, "bold"),
                                           command=self.main.front_page)
        back_button_stocks.pack(pady=30)


