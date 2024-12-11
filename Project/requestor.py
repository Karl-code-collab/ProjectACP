import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import mysql.connector
import re
class Requestor:
    def __init__(self, root, db, cursor, main_front):
        self.root = root
        self.db = db
        self.cursor = cursor
        self.main = main_front

    def show_login_req_frame(self):
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

        system_label = tk.Label(title_container, text="Login as Requestor", font=("Helvetica", 25, "bold"), bg="#F5F5F5", fg="#2B2B3E", justify="center")
        system_label.pack(pady=(10, 0))

        container = tk.Frame(right_frame, bg="#2B2B3E")
        container.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(container, text="Registered email", bg="#2D2B3E", fg="white", font=("Helvetica", 16, "bold"), padx=5).pack(pady=(10, 10), anchor="w")
        req_email = ctk.CTkEntry(container, width=350, height=50, placeholder_text="Registered Email", font=("Helvetica", 16, "bold"), fg_color="white", text_color="black", corner_radius=15)
        req_email.pack(pady=(0, 10), anchor="w")

        tk.Label(container, text="Password", bg="#2D2B3E", fg="white", font=("Helvetica", 16, "bold"), padx=5).pack(pady=(10, 10), anchor="w")
        req_pass = ctk.CTkEntry(container, width=350, height=50, placeholder_text="Password", font=("Helvetica", 16, "bold"), fg_color="white", text_color="black", show="*", corner_radius=10)
        req_pass.pack(pady=(0, 10), anchor="w")

        login_admin_button = ctk.CTkButton(container, text="Login Now", fg_color="#2ECC71", text_color="white", font=("Helvetica", 16, "bold"), width=200, height=50, corner_radius=15, hover_color="#27AE60", command=lambda: self.req_login(req_email.get().strip(), req_pass.get()))
        login_admin_button.pack(pady=20)

        hyperlink_frame = tk.Frame(container, bg="#2B2B3E")
        hyperlink_frame.pack(pady=(0, 10))

        reg_donor_label = tk.Label(hyperlink_frame, text="Don't have an Account? ", bg="#2B2B3E", fg="white", font=("Helvetica", 12))
        reg_donor_label.pack(side=tk.LEFT)

        back_to_menu_link = tk.Label(hyperlink_frame, text="Register Now!", bg="#2B2B3E", fg="#50C878", font=("Helvetica", 12, "bold"), cursor="hand2")
        back_to_menu_link.pack(side=tk.LEFT)

        back_to_menu_link.bind("<Button-1>", lambda e: self.show_req_register_frame())

    def req_login(self, req_email, req_pass):
        if not req_email:
            messagebox.showerror("Error Message", "Email is required!")
            return False
        elif not req_pass:
            messagebox.showerror("Error Message", "Password is required!")
            return False

        try:
            self.cursor.execute("""SELECT * FROM req_users WHERE email = %s AND password = %s""", (req_email, req_pass))
            user = self.cursor.fetchone()

            if user:
                messagebox.showinfo("Success", "Login successful!")
                self.req_user_dashboard(req_email, req_pass)
            else:
                messagebox.showerror("Error", "Invalid username or password!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Login failed: {err}")

    def show_req_register_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Recreate and configure register frame
        self.register_frame = tk.Frame(self.root, bg="#2B2B3E")
        self.register_frame.pack(fill="both", expand=True)
        self.root.geometry("800x800")
        self.root.configure(bg="#2B2B3E")

        # Register Title
        title_label_req = tk.Label(self.register_frame, text="Register as Requestor", font=("Helvetica", 30, "bold"),
                                   bg="#2B2B3E", fg="white")
        title_label_req.pack(pady=30)

        # Form container
        form_frame_req = tk.Frame(self.register_frame, bg="#2B2B3E")
        form_frame_req.pack(padx=50)

        # styles
        label_all = {"bg": "#2B2B3E", "fg": "white", "font": ("Helvetica", 12)}
        entry_sty = {"width": 225, "height": 35, "fg_color": "white", "text_color": "black", "corner_radius": 5}

        row_fill_req = tk.Frame(form_frame_req, bg="#2B2B3E")
        row_fill_req.pack(fill="x", pady=5)

        tk.Label(row_fill_req, text="Enter the following: ", bg="#2B2B3E", fg="#2ECC71", font="Helvetica 13 bold").grid(
            row=0, column=0, sticky="w", padx=(0, 25), pady=(0, 5))

        # full name of requestor
        row_name_req = tk.Frame(form_frame_req, bg="#2B2B3E")
        row_name_req.pack(fill="x", pady=3)

        tk.Label(row_name_req, text="Full Name", **label_all).grid(row=0, column=0, sticky="w", padx=(0, 60))
        lastname_req = ctk.CTkEntry(row_name_req, placeholder_text="Enter your last name", **entry_sty)
        lastname_req.grid(row=0, column=1, padx=10, pady=10)

        firstname_req = ctk.CTkEntry(row_name_req, placeholder_text="Enter your first name", **entry_sty)
        firstname_req.grid(row=0, column=3, padx=10, pady=10)

        middle_i_req = ctk.CTkEntry(row_name_req, placeholder_text="MI", width=50, height=35, fg_color="white",
                                    text_color="black", corner_radius=5)
        middle_i_req.grid(row=0, column=4, padx=10, pady=10)

        # req contacts
        row_contact_req = tk.Frame(form_frame_req, bg="#2B2B3E")
        row_contact_req.pack(fill="x", pady=5)

        tk.Label(row_contact_req, text="Contact Number", **label_all).grid(row=0, column=0, sticky="w", padx=(0, 25))
        contactnumber_req = ctk.CTkEntry(row_contact_req, placeholder_text="Enter your contact number", width=540,
                                         height=35, fg_color="white", text_color="black", corner_radius=5)
        contactnumber_req.grid(row=0, column=1)

        # requestor age
        row_age_req = tk.Frame(form_frame_req, bg="#2B2B3E")
        row_age_req.pack(fill="x", pady=5)

        tk.Label(row_age_req, text="Age", **label_all).grid(row=0, column=0, sticky="w", padx=(0, 110))
        age_req = ctk.CTkEntry(row_age_req, placeholder_text="Enter your age", width=540, height=35, fg_color="white",
                               text_color="black", corner_radius=5)
        age_req.grid(row=0, column=1)

        # req gender
        row_gender_req = tk.Frame(form_frame_req, bg="#2B2B3E")
        row_gender_req.pack(fill="x", pady=5)

        tk.Label(row_gender_req, text="Gender", **label_all).grid(row=0, column=0, sticky="w", padx=(0, 77))
        gender_req = ctk.CTkOptionMenu(row_gender_req, values=["Male", "Female", "Other"], width=540, height=35,
                                       fg_color="#2471A3", button_color="#2471A3")
        gender_req.grid(row=0, column=1, padx=10)

        # req blood and urgency level
        row_blood_urgency_req = tk.Frame(form_frame_req, bg="#2B2B3E")
        row_blood_urgency_req.pack(fill="x", pady=5)

        tk.Label(row_blood_urgency_req, text="Blood Needed &\nUrgency Level", **label_all).grid(row=0, column=0,sticky="w",padx=(0, 10))
        bloodtype_req = ctk.CTkOptionMenu(row_blood_urgency_req, values=["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"],
                                          width=260, height=35, fg_color="#2471A3", button_color="#2471A3")
        bloodtype_req.grid(row=0, column=1, padx=10)

        bloodurgency_req = ctk.CTkOptionMenu(row_blood_urgency_req, values=["Critical/Emergency", "Urgent", "Moderate", "Low Priority"],
                                          width=260, height=35, fg_color="#2471A3", button_color="#2471A3")
        bloodurgency_req.grid(row=0, column=2, padx=10)

        # full address
        row_address_req = tk.Frame(form_frame_req, bg="#2B2B3E")
        row_address_req.pack(fill="x", pady=5)

        tk.Label(row_address_req, text="Full Address", **label_all).grid(row=0, column=0, sticky="w", padx=(0, 40))
        address_req = ctk.CTkEntry(row_address_req, placeholder_text="Enter your full address", width=540, height=35,
                                   fg_color="white", text_color="black", corner_radius=5)
        address_req.grid(row=0, column=1, padx=10)

        # create req label
        row_label_req = tk.Frame(form_frame_req, bg="#2B2B3E")
        row_label_req.pack(fill="x", pady=5)

        tk.Label(row_label_req, text="Create your account", bg="#2B2B3E", fg="#2ECC71", font="Helvetica 13 bold").grid(row=0, column=0, sticky="w", padx=(0, 25), pady=(25, 5))

        # email requestor
        row_email_req = tk.Frame(form_frame_req, bg="#2B2B3E")
        row_email_req.pack(fill="x", pady=5)

        tk.Label(row_email_req, text="Email Address", **label_all).grid(row=0, column=0, sticky="w", padx=(0, 30))
        email_req = ctk.CTkEntry(row_email_req, placeholder_text="Enter your email address", width=540, height=35,
                                 fg_color="white", text_color="black", corner_radius=5)
        email_req.grid(row=0, column=1, padx=10, pady=10)

        # create pass req

        row_create_req = tk.Frame(form_frame_req, bg="#2B2B3E")
        row_create_req.pack(fill="x", pady=5)

        tk.Label(row_create_req, text="Create Password", **label_all).grid(row=0, column=0, sticky="w", padx=(0, 14))
        create_pass_req = ctk.CTkEntry(row_create_req, placeholder_text="Enter your password", show="•", width=540,
                                       height=35, fg_color="white", text_color="black", corner_radius=5)
        create_pass_req.grid(row=0, column=1, padx=10)

        # confirm pass req
        row_confirm_req = tk.Frame(form_frame_req, bg="#2B2B3E")
        row_confirm_req.pack(fill="x", pady=5)

        tk.Label(row_confirm_req, text="Confirm Password", **label_all).grid(row=0, column=0, sticky="w", padx=(0, 8))
        confirm_req = ctk.CTkEntry(row_confirm_req, placeholder_text="Confirm your password", show="•", width=540,
                                   height=35, fg_color="white", text_color="black", corner_radius=5)
        confirm_req.grid(row=0, column=1, padx=10)

        # submit and back button req
        row_submit_req = tk.Frame(form_frame_req, bg="#2B2B3E")
        row_submit_req.pack(fill="x", pady=5)

        submit_btn_req = ctk.CTkButton(row_submit_req, text="Submit", width=250, height=40, fg_color="#2ECC71", hover_color="#27AE60", corner_radius=5, font=ctk.CTkFont(size=16, weight="bold"),
                                       command=lambda: self.reg_requestor(firstname_req.get(), middle_i_req.get(),lastname_req.get(), contactnumber_req.get(),age_req.get(), gender_req.get(),bloodtype_req.get(), bloodurgency_req.get(),address_req.get(), email_req.get(),create_pass_req.get(), confirm_req.get()))
        submit_btn_req.grid(row=0, column=1, padx=(100, 20), pady=10)

        back_btn_req = ctk.CTkButton(row_submit_req, text="Back to Menu", width=250, height=40, fg_color="#3498DB",
                                     hover_color="#2980B9", corner_radius=5, font=ctk.CTkFont(size=16, weight="bold", ),
                                     command=lambda: self.main.front_page())
        back_btn_req.grid(row=0, column=2, padx=(0, 20), pady=10)

    def reg_requestor(self, firstname, mi, lastname, contact, age, gender, blood_needed, urgency_level, address, email, password, confirm_password):
        if not firstname or not mi or not lastname or not contact or not age or not gender or not blood_needed or not urgency_level or not address or not email or not password or not confirm_password:
            messagebox.showerror("Error", "All fields are required")

        if not self.email_validation(email):
            messagebox.showerror("Error", "Invalid email address")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")



        try:
            self.cursor.execute("""INSERT INTO req_users (first_name, middle_initial, last_name, contact_number, age, gender, blood_needed, urgency_level, status_req, address, email, password) 
                                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s)""",
                                (firstname, mi, lastname, contact, age, gender, blood_needed, urgency_level, "Pending request", address, email, password))

            self.db.commit()
            messagebox.showinfo("Success", "Registration successful!")
            self.show_login_req_frame()

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Registration failed: {err}")

    def email_validation(self, email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        if re.match(email_regex, email):
            return True
        return False


    def req_user_dashboard(self, email, req_pass):
        for widget in self.root.winfo_children():  # clear
            widget.destroy()

        self.req_dashboard_frame = tk.Frame(self.root, bg="white")
        self.req_dashboard_frame.pack(fill="both", expand=True)
        self.root.geometry("1200x700")
        self.root.configure(bg="white")

        self.cursor.execute(
            "SELECT first_name, last_name, middle_initial, blood_needed, urgency_level, status_req FROM req_users WHERE email = %s AND password = %s",
            (email, req_pass))
        result = self.cursor.fetchone()

        if result:
            first_name, last_name, middle_initial, blood_needed, urgency_level, status_req = result
            full_name_greet = f"{last_name.upper()}, {first_name.upper()} {middle_initial.upper()}."
            blood_label = blood_needed
            urgency_label = urgency_level
            status_label = status_req

            if status_label == "Processed/Ready":
                label_all = {"bg": "white", "fg": "#2ECC71", "font": ("Helvetica", 15, "bold")}
                announce_label = "Please proceed to the Clinic. Thank you!"
            else:
                status_label = "Pending Request"
                label_all = {"bg": "white", "fg": "#2B2B3E", "font": ("Helvetica", 15)}
                announce_label = "Please wait for further updates. Thank you!"
            system_name_label = tk.Label(self.req_dashboard_frame, text="BetaMax", font=("Helvetica", 18, "bold"),
                                         bg="white")
            system_name_label.pack(pady=(20, 10), padx=20, anchor="w")

            overview_label = tk.Label(self.req_dashboard_frame, text="Overview", font=("Helvetica", 20, "bold"),
                                      bg="white")
            overview_label.pack(pady=(30, 20), anchor="center")

            info_frame = tk.Frame(self.req_dashboard_frame, bg="white")
            info_frame.pack(pady=(10, 30), anchor="center")

            tk.Label(info_frame, text="Name:", font=("Helvetica", 15, "bold"), bg="white").grid(row=0, column=0,padx=(10, 5), pady=5,sticky="e")
            tk.Label(info_frame, text=full_name_greet, font=("Helvetica", 15), bg="white").grid(row=0, column=1,padx=(5, 10), pady=5,sticky="w")

            tk.Label(info_frame, text="Type of Application:", font=("Helvetica", 15, "bold"), bg="white").grid(row=1,column=0,padx=(10, 5),pady=5,sticky="e")
            tk.Label(info_frame, text=f"REQUEST FOR BLOOD ({blood_label})", font=("Helvetica", 15), bg="white").grid(row=1, column=1, padx=(5, 10), pady=5, sticky="w")

            tk.Label(info_frame, text="Urgency Level:", font=("Helvetica", 15, "bold"), bg="white").grid(row=2,column=0,padx=(10, 5),pady=5,sticky="e")
            tk.Label(info_frame, text=urgency_label, font=("Helvetica", 15), bg="white").grid(row=2, column=1,padx=(5, 10), pady=5,sticky="w")

            tk.Label(info_frame, text="Status:", font=("Helvetica", 15, "bold"), bg="white").grid(row=3, column=0,padx=(10, 5), pady=5,sticky="e")
            tk.Label(info_frame, text=status_label, **label_all).grid(row=3, column=1, padx=(5, 10), pady=5, sticky="w")

            tk.Label(self.req_dashboard_frame, text=announce_label, font=("Helvetica", 18, "bold"), bg="white").pack(
                pady=(30, 70), anchor="center")

            row_submit_text = tk.Frame(self.req_dashboard_frame, bg="white")
            row_submit_text.pack(pady=(10, 10), anchor="center")

            button_frame = tk.Frame(row_submit_text, bg="white")
            button_frame.pack(fill="x", pady=(0, 20))

            submit_button = ctk.CTkButton(button_frame, text="Message Admin", width=250, height=50, fg_color="#2ECC71", hover_color="#27AE60", corner_radius=5, font=ctk.CTkFont(size=16, weight="bold"),
                                          command=lambda: self.message_admin(email))
            submit_button.pack(side="left", padx=10)

            back_button = ctk.CTkButton(button_frame, text="Back to Menu", width=250, height=50, fg_color="#3498DB", hover_color="#2980B9", corner_radius=5, font=ctk.CTkFont(size=16, weight="bold"),
                                        command=lambda: self.main.front_page())
            back_button.pack(side="left", padx=10)

        else:
            label = tk.Label(self.req_dashboard_frame, text="User not found", font=("Arial", 24), fg="white",
                             bg="#2B2B3E")
            label.pack(pady=20, side="top", anchor="w")

    def message_admin(self, email):
        admin_window = tk.Toplevel(self.root)
        admin_window.title("Message to Admin")
        admin_window.geometry("500x250")
        admin_window.configure(bg="white")
        admin_window.resizable(False, False)

        # Retrieve the user ID based on the email address
        self.cursor.execute("SELECT requestorID FROM req_users WHERE email = %s", (email,))
        requestorID = self.cursor.fetchone()
        if not requestorID:
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
                self.cursor.execute("""INSERT INTO requestor_message (requestorID, email, req_message) VALUES (%s, %s, %s)""",
                                    (requestorID[0], email, message_from_donor))
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