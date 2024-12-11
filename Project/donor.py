import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import re
import mysql.connector

class Donor:
    def __init__(self, root, db, cursor, main_front):
        self.root = root
        self.db = db
        self.cursor = cursor
        self.main = main_front

    def show_login_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.geometry("1000x600")

        main_container = tk.Frame(self.root)
        main_container.pack(fill="both", expand=True)

        left_frame = tk.Frame(main_container, bg="#F5F5F5")
        left_frame.pack(side="left", fill="both", expand=True)

        right_frame = tk.Frame(main_container, bg="#2B2B3E")
        right_frame.pack(side="right", fill="both", expand=True)

        title_container = tk.Frame(left_frame, bg="#F5F5F5")
        title_container.place(relx=0.5, rely=0.4, anchor="center")

        system_name = tk.Label(title_container, text="BetaMax", font=("Helvetica", 15, "bold"), bg="#F5F5F5", fg="#2B2B3E")
        system_name.pack()

        system_label = tk.Label(title_container, text="Login as Donor", font=("Helvetica", 25, "bold"), bg="#F5F5F5", fg="#2B2B3E", justify="center")
        system_label.pack(pady=(10, 0))

        container = tk.Frame(right_frame, bg="#2B2B3E")
        container.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(container, text="Registered email", bg="#2D2B3E", fg="white", font=("Helvetica", 16, "bold"), padx=5).pack(pady=(10, 10), anchor="w")
        donor_email = ctk.CTkEntry(container, width=350, height=50, placeholder_text="Registered Email", font=("Helvetica", 16, "bold"), fg_color="white", text_color="black", corner_radius=15)
        donor_email.pack(pady=(0, 10), anchor="w")

        tk.Label(container, text="Password", bg="#2D2B3E", fg="white", font=("Helvetica", 16, "bold"), padx=5).pack(pady=(10, 10), anchor="w")
        donor_pass = ctk.CTkEntry(container, width=350, height=50, placeholder_text="Password", font=("Helvetica", 16, "bold"), fg_color="white", text_color="black", show="*", corner_radius=10)
        donor_pass.pack(pady=(0, 10), anchor="w")

        login_admin_button = ctk.CTkButton(container, text="Login Now", fg_color="#2ECC71", text_color="white", font=("Helvetica", 16, "bold"), width=200, height=50, corner_radius=15, hover_color="#27AE60", command=lambda: self.login(donor_email.get().strip(), donor_pass.get()))
        login_admin_button.pack(pady=20)

        hyperlink_frame = tk.Frame(container, bg="#2B2B3E")
        hyperlink_frame.pack(pady=(0, 10))

        reg_donor_label = tk.Label(hyperlink_frame, text="Don't have an Account? ", bg="#2B2B3E", fg="white", font=("Helvetica", 12))
        reg_donor_label.pack(side=tk.LEFT)

        back_to_menu_link = tk.Label(hyperlink_frame, text="Register Now!", bg="#2B2B3E", fg="#50C878", font=("Helvetica", 12, "bold"), cursor="hand2")
        back_to_menu_link.pack(side=tk.LEFT)

        back_to_menu_link.bind("<Button-1>", lambda e: self.show_register_frame())

    def login(self, email, password):
        if not email:
            messagebox.showerror("Error Message", "Email is required!")
            return False
        elif not password:
            messagebox.showerror("Error Message", "Password is required!")
            return False

        try:
            self.cursor.execute("""SELECT * FROM donor_users WHERE email = %s AND password = %s""", (email, password))
            user = self.cursor.fetchone()

            if user:
                messagebox.showinfo("Success", "Login successful!")
                self.donor_dashboard(email, password)
            else:
                messagebox.showerror("Error", "Invalid username or password!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Login failed: {err}")

    def show_register_frame(self): #donor
        # Clear main container first
        for widget in self.root.winfo_children():
            widget.destroy()

        # Recreate and configure register frame
        self.register_frame = tk.Frame(self.root, bg="#2B2B3E")
        self.register_frame.pack(fill="both", expand=True)
        self.root.geometry("800x800")
        self.root.configure(bg="#2B2B3E")

        # Register Title
        title_label = tk.Label(self.register_frame, text="Register as Donor", font=("Helvetica", 30, "bold"),
                               bg="#2B2B3E", fg="white")
        title_label.pack(pady=30)

        # Form container
        form_frame = tk.Frame(self.register_frame, bg="#2B2B3E")
        form_frame.pack(padx=50)

        # styles
        label_style = {"bg": "#2B2B3E", "fg": "white", "font": ("Helvetica", 12)}
        entry_style = {"width": 225, "height": 35, "fg_color": "white", "text_color": "black", "corner_radius": 5}

        # fill up label
        row_fill = tk.Frame(form_frame, bg="#2B2B3E")
        row_fill.pack(fill="x", pady=5)

        tk.Label(row_fill, text="Enter the following:", bg="#2B2B3E", fg="#2ECC71", font="Helvetica 13 bold").grid(
            row=0, column=0, sticky="w", padx=(0, 25), pady=(0, 5))
        # full
        row_name = tk.Frame(form_frame, bg="#2B2B3E")
        row_name.pack(fill="x", pady=3)

        tk.Label(row_name, text="Full Name", **label_style).grid(row=0, column=0, sticky="w", padx=(0, 60))
        lastname = ctk.CTkEntry(row_name, placeholder_text="Enter your last name", **entry_style)
        lastname.grid(row=0, column=1, padx=10, pady=10)

        firstname = ctk.CTkEntry(row_name, placeholder_text="Enter your first name", **entry_style)
        firstname.grid(row=0, column=3, padx=10, pady=10)

        middle_i = ctk.CTkEntry(row_name, placeholder_text="MI", width=50, height=35, fg_color="white",
                                text_color="black", corner_radius=5)
        middle_i.grid(row=0, column=4, padx=10, pady=10)

        # contacts
        row_contact = tk.Frame(form_frame, bg="#2B2B3E")
        row_contact.pack(fill="x", pady=5)

        tk.Label(row_contact, text="Contact Number", **label_style).grid(row=0, column=0, sticky="w", padx=(0, 25))
        contactnumber = ctk.CTkEntry(row_contact, placeholder_text="Enter your contact number", width=540, height=35,
                                     fg_color="white", text_color="black", corner_radius=5)
        contactnumber.grid(row=0, column=1)

        # age
        row_age = tk.Frame(form_frame, bg="#2B2B3E")
        row_age.pack(fill="x", pady=5)

        tk.Label(row_age, text="Age", **label_style).grid(row=0, column=0, sticky="w", padx=(0, 110))
        age = ctk.CTkEntry(row_age, placeholder_text="Enter your age", width=540, height=35, fg_color="white",
                           text_color="black", corner_radius=5)
        age.grid(row=0, column=1)

        # gender menu
        row_gender = tk.Frame(form_frame, bg="#2B2B3E")
        row_gender.pack(fill="x", pady=5)

        tk.Label(row_gender, text="Gender", **label_style).grid(row=0, column=0, sticky="w", padx=(0, 77))
        gender = ctk.CTkOptionMenu(row_gender, values=["Male", "Female", "Other"], width=540, height=35,
                                   fg_color="#2471A3", button_color="#2471A3")
        gender.grid(row=0, column=1, padx=10)

        # blood group menu
        row_blood = tk.Frame(form_frame, bg="#2B2B3E")
        row_blood.pack(fill="x", pady=5)

        tk.Label(row_blood, text="Blood Group", **label_style).grid(row=0, column=0, sticky="w", padx=(0, 40))
        bloodtype = ctk.CTkOptionMenu(row_blood, values=["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"], width=540,
                                      height=35, fg_color="#2471A3", button_color="#2471A3")
        bloodtype.grid(row=0, column=1, padx=10)

        # full address text Field
        row_address = tk.Frame(form_frame, bg="#2B2B3E")
        row_address.pack(fill="x", pady=5)

        tk.Label(row_address, text="Full Address", **label_style).grid(row=0, column=0, sticky="w", padx=(0, 40))
        full_address = ctk.CTkEntry(row_address, placeholder_text="Enter your full address", width=540, height=35,
                                    fg_color="white", text_color="black", corner_radius=5)
        full_address.grid(row=0, column=1, padx=10)

        # email and pass
        row_label = tk.Frame(form_frame, bg="#2B2B3E")
        row_label.pack(fill="x", pady=5)

        tk.Label(row_label, text="Create your account", bg="#2B2B3E", fg="#2ECC71", font="Helvetica 13 bold").grid(
            row=0, column=0, sticky="w", padx=(0, 25), pady=(25, 5))


        # email address
        row_email = tk.Frame(form_frame, bg="#2B2B3E")
        row_email.pack(fill="x", pady=3)

        tk.Label(row_email, text="Email Address", **label_style).grid(row=0, column=0, sticky="w", padx=(0, 25))
        email = ctk.CTkEntry(row_email, placeholder_text="Enter your email address", width=540, height=35,
                             fg_color="white", text_color="black", corner_radius=5)
        email.grid(row=0, column=1, padx=10)

        # creating password
        row_create = tk.Frame(form_frame, bg="#2B2B3E")
        row_create.pack(fill="x", pady=10)

        tk.Label(row_create, text="Create Password", **label_style).grid(row=0, column=0, sticky="w", padx=(0, 8))
        create_pass = ctk.CTkEntry(row_create, placeholder_text="Enter password", show="•", width=540, height=35,
                                   fg_color="white", text_color="black", corner_radius=5)
        create_pass.grid(row=0, column=1, padx=10)

        # confirm pass
        row_confirm = tk.Frame(form_frame, bg="#2B2B3E")
        row_confirm.pack(fill="x", pady=10)

        tk.Label(row_confirm, text="Confirm Password", **label_style).grid(row=0, column=0, sticky="w", padx=(0, 3))
        confirm_pass = ctk.CTkEntry(row_confirm, placeholder_text="Confirm password", show="•", width=540, height=35,
                                    fg_color="white", text_color="black", corner_radius=5)
        confirm_pass.grid(row=0, column=1, padx=10)

        # Submit button & getting the values of the user input

        row_submit = tk.Frame(form_frame, bg="#2B2B3E")
        row_submit.pack(fill="x", pady=5)

        submit_btn = ctk.CTkButton(row_submit, text="Submit",
                                   command=lambda: self.register(firstname.get(), middle_i.get(), lastname.get(),
                                                                 contactnumber.get(), age.get(), gender.get(),
                                                                 bloodtype.get(), full_address.get(), email.get(),
                                                                 create_pass.get(), confirm_pass.get()),
                                   width=250, height=40, fg_color="#2ECC71", hover_color="#27AE60", corner_radius=5,font=ctk.CTkFont(size=16, weight="bold"))
        submit_btn.grid(row=0, column=1, padx=(100, 20), pady=10)

        back_btn = ctk.CTkButton(row_submit, text="Back", width=250, height=40, fg_color="#3498DB",
                                 hover_color="#2980B9", corner_radius=5, font=ctk.CTkFont(size=16, weight="bold", ),
                                 command=lambda: self.main.front_page())
        back_btn.grid(row=0, column=2, padx=(0, 20), pady=10)

    def register(self, first_name, mi, last_name, contact, age, gender, blood_group, address, email, password, confirm_password):
        if not first_name or not mi or not last_name or not contact or not age or not gender or not blood_group or not address or not email or not password or not confirm_password:  # check if empty
            messagebox.showerror("Error", "All fields are required!")

        if not self.email_validation(email):
            messagebox.showerror("Error", "Email is not valid")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        try:

            self.cursor.execute(
                """INSERT INTO donor_users (first_name, middle_initial, last_name, contact, age, gender, blood_group, status, address, email, password) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s)""",
                          (first_name, mi, last_name, contact, age, gender, blood_group, "Pending", address, email, password))
            self.db.commit()
            messagebox.showinfo("Success", "Registration successful!")
            self.show_login_frame()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Registration failed: {err}")

    def email_validation(self, email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        if re.match(email_regex, email):
            return True
        return False

    def donor_dashboard(self, email, donor_pass):
        for widget in self.root.winfo_children():  # clear
            widget.destroy()

        self.donor_dashboard_frame = tk.Frame(self.root, bg="white")
        self.donor_dashboard_frame.pack(fill="both", expand=True)
        self.root.geometry("1200x700")
        self.root.configure(bg="white")


        #getting the value
        self.cursor.execute(
            "SELECT first_name, middle_initial, last_name, blood_group, status, date_issued FROM donor_users WHERE email = %s AND password = %s",
            (email, donor_pass))
        result = self.cursor.fetchone()

        if result:
            first_name, middle_initial, last_name, blood_group, status, date_issued = result
            donor_fullname = f"{last_name.upper()}, {first_name.upper()} {middle_initial.upper()}."
            donor_blood_label = blood_group
            date_label = date_issued
            donor_status_label = status

            if donor_status_label == "Processed":
                label_all = {"bg": "white", "fg": "#2ECC71", "font": ("Helvetica", 15, "bold")}
                announce_label_donor = "Please proceed to the Clinic. Thank you!"

            elif donor_status_label == "Done":
                label_all = {"bg": "white", "fg": "#2ECC71", "font": ("Helvetica", 15, "bold")}
                announce_label_donor = "Thank you for your donation."

            else:
                donor_status_label = "Unprocessed"
                label_all = {"bg": "white", "fg": "#2B2B3E", "font": ("Helvetica", 15)}
                announce_label_donor = "Please wait for further updates. Thank you!"

            system_name_label = tk.Label(self.donor_dashboard_frame, text="BetaMax", font=("Helvetica", 18, "bold"),
                                         bg="white")
            system_name_label.pack(pady=(20, 10), padx=20, anchor="w")

            overview_donor = tk.Label(self.donor_dashboard_frame, text="Overview", font=("Helvetica", 20, "bold"),
                                      bg="white")
            overview_donor.pack(pady=(10, 10), anchor="center")

            info_frame_donor = tk.Frame(self.donor_dashboard_frame, bg="white")
            info_frame_donor.pack(pady=(10, 10), anchor="center")

            tk.Label(info_frame_donor, text="Name:", font=("Helvetica", 15, "bold"), bg="white").grid(row=0, column=0, padx=(10, 5), pady=5, sticky="e")

            tk.Label(info_frame_donor, text=donor_fullname, font=("Helvetica", 15), bg="white").grid(row=0, column=1, padx=(5, 10), pady=5, sticky="w")

            tk.Label(info_frame_donor, text="Type of Application:", font=("Helvetica", 15, "bold"), bg="white").grid(
                row=1, column=0, padx=(10, 5), pady=5, sticky="e")
            tk.Label(info_frame_donor, text=f"DONOR FOR BLOOD ({donor_blood_label})", font=("Helvetica", 15),
                     bg="white").grid(row=1, column=1, padx=(5, 10), pady=5, sticky="w")

            tk.Label(info_frame_donor, text="Date Issued:", font=("Helvetica", 15, "bold"), bg="white").grid(row=2, column=0, padx=(10, 5), pady=5, sticky="e")
            tk.Label(info_frame_donor, text=date_label, font=("Helvetica", 15), bg="white").grid(row=2, column=1, padx=(5, 10), pady=5, sticky="w")

            tk.Label(info_frame_donor, text="Status:", font=("Helvetica", 15, "bold"), bg="white").grid(row=3, column=0, padx=(10, 5), pady=5, sticky="e")
            tk.Label(info_frame_donor, text=donor_status_label, **label_all).grid(row=3, column=1, padx=(5, 10), pady=5, sticky="w")

            tk.Label(self.donor_dashboard_frame, text=announce_label_donor, font=("Helvetica", 18, "bold"),
                     bg="white").pack(pady=(30, 70), anchor="center")

            row_submit_text = tk.Frame(self.donor_dashboard_frame, bg="white")
            row_submit_text.pack(pady=(10, 10), anchor="center")

            button_frame = tk.Frame(row_submit_text, bg="white")
            button_frame.pack(fill="x", pady=(0, 20))

            submit_button = ctk.CTkButton(button_frame, text="Message Admin", width=250, height=50, fg_color="#2ECC71",
                                          hover_color="#27AE60", corner_radius=5,
                                          font=ctk.CTkFont(size=16, weight="bold"),
                                          command=lambda: self.message_admin(email))
            submit_button.pack(side="left", padx=10)

            back_button = ctk.CTkButton(button_frame, text="Back to Menu", width=250, height=50, fg_color="#3498DB",
                                        hover_color="#2980B9", corner_radius=5,
                                        font=ctk.CTkFont(size=16, weight="bold"), command=lambda: self.clear_frame())
            back_button.pack(side="left", padx=10)

        else:
            label = tk.Label(self.donor_dashboard_frame, text="User not found", font=("Arial", 24), fg="white",
                             bg="#2B2B3E")
            label.pack(pady=20, side="top", anchor="w")

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.main.front_page()

    def message_admin(self, email):
        admin_window = tk.Toplevel(self.root)
        admin_window.title("Message to Admin")
        admin_window.geometry("500x250")
        admin_window.configure(bg="white")
        admin_window.resizable(False, False)

        # Retrieve the user ID based on the email address
        self.cursor.execute("SELECT id FROM donor_users WHERE email = %s", (email,))
        user_id = self.cursor.fetchone()
        if not user_id:
            messagebox.showerror("Error", "User not found")
            return

        # Create and place the text box
        text_box = ctk.CTkTextbox(admin_window, height=150, width=450, bg_color="white", fg_color="#D3D3D3",
                                  text_color="#2B2B3E", corner_radius=5)
        text_box.pack(pady=20)

        row_submit_text_adm = tk.Frame(admin_window, bg="white")
        row_submit_text_adm.pack(pady=(10, 10), anchor="center")

        button_frame_ad = tk.Frame(row_submit_text_adm, bg="white")
        button_frame_ad.pack(fill="x", pady=(0, 20))

        def submit_message():
            message_from_donor = text_box.get("1.0", "end-1c")
            try:
                self.cursor.execute("""INSERT INTO donor_message (user_id, email, donor_message) VALUES (%s, %s, %s)""",
                                    (user_id[0], email, message_from_donor))
                self.db.commit()
                messagebox.showinfo("Success", "Message sent successfully!")
                admin_window.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Message failed: {err}")

        submit_button = ctk.CTkButton(button_frame_ad, text="Enter", width=75, height=15, fg_color="#2ECC71",
                                      hover_color="#27AE60", corner_radius=5, font=ctk.CTkFont(size=13, weight="bold"),
                                      command=submit_message)
        submit_button.pack(side="left", padx=10)

        back_button = ctk.CTkButton(button_frame_ad, text="Cancel", width=75, height=15, fg_color="#3498DB",
                                    hover_color="#2980B9", corner_radius=5, font=ctk.CTkFont(size=13, weight="bold"),
                                    command=lambda: admin_window.destroy())
        back_button.pack(side="left", padx=10)
