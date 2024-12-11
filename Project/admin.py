import tkinter as tk
from tkinter import messagebox, ttk
import customtkinter as ctk
import mysql.connector

class Admin:
    def __init__(self, root, db, cursor, main_front):
        self.root = root
        self.db = db
        self.cursor = cursor
        self.main = main_front

        #retrieving the number of requestor with
    def count_requests (self):
        self.cursor.execute("SELECT COUNT(*) FROM req_users WHERE status_req = 'Pending request'")
        result = self.cursor.fetchone()[0]
        return result

    def count_donors (self):
        self.cursor.execute("SELECT COUNT(*) FROM donor_users WHERE status = 'Pending'")
        result = self.cursor.fetchone()[0]
        return result
    def count_total_stocks (self):
        self.cursor.execute("SELECT COUNT(*) FROM donor_users WHERE status = 'Processed'")
        result = self.cursor.fetchone()[0]
        return result

    def count_total_messages(self):
        self.cursor.execute("SELECT COUNT(*) FROM requestor_message")
        req_count = self.cursor.fetchone()[0]
        self.cursor.execute("SELECT COUNT(*) FROM donor_message")
        donor_count = self.cursor.fetchone()[0]
        return req_count + donor_count


    def admin_login_frame(self):
        for widget in self.root.winfo_children():  # clear
            widget.destroy()

        self.root.geometry("1000x600")

        # Create main container
        main_container = tk.Frame(self.root)
        main_container.pack(fill="both", expand=True)

        # Left frame (light background)
        left_frame = tk.Frame(main_container, bg="#F5F5F5")
        left_frame.pack(side="left", fill="both", expand=True)

        # Right frame (dark background)
        right_frame = tk.Frame(main_container, bg="#2B2B3E")
        right_frame.pack(side="right", fill="both", expand=True)

        # Left frame content
        title_container = tk.Frame(left_frame, bg="#F5F5F5")
        title_container.place(relx=0.5, rely=0.4, anchor="center")

        system_name = tk.Label(title_container, text="BetaMax", font=("Helvetica", 15, "bold"), bg="#F5F5F5",
                               fg="#2B2B3E")

        system_name.pack()

        system_label = tk.Label(title_container, text="Login as Admin", font=("Helvetica", 25, "bold"), bg="#F5F5F5",
                                fg="#2B2B3E", justify="center")
        system_label.pack(pady=(10, 0))

        container = tk.Frame(right_frame, bg="#2B2B3E")
        container.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(container, text="Username or Email", bg="#2D2B3E", fg="white", font=("Helvetica", 16, "bold"),
                 padx=5).pack(pady=(10, 10), anchor="w")
        admin_user = ctk.CTkEntry(container, width=350, height=50, placeholder_text="Username or Email",
                                  font=("Helvetica", 16, "bold"), fg_color="white", text_color="black",
                                  corner_radius=15)
        admin_user.pack(pady=(0, 10), anchor="w")

        tk.Label(container, text="Password", bg="#2D2B3E", fg="white", font=("Helvetica", 16, "bold"), padx=5).pack(
            pady=(10, 10), anchor="w")
        admin_pass = ctk.CTkEntry(container, width=350, height=50, placeholder_text="Password",
                                  font=("Helvetica", 16, "bold"), fg_color="white", text_color="black", show="*",
                                  corner_radius=10)
        admin_pass.pack(pady=(0, 10), anchor="w")

        login_admin_button = ctk.CTkButton(container, text="Login Now", fg_color="#2ECC71", text_color="white",
                                           font=("Helvetica", 16, "bold"), width=200, height=50, corner_radius=15,
                                           hover_color="#27AE60",
                                           command=lambda: self.admin_login(admin_user.get(), admin_pass.get()))
        login_admin_button.pack(pady=20)

        hyperlink_frame = tk.Frame(container, bg="#2B2B3E")
        hyperlink_frame.pack(pady=(0, 10))

        not_admin_label = tk.Label(hyperlink_frame, text="Not an admin? ", bg="#2B2B3E", fg="white",
                                   font=("Helvetica", 12))
        not_admin_label.pack(side=tk.LEFT)

        back_to_menu_link = tk.Label(hyperlink_frame, text="Back to Menu!", bg="#2B2B3E", fg="#3498db",
                                     font=("Helvetica", 12, "bold"), cursor="hand2")
        back_to_menu_link.pack(side=tk.LEFT)

        # Bind click event to the hyperlink
        back_to_menu_link.bind("<Button-1>", lambda e: self.main.front_page())

    def admin_login(self, admin_user, admin_password):

        default_admin = "Admin"
        default_password = "missnakita"
        if not admin_user:
            messagebox.showerror("Error Message", "Username is required!")
            return False
        elif not admin_password:
            messagebox.showerror("Error Message", "Password is required!")
            return False
        try: #admin login
            self.cursor.execute("""SELECT * FROM admin WHERE (username = %s OR admin_email = %s) AND password = %s""",
                                (admin_user, admin_user, admin_password))
            user = self.cursor.fetchone()



            if user:
                messagebox.showinfo("Success", "Login successful!")
                self.admin_dashboard()
            elif admin_user == default_admin and admin_password == default_password: #an admin can use this but highly recommended to use the database record
                messagebox.showinfo("Success", "Login successfully using default Admin Account!")
                self.admin_dashboard()
            else:
                messagebox.showerror("Error", "Invalid username or password!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Login failed: {err}")

    def create_donor_treeview(parent_frame):
        # Style configuration
        style = ttk.Style()
        style.configure("Custom.Treeview", background="white", foreground="black", rowheight=25, fieldbackground="white")
        style.configure("Custom.Treeview.Heading", background="#2B2B3E", foreground="white", relief="flat")
        style.map("Custom.Treeview",
                  background=[("selected", "#2ECC71")],
                  foreground=[("selected", "white")])

        # Create Treeview
        columns = ("id", "first_name", "middle_initial", "last_name", "contact",
                   "age", "gender", "blood_group", "status", "address", "email", "date_issued")

        tree = ttk.Treeview(parent_frame, columns=columns, show="headings", style="Custom.Treeview")

        # Configure column headings
        tree.heading("id", text="ID")
        tree.heading("first_name", text="First Name")
        tree.heading("middle_initial", text="MI")
        tree.heading("last_name", text="Last Name")
        tree.heading("contact", text="Contact")
        tree.heading("age", text="Age")
        tree.heading("gender", text="Gender")
        tree.heading("blood_group", text="Blood Type")
        tree.heading("status", text="Status")
        tree.heading("address", text="Address")
        tree.heading("email", text="Email")
        tree.heading("date_issued", text="Date Issued")

        # Configure column widths
        tree.column("id", width=50)
        tree.column("first_name", width=120)
        tree.column("middle_initial", width=50)
        tree.column("last_name", width=120)
        tree.column("contact", width=120)
        tree.column("age", width=50)
        tree.column("gender", width=80)
        tree.column("blood_group", width=100)
        tree.column("status", width=100)
        tree.column("address", width=200)
        tree.column("email", width=180)
        tree.column("date_issued", width=120)

        # Add scrollbars
        vsb = ttk.Scrollbar(parent_frame, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(parent_frame, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        # Grid layout
        tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")

        # Configure grid weights
        parent_frame.grid_rowconfigure(0, weight=1)
        parent_frame.grid_columnconfigure(0, weight=1)

        return tree

    def refresh_treeview(self, tree):
        # Clear existing items
        for item in tree.get_children():
            tree.delete(item)

        # Fetch and insert new data
        self.cursor.execute(
            """SELECT id, last_name, first_name, middle_initial, contact, age, gender, blood_group, date_issued, status FROM donor_users ORDER BY 
               CASE status
               WHEN 'Pending' THEN 1
               WHEN 'Processed' THEN 2
               WHEN 'Done' THEN 3
               ELSE 4
               END, date_issued DESC""")
        for row in self.cursor.fetchall():
            tree.insert("", "end", values=row)





    def admin_dashboard(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.geometry("1200x700")
        self.root.configure(bg="#2B2B3E")

        # Create main frame
        main_frame = tk.Frame(self.root, bg="#2B2B3E")
        main_frame.pack(fill="both", expand=True)

        # Add title
        title_label = ctk.CTkLabel(main_frame, text="Admin Dashboard (Donor Section)", font=("Helvetica", 24, "bold"),
                                   text_color="white")
        title_label.pack(pady=(20, 30))

        # Create frame for buttons in the upper left
        button_frame = tk.Frame(main_frame, bg="#2B2B3E")
        button_frame.pack(pady=10)

        count_reqs = self.count_requests()

        # Create buttons for requests, donors, and stocks
        requests_btn = ctk.CTkButton(button_frame, text=f"Requests ({count_reqs})",
                                     command=lambda: self.show_requests(), width=120, height=35, fg_color="#2ECC71",
                                     hover_color="#27AE60")
        requests_btn.pack(side="left", padx=5)

        count_donor = self.count_donors()
        donors_btn = ctk.CTkButton(button_frame, text=f"Donors ({count_donor}) ",
                                   command=lambda: self.admin_dashboard(), width=120, height=35, fg_color="#3498DB",
                                   hover_color="#2980B9")
        donors_btn.pack(side="left", padx=5)

        count_stock = self.count_total_stocks()

        stocks_btn = ctk.CTkButton(button_frame, text=f"Stocks ({count_stock})", width=120, height=35, fg_color="#E74C3C",
                                   hover_color="#C0392B",
                                   command=lambda: self.show_stocks_frame_admin())

        stocks_btn.pack(side="left", padx=5)

        # Add separator
        separator = ttk.Separator(main_frame, orient="horizontal")
        separator.pack(fill="x", padx=20, pady=(10, 20))

        # Create frame for treeview
        tree_frame = tk.Frame(main_frame, bg="#2B2B3E")
        tree_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Create and populate treeview
        columns = (
        "id", "last_name", "first_name", "middle_initial", "contact", "age", "gender", "blood_group", "date_issued",
        "status")
        donor_tree = ttk.Treeview(tree_frame, columns=columns, show="headings")

        # Configure column headings
        for col in columns:
            donor_tree.heading(col, text=col.replace("_", " ").title())
            donor_tree.column(col, width=100)

        # Add scrollbars
        y_scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=donor_tree.yview)
        x_scrollbar = ttk.Scrollbar(tree_frame, orient="horizontal", command=donor_tree.xview)
        donor_tree.configure(yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)

        # Grid layout
        donor_tree.grid(row=0, column=0, sticky="nsew")
        y_scrollbar.grid(row=0, column=1, sticky="ns")
        x_scrollbar.grid(row=1, column=0, sticky="ew")

        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)

        # Populate treeview with data
        self.cursor.execute("""SELECT id, last_name, first_name, middle_initial, contact, age, gender, blood_group, date_issued, status FROM donor_users ORDER BY
        CASE status
        WHEN 'Pending' THEN 1
        WHEN 'Processed' THEN 2
        WHEN 'Done' THEN 3
        ELSE 4
        END, date_issued DESC""")

        for row in self.cursor.fetchall():
            donor_tree.insert("", "end", values=row)

        # Add refresh button
        bottom_button_frame = tk.Frame(main_frame, bg="#2B2B3E")
        bottom_button_frame.pack(pady=10)

        refresh_btn = ctk.CTkButton(bottom_button_frame, text="Refresh",
                                    command=lambda: self.refresh_treeview(donor_tree), width=200, height=40,
                                    fg_color="#28a745", hover_color="#218838")
        refresh_btn.pack(side="left", padx=5)

        # Add update process button
        update_btn = ctk.CTkButton(bottom_button_frame, text="Update Process", width=200, height=40,fg_color="#E67E22", hover_color="#D35400",
                                   command=lambda: self.update_process(donor_tree))
        update_btn.pack(side="left", padx=5)

        edit_btn = ctk.CTkButton(bottom_button_frame, text="Edit Details", width=200, height=40,
                                 fg_color="#9B59B6", hover_color="#8E44AD",
                                 command=lambda: self.edit_details(donor_tree))
        edit_btn.pack(side="left", padx=5)

        delete_btn = ctk.CTkButton(bottom_button_frame, text="Delete", width=200, height=40,
                                   fg_color="#E74C3C", hover_color="#C0392B",
                                   command=lambda: self.delete_donor(donor_tree))
        delete_btn.pack(side="left", padx=5)


        # Add back to menu button
        back_btn = ctk.CTkButton(bottom_button_frame, text="Log out", command=self.ask_before_logout, width=200,
                                 height=40, fg_color="#3498DB", hover_color="#2980B9")
        back_btn.pack(side="left", padx=5)

        total_messages = self.count_total_messages()
        messages_btn = ctk.CTkButton(button_frame, text=f"Messages({total_messages})", width=120, height=35, fg_color="#ff5722",
                                     hover_color="#e64a19", command=lambda: self.show_message_admin())
        messages_btn.pack(side="left", padx=5)




    def update_process(self, tree):
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a row to update.")
            return

        item = tree.item(selected_item[0])
        user_id = item['values'][0]
        current_status = item['values'][9]

        if current_status != "Pending":
            messagebox.showinfo("Info", "This record is not in Pending status.")
            return

        try:
            self.cursor.execute("UPDATE donor_users SET status = 'Processed' WHERE id = %s", (user_id,))
            self.db.commit()
            messagebox.showinfo("Success", "Status updated to Processed.")
            self.refresh_treeview(tree)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to update status: {err}")

    #req admin dashboard process
    def create_requestor_treeview(self, parent_frame):
        # Style configuration
        style = ttk.Style()
        style.configure("Custom.Treeview", background="white", foreground="black", rowheight=25,
                        fieldbackground="white")
        style.configure("Custom.Treeview.Heading", background="#2B2B3E", foreground="black", relief="flat")
        style.map("Custom.Treeview",
                  background=[("selected", "#2ECC71")],
                  foreground=[("selected", "white")])

        # Create Treeview with columns matching req_users table
        columns = ("requestorID", "first_name", "middle_initial", "last_name", "contact_number",
                   "age", "gender", "blood_needed", "urgency_level", "status_req")

        tree = ttk.Treeview(parent_frame, columns=columns, show="headings", style="Custom.Treeview")

        # Configure column headings
        tree.heading("requestorID", text="Requestor ID")
        tree.heading("first_name", text="First Name")
        tree.heading("middle_initial", text="MI")
        tree.heading("last_name", text="Last Name")
        tree.heading("contact_number", text="Contact")
        tree.heading("age", text="Age")
        tree.heading("gender", text="Gender")
        tree.heading("blood_needed", text="Blood Needed")
        tree.heading("urgency_level", text="Urgency Level")
        tree.heading("status_req", text="Status")

        # Configure column widths
        tree.column("requestorID", width=100)
        tree.column("first_name", width=120)
        tree.column("middle_initial", width=50)
        tree.column("last_name", width=120)
        tree.column("contact_number", width=120)
        tree.column("age", width=50)
        tree.column("gender", width=80)
        tree.column("blood_needed", width=100)
        tree.column("urgency_level", width=150)
        tree.column("status_req", width=120)

        # Add scrollbars
        vsb = ttk.Scrollbar(parent_frame, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(parent_frame, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        # Grid layout
        tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")

        # Configure grid weights
        parent_frame.grid_rowconfigure(0, weight=1)
        parent_frame.grid_columnconfigure(0, weight=1)

        return tree

    def refresh_requestor_treeview(self, tree):
        # Clear existing items
        for item in tree.get_children():
            tree.delete(item)

        # Fetch and insert new data
        self.cursor.execute(
            """
            SELECT requestorID, first_name, middle_initial, last_name, contact_number, 
                   age, gender, blood_needed, urgency_level, status_req FROM req_users ORDER BY CASE 
                   WHEN status_req = 'Pending request' THEN 0 
                   ELSE 1 
                   END, requestorID DESC"""
        )
        for row in self.cursor.fetchall():
            tree.insert("", "end", values=row)

    def show_requests(self):
        # Clear current window
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.geometry("1200x700")
        self.root.configure(bg="#2B2B3E")

        # Create main frame
        main_frame = tk.Frame(self.root, bg="#2B2B3E")
        main_frame.pack(fill="both", expand=True)

        # Add title
        title_label = ctk.CTkLabel(main_frame, text="Admin Dashboard (Requests Section)",
                                   font=("Helvetica", 24, "bold"), text_color="white")
        title_label.pack(pady=(20, 30))

        # Create frame for buttons
        button_frame = tk.Frame(main_frame, bg="#2B2B3E")
        button_frame.pack(pady=10)

        counts = self.count_requests()
        # Navigation buttons
        requests_btn = ctk.CTkButton(button_frame, text=f"Requests ({counts})", width=120, height=35, fg_color="#2ECC71",
                                     hover_color="#27AE60", command=lambda: self.show_requests())
        requests_btn.pack(side="left", padx=5)

        count_donors = self.count_donors()
        donors_btn = ctk.CTkButton(button_frame, text=f"Donors ({count_donors})", width=120, height=35, fg_color="#3498DB",
                                   hover_color="#2980B9", command=lambda: self.admin_dashboard())
        donors_btn.pack(side="left", padx=5)

        count_stocks = self.count_total_stocks()
        stocks_btn = ctk.CTkButton(button_frame, text=f"Stocks ({count_stocks})", width=120, height=35, fg_color="#E74C3C",
                                   hover_color="#C0392B", command=lambda: self.show_stocks_frame_admin())
        stocks_btn.pack(side="left", padx=5)

        total_messages = self.count_total_messages()
        messages_btn = ctk.CTkButton(button_frame, text= f"Messages({total_messages})", width=120, height=35, fg_color="#ff5722",
                                    hover_color="#e64a19", command=lambda: self.show_message_admin())
        messages_btn.pack(side="left", padx=5)

        # Add separator
        separator = ttk.Separator(main_frame, orient="horizontal")
        separator.pack(fill="x", padx=20, pady=(10, 20))

        # Create frame for treeview
        tree_frame = tk.Frame(main_frame, bg="#2B2B3E")
        tree_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Create and populate treeview
        requestor_tree = self.create_requestor_treeview(tree_frame)

        # Populate treeview with data
        self.refresh_requestor_treeview(requestor_tree)

        # Bottom buttons frame
        bottom_button_frame = tk.Frame(main_frame, bg="#2B2B3E")
        bottom_button_frame.pack(pady=10)

        # Refresh button
        refresh_btn = ctk.CTkButton(bottom_button_frame, text="Refresh",
                                    command=lambda: self.refresh_requestor_treeview(requestor_tree), width=200,
                                    height=40, fg_color="#2ECC71", hover_color="#27AE60")
        refresh_btn.pack(side="left", padx=5)

        # Process button
        process_btn = ctk.CTkButton(bottom_button_frame, text="Process Request",
                                    command=lambda: self.process_request(requestor_tree), width=200, height=40,
                                    fg_color="#E67E22", hover_color="#D35400")
        process_btn.pack(side="left", padx=5)

        edit_btn = ctk.CTkButton(bottom_button_frame, text="Edit Details", width=200, height=40,
                                 fg_color="#9B59B6", hover_color="#8E44AD",
                                 command=lambda: self.edit_requestor_details(requestor_tree))
        edit_btn.pack(side="left", padx=5)

        delete_btn = ctk.CTkButton(bottom_button_frame, text="Delete", width=200, height=40,
                                   fg_color="#E74C3C", hover_color="#C0392B",
                                   command=lambda: self.delete_requestor(requestor_tree))
        delete_btn.pack(side="left", padx=5)



        # Logout button
        logout_btn = ctk.CTkButton(bottom_button_frame, text="Log out", command=self.ask_before_logout, width=200,
                                   height=40, fg_color="#3498DB", hover_color="#2980B9")
        logout_btn.pack(side="left", padx=5)

    def process_request(self, tree):
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a row to process.")
            return

        item = tree.item(selected_item[0])
        requestor_id = item['values'][0]
        blood_needed = item['values'][7]  # Get blood type needed
        current_status = item['values'][9]

        if current_status != "Pending request":
            messagebox.showinfo("Info", "This request has already been processed.")
            return

        try:
            # Start a transaction
            self.cursor.execute("START TRANSACTION")

            # Update request status
            self.cursor.execute(
                "UPDATE req_users SET status_req = 'Processed/Ready' WHERE requestorID = %s",
                (requestor_id,)
            )

            # Update one matching donor's status to 'done'
            self.cursor.execute(
                """UPDATE donor_users SET status = 'Done' WHERE blood_group = %s AND status = 'Processed' ORDER BY id LIMIT 1""",
                (blood_needed,))
            # Check if a donor was updated
            if self.cursor.rowcount == 0:
                self.cursor.execute("ROLLBACK")
                messagebox.showerror("Error", f"No processed donor found with matching blood type {blood_needed}")
                return

            # Commit the transaction
            self.cursor.execute("COMMIT")
            messagebox.showinfo("Success", "Request has been processed successfully and donor status updated.")
            self.refresh_requestor_treeview(tree)

        except mysql.connector.Error as err:
            self.cursor.execute("ROLLBACK")
            messagebox.showerror("Error", f"Failed to process request: {err}")

    def show_stocks_frame_admin(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.stocks_frame = tk.Frame(self.root, bg="#2B2B3E")
        self.stocks_frame.pack(fill="both", expand=True)
        self.root.geometry("1200x700")

        # Title
        title_label = ctk.CTkLabel(self.stocks_frame, text="BetaMax ", font=("Helvetica", 24, "bold"))
        title_label.pack(pady=(20, 10), padx=20, anchor="w")

        subtitle_label = ctk.CTkLabel(self.stocks_frame, text="Admin Dashboard (Stocks)", font=("Helvetica", 25, "bold"))
        subtitle_label.pack(pady=(10, 30))

        # Create a frame for the blood type cards
        self.cards_frame = ctk.CTkFrame(self.stocks_frame, fg_color="transparent")
        self.cards_frame.pack(pady=20)

        # Initialize blood type data
        blood_types = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

        try:
            # Establish database connection
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="blood_donation_db"
            )
            cursor = conn.cursor()

            # Fetch processed counts for each blood type
            self.blood_stock = {}
            for blood_type in blood_types:
                cursor.execute(
                    """SELECT COUNT(*) FROM donor_users WHERE blood_group = %s AND status = 'Processed';""",
                    (blood_type,)
                )
                self.blood_stock[blood_type] = cursor.fetchone()[0]

            # Generate cards for blood types
            for i, blood_type in enumerate(blood_types):
                count = self.blood_stock.get(blood_type, 0)
                card = ctk.CTkFrame(self.cards_frame, width=250, height=150, corner_radius=10, fg_color="white")
                card.grid(row=i // 4, column=i % 4, padx=10, pady=10)

                blood_type_label = ctk.CTkLabel(card, text=blood_type, font=("Helvetica", 36, "bold"), text_color="#2B2B3E")
                blood_type_label.place(relx=0.5, rely=0.3, anchor="center")

                amount_label = ctk.CTkLabel(card, text=str(count), font=("Helvetica", 36, "bold"), text_color="#2B2B3E")
                amount_label.place(relx=0.5, rely=0.7, anchor="center")

        except mysql.connector.Error as err:
            print(f"Something went wrong: {err}")

        # Back to menu button
        back_button_stocks = ctk.CTkButton(self.stocks_frame, text="Back to Admin Dashboard",
                                           command=lambda: self.admin_dashboard() , width=250, height=40, fg_color="#3498DB", hover_color="#2980B9", font=("Helvetica", 16, "bold"))
        back_button_stocks.pack(pady=30)

    def show_message_admin(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.geometry("1200x700")
        self.root.configure(bg="#2B2B3E")

        # Create main frame
        main_frame = tk.Frame(self.root, bg="#2B2B3E")
        main_frame.pack(fill="both", expand=True)

        # Add title
        title_label = ctk.CTkLabel(main_frame, text="Admin Dashboard (Messages)",
                                   font=("Helvetica", 24, "bold"),
                                   text_color="white")
        title_label.pack(pady=(20, 30))

        # Navigation buttons frame
        button_frame = tk.Frame(main_frame, bg="#2B2B3E")
        button_frame.pack(pady=10)

        # Add navigation buttons
        counts = self.count_requests()
        requests_btn = ctk.CTkButton(button_frame, text=f"Requests ({counts})",
                                     width=120, height=35, fg_color="#2ECC71",
                                     hover_color="#27AE60",
                                     command=lambda: self.show_requests())
        requests_btn.pack(side="left", padx=5)

        count_donors = self.count_donors()
        donors_btn = ctk.CTkButton(button_frame, text=f"Donors ({count_donors})",
                                   width=120, height=35, fg_color="#3498DB",
                                   hover_color="#2980B9",
                                   command=lambda: self.admin_dashboard())
        donors_btn.pack(side="left", padx=5)

        count_stocks = self.count_total_stocks()
        stocks_btn = ctk.CTkButton(button_frame, text=f"Stocks ({count_stocks})",
                                   width=120, height=35, fg_color="#E74C3C",
                                   hover_color="#C0392B",
                                   command=lambda: self.show_stocks_frame_admin())
        stocks_btn.pack(side="left", padx=5)

        total_messages = self.count_total_messages()
        messages_btn = ctk.CTkButton(button_frame, text=f"Messages({total_messages})",
                                     width=120, height=35, fg_color="#ff5722",
                                     hover_color="#e64a19",
                                     command=lambda: self.show_message_admin())
        messages_btn.pack(side="left", padx=5)

        # Create two-column layout
        columns_frame = tk.Frame(main_frame, bg="#2B2B3E")
        columns_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Left column for donor messages
        donor_frame = tk.Frame(columns_frame, bg="#2B2B3E")
        donor_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

        # Right column for requestor messages
        requestor_frame = tk.Frame(columns_frame, bg="#2B2B3E")
        requestor_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))

        # Donor messages section
        donor_label = ctk.CTkLabel(donor_frame, text="Donor Messages",
                                   font=("Helvetica", 20, "bold"),
                                   text_color="white")
        donor_label.pack(pady=(0, 20))

        donor_messages_frame = ctk.CTkScrollableFrame(donor_frame, fg_color="transparent")
        donor_messages_frame.pack(fill="both", expand=True)

        # Fetch and display donor messages
        self.cursor.execute("""
            SELECT donorMessID, email, donor_message, user_id, mess_date
            FROM donor_message 
            ORDER BY donorMessID DESC
        """)
        donor_messages = self.cursor.fetchall()

        for msg in donor_messages:
            self.create_message_card(donor_messages_frame, msg, "Donor")

        # Requestor messages section
        requestor_label = ctk.CTkLabel(requestor_frame, text="Requestor Messages",
                                       font=("Helvetica", 20, "bold"),
                                       text_color="white")
        requestor_label.pack(pady=(0, 20))

        requestor_messages_frame = ctk.CTkScrollableFrame(requestor_frame, fg_color="transparent")
        requestor_messages_frame.pack(fill="both", expand=True)

        # Fetch and display requestor messages
        self.cursor.execute("""
            SELECT messageID, email, req_message, requestorID, mess_date
            FROM requestor_message 
            ORDER BY messageID DESC
        """)
        requestor_messages = self.cursor.fetchall()

        for msg in requestor_messages:
            self.create_message_card(requestor_messages_frame, msg, "Requestor")

        # Bottom buttons frame
        bottom_frame = tk.Frame(main_frame, bg="#2B2B3E")
        bottom_frame.pack(pady=20)

        # Add refresh button
        refresh_btn = ctk.CTkButton(bottom_frame, text="Refresh",
                                    command=lambda: self.show_message_admin(),
                                    width=200, height=40,
                                    fg_color="#2ECC71",
                                    hover_color="#27AE60")
        refresh_btn.pack(side="left", padx=5)

        # Add back button
        back_btn = ctk.CTkButton(bottom_frame, text="Back to Dashboard",
                                 command=lambda: self.admin_dashboard(),
                                 width=200, height=40,
                                 fg_color="#3498DB",
                                 hover_color="#2980B9")
        back_btn.pack(side="left", padx=5)

    def create_message_card(self, parent_frame, msg, msg_type):
        # Create message card
        card = ctk.CTkFrame(parent_frame, fg_color="white", corner_radius=10)
        card.pack(fill="x", pady=5, padx=5)

        # Message header
        header_frame = ctk.CTkFrame(card, fg_color="transparent")
        header_frame.pack(fill="x", padx=15, pady=(10, 5))

        # Update the ID text based on message type
        msg_id_text = "Donor ID: " if msg_type == "Donor" else "Requestor ID: "
        msg_id = ctk.CTkLabel(header_frame, text=f"{msg_id_text}{msg[3]}",
                              font=("Helvetica", 12),
                              text_color="#666")
        msg_id.pack(side="left")

        # Add date
        date_label = ctk.CTkLabel(header_frame, text=f"Date: {msg[4]}",
                                  font=("Helvetica", 12),
                                  text_color="#666")
        date_label.pack(side="left", padx=10)

        email = ctk.CTkLabel(header_frame, text=f"From: {msg[1]}",
                             font=("Helvetica", 12, "bold"),
                             text_color="#2B2B3E")
        email.pack(side="right")

        # Message content
        message = ctk.CTkLabel(card, text=msg[2],
                               font=("Helvetica", 14),
                               text_color="#2B2B3E",
                               wraplength=400,
                               justify="left")
        message.pack(fill="x", padx=15, pady=(5, 15))

    def edit_details(self, tree):
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a row to edit.")
            return

        item = tree.item(selected_item[0])
        user_id = item['values'][0]

        # Create a new window for editing
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Donor Details")
        edit_window.geometry("450x550")
        edit_window.configure(bg="#2B2B3E")
        edit_window.resizable(False, False)

        # Fetch user details
        self.cursor.execute("SELECT * FROM donor_users WHERE id = %s", (user_id,))
        user = self.cursor.fetchone()

        if not user:
            messagebox.showerror("Error", "User not found.")
            edit_window.destroy()
            return

        # Create a frame for the content
        content_frame = tk.Frame(edit_window, bg="#2B2B3E", padx=20, pady=20)
        content_frame.pack(fill="both", expand=True)

        # Create input fields
        fields = ['First Name', 'Middle Initial', 'Last Name', 'Contact', 'Age', 'Gender', 'Blood Group', 'Status', 'Address', 'Email']
        entries = {}

        for i, field in enumerate(fields):
            tk.Label(content_frame, text=field, bg="#2B2B3E", fg="white", font=("Helvetica", 12)).grid(row=i, column=0, padx=10, pady=5, sticky="w")
            entry = ctk.CTkEntry(content_frame, width=250, height=35, fg_color="white", text_color="black", corner_radius=5)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="ew")
            entry.insert(0, str(user[i+1]))  # +1 because id is at index 0
            entries[field] = entry

        # Button frame
        button_frame = tk.Frame(content_frame, bg="#2B2B3E")
        button_frame.grid(row=len(fields), column=0, columnspan=2, pady=20)

        # Save button
        save_btn = ctk.CTkButton(button_frame, text="Save",
                                 command=lambda: self.save_details(user_id, entries, edit_window, tree),
                                 width=190, height=40,
                                 fg_color="#2ECC71", hover_color="#27AE60",
                                 text_color="white", font=("Helvetica", 14, "bold"))
        save_btn.pack(side="left", padx=10)

        # Cancel button
        cancel_btn = ctk.CTkButton(button_frame, text="Cancel",
                                   command=edit_window.destroy,
                                   width=200, height=40,
                                   fg_color="#3498DB", hover_color="#2980B9",
                                   text_color="white", font=("Helvetica", 14, "bold"))
        cancel_btn.pack(side="left", padx=10)

        # Configure grid
        content_frame.grid_columnconfigure(1, weight=1)


        #donor save details
    def save_details(self, user_id, entries, edit_window, tree):
        # Prepare update query
        update_query = """
        UPDATE donor_users 
        SET first_name=%s, middle_initial=%s, last_name=%s, contact=%s, 
            age=%s, gender=%s, blood_group=%s, status=%s, address=%s, email=%s 
        WHERE id=%s
        """
        values = [entries[field].get() for field in entries] + [user_id]

        try:
            self.cursor.execute(update_query, values)
            self.db.commit()
            messagebox.showinfo("Success", "Details updated successfully.")
            edit_window.destroy()
            self.refresh_treeview(tree)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to update details: {err}")

    def edit_requestor_details(self, tree):
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a row to edit.")
            return

        item = tree.item(selected_item[0])
        requestor_id = item['values'][0]

        # Create a new window for editing
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Requestor Details")
        edit_window.geometry("450x600")
        edit_window.configure(bg="#2B2B3E")
        edit_window.resizable(False, False)

        # Fetch requestor details
        self.cursor.execute("SELECT * FROM req_users WHERE requestorID = %s", (requestor_id,))
        requestor = self.cursor.fetchone()

        if not requestor:
            messagebox.showerror("Error", "Requestor not found.")
            edit_window.destroy()
            return

        # Create a frame for the content
        content_frame = tk.Frame(edit_window, bg="#2B2B3E", padx=20, pady=20)
        content_frame.pack(fill="both", expand=True)

        # Create input fields
        fields = ['First Name', 'Middle Initial', 'Last Name', 'Contact Number', 'Age', 'Gender', 'Blood Needed', 'Urgency Level', 'Status', 'Address', 'Email']
        entries = {}

        for i, field in enumerate(fields):
            tk.Label(content_frame, text=field, bg="#2B2B3E", fg="white", font=("Helvetica", 12)).grid(row=i, column=0, padx=10, pady=5, sticky="w")
            entry = ctk.CTkEntry(content_frame, width=250, height=35, fg_color="white", text_color="black", corner_radius=5)
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="ew")
            entry.insert(0, str(requestor[i+1]))  # +1 because requestorID is at index 0
            entries[field] = entry

        # Button frame
        button_frame = tk.Frame(content_frame, bg="#2B2B3E")
        button_frame.grid(row=len(fields), column=0, columnspan=2, pady=20)

        # Save button
        save_btn = ctk.CTkButton(button_frame, text="Save",
                                 command=lambda: self.save_requestor_details(requestor_id, entries, edit_window, tree),
                                 width=190, height=40,
                                 fg_color="#2ECC71", hover_color="#27AE60",
                                 text_color="white", font=("Helvetica", 14, "bold"))
        save_btn.pack(side="left", padx=10)

        # Cancel button
        cancel_btn = ctk.CTkButton(button_frame, text="Cancel",
                                   command=edit_window.destroy,
                                   width=200, height=40,
                                   fg_color="#3498DB", hover_color="#2980B9",
                                   text_color="white", font=("Helvetica", 14, "bold"))
        cancel_btn.pack(side="left", padx=10)

        # Configure grid
        content_frame.grid_columnconfigure(1, weight=1)

    def save_requestor_details(self, requestor_id, entries, edit_window, tree):
        # Prepare update query
        update_query = """
           UPDATE req_users 
           SET first_name=%s, middle_initial=%s, last_name=%s, contact_number=%s, 
               age=%s, gender=%s, blood_needed=%s, urgency_level=%s, status_req=%s, address=%s, email=%s 
           WHERE requestorID=%s
           """
        values = [entries[field].get() for field in entries] + [requestor_id]

        try:
            self.cursor.execute(update_query, values)
            self.db.commit()
            messagebox.showinfo("Success", "Requestor details updated successfully.")
            edit_window.destroy()
            self.refresh_requestor_treeview(tree)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to update requestor details: {err}")

    def delete_donor(self, tree):
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a row to delete.")
            return

        item = tree.item(selected_item[0])
        user_id = item['values'][0]

        # Confirmation dialog
        if messagebox.askyesno("Confirmation", "Are you sure you want to delete this donor?"):
            try:
                self.cursor.execute("DELETE FROM donor_users WHERE id = %s", (user_id,))
                self.db.commit()
                messagebox.showinfo("Success", "Donor deleted successfully.")
                self.refresh_treeview(tree)
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Failed to delete donor: {err}")

    def delete_requestor(self, tree):
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a row to delete.")
            return

        item = tree.item(selected_item[0])
        requestor_id = item['values'][0]

        # Confirmation dialog
        if messagebox.askyesno("Confirmation", "Are you sure you want to delete this requestor?"):
            try:
                self.cursor.execute("DELETE FROM req_users WHERE requestorID = %s", (requestor_id,))
                self.db.commit()
                messagebox.showinfo("Success", "Requestor deleted successfully.")
                self.refresh_requestor_treeview(tree)
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Failed to delete requestor: {err}")




    def ask_before_logout(self):
        ask = messagebox.askyesno("Confirmation", "Are you sure to log out?")
        if ask:
            self.main.front_page()
        else:
            return False

