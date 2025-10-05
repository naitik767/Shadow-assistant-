import json
import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class TaskManagerApp:
    def __init__(self, root, file='tasks_gui.json'):
        self.root = root
        self.root.title("📝 Shadow Task Manager")
        self.file = file
        self.tasks = []
        self.load_tasks()
    
        # Style
        self.frame = ttk.Frame(root, padding=10)
        self.frame.pack(fill=BOTH, expand=YES)

        # Entry widgets
        ttk.Label(self.frame, text="Description:").grid(row=0, column=0, sticky=W)
        self.desc_entry = ttk.Entry(self.frame, width=40)
        self.desc_entry.grid(row=0, column=1, padx=5)

        ttk.Label(self.frame, text="Category:").grid(row=1, column=0, sticky=W)
        self.cat_entry = ttk.Entry(self.frame, width=40)
        self.cat_entry.grid(row=1, column=1, padx=5)

        # Buttons
        ttk.Button(self.frame, text="➕ Add Task", bootstyle=SUCCESS, command=self.add_task).grid(row=2, column=0, columnspan=2, pady=10)

        # Task list
        self.task_list = ttk.Treeview(self.frame, columns=("desc", "cat", "status"), show='headings', height=10)
        self.task_list.heading("desc", text="Description")
        self.task_list.heading("cat", text="Category")
        self.task_list.heading("status", text="Status")
        self.task_list.column("desc", width=200)
        self.task_list.column("cat", width=100)
        self.task_list.column("status", width=80)
        self.task_list.grid(row=3, column=0, columnspan=2, pady=10)

        # Action buttons
        ttk.Button(self.frame, text="✅ Mark Done", bootstyle=PRIMARY, command=self.mark_done).grid(row=4, column=1, pady=5)
        ttk.Button(self.frame, text="💾 Save Tasks", bootstyle=INFO, command=self.save_tasks).grid(row=4, column=2, pady=5)
        ttk.Button(self.frame, text="🗑️ Delete Task", bootstyle=DANGER, command=self.delete_task).grid(row=4, column=0, pady=5)

        # ADD this after task_list (treeview) and buttons
        self.status_label = ttk.Label(self.frame, text="", font=("Segoe UI", 10), anchor="w", bootstyle="info")
        self.status_label.grid(row=5, column=0, columnspan=2, sticky="w", pady=(5, 0))

        self.update_task_view()
        

    def load_tasks(self):
        if os.path.exists(self.file):
            with open(self.file, 'r') as f:
                self.tasks = json.load(f)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.file, 'w') as f:
            json.dump(self.tasks, f, indent=4)
        ttk.Messagebox.show_info("Saved", "Tasks saved successfully!")

    def add_task(self):
        desc = self.desc_entry.get().strip()
        cat = self.cat_entry.get().strip() or "General"
        if desc == "":
            ttk.Messagebox.show_warning("Warning", "Description cannot be empty!")
            return
        self.tasks.append({"description": desc, "category": cat, "completed": False})
        self.desc_entry.delete(0, 'end')
        self.cat_entry.delete(0, 'end')
        self.update_task_view()
    def mark_done(self):
        selected = self.task_list.selection()
        if not selected:
            ttk.Messagebox.show_warning("Select a Task", "Please select a task to mark as done.")
            return
        index = int(selected[0])
        self.tasks[index]["completed"] = True
        self.update_task_view()
    def delete_task(self):
        selected = self.task_list.selection()
        if not selected:
            from ttkbootstrap.dialogs import Messagebox
            Messagebox.show_warning("Select Task", "Please select a task to delete!", parent=self.root)
            return
        for iid in selected:
            # delete from list
            idx = int(iid)
            if 0 <= idx < len(self.tasks):
                self.tasks.pop(idx)
            # delete from treeview
            self.task_list.delete(iid)
        # refresh view and IDs after deletion
        self.update_task_view()


    

    def update_task_view(self):
        for i in self.task_list.get_children():
            self.task_list.delete(i)
        for idx, task in enumerate(self.tasks):
            status = "✅" if task.get("completed") else "❌"
            self.task_list.insert("", "end", iid=idx, values=(task["description"], task["category"], status))
            total = len(self.tasks)
            completed = sum(1 for task in self.tasks if task["completed"])
            pending = total - completed

            self.status_label.config(
                text=f"📊 Total: {total} | ✅ Completed: {completed} | ❌ Pending: {pending}"
            )
    # la.py ke end me add karo
    def get_pending_count():
        from json import load
        if not os.path.exists('tasks_gui.json'):
            return 0
        with open('tasks_gui.json', 'r') as f:
            tasks = load(f)
        pending = sum(1 for task in tasks if not task.get("completed"))
        return pending
        # la.py ke end me add karo (ya same file me jahan get_pending_count hai)

    def get_completed_count():
        from json import load
        if not os.path.exists('tasks_gui.json'):
            return 0
        with open('tasks_gui.json', 'r') as f:
            tasks = load(f)
        completed = sum(1 for task in tasks if task.get("completed"))
        return completed
                

if __name__ == "__main__":
            app = ttk.Window(themename="darkly")  # You can try: journal, flatly, darkly, cyborg etc.
            TaskManagerApp(app)
            app.mainloop()


