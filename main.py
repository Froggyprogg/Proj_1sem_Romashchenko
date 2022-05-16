import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):

    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#abcdef', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="BD/11.gif")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить записи', command=self.open_dialog, bg='#abcdef', width=150, bd=0,
                                    compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file="BD/12.gif")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, width=150, bg='#abcdef',
                                    bd=0, compound=tk.TOP, image=self.update_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="BD/13.gif")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#abcdef', width=150,
                                    bd=0, compound=tk.TOP, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="BD/14.gif")
        btn_search = tk.Button(toolbar, text="Поиск записи", command=self.open_search_dialog, bg='#abcdef', width=150,
                               bd=0, compound=tk.TOP, image=self.search_img)
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file="BD/15.gif")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#abcdef', width=150,
                               bd=0, compound=tk.TOP, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('user_id', 'date', 'strax', 'type', 'tarif', 'filial'), height=15, show='headings')

        self.tree.column('user_id', width=50, anchor=tk.CENTER)
        self.tree.column('date', width=180, anchor=tk.CENTER)
        self.tree.column('strax', width=140, anchor=tk.CENTER)
        self.tree.column('type', width=140, anchor=tk.CENTER)
        self.tree.column('tarif', width=140, anchor=tk.CENTER)
        self.tree.column('filial', width=140, anchor=tk.CENTER)

        self.tree.heading('user_id', text='ID')
        self.tree.heading('date', text='Дата заключения')
        self.tree.heading('strax', text='Страховая сумма')
        self.tree.heading('type', text='Вид страхования')
        self.tree.heading('tarif', text='Тарифная ставка')
        self.tree.heading('filial', text='Филиал')

        self.tree.pack()

    def records(self, user_id, date, strax, type, tarif, filial):
        self.db.insert_data(user_id, date, strax, type, tarif, filial)
        self.view_records()

    def update_record(self, user_id, date, strax, type, tarif, filial):
        self.db.cur.execute("""UPDATE users SET user_id=?, date=?, strax=?, type=?, tarif=?, filial=? WHERE user_id=?""",
                            (user_id, date, strax, type, tarif, filial, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM users""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM users WHERE user_id=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()


    def search_records(self, strax):
        tarif = (strax,)
        self.db.cur.execute("""SELECT * FROM users WHERE strax>?""", tarif)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]


    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()

class Child(tk.Toplevel):

    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить игрока')
        self.geometry('400x240+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Номер')
        label_description.place(x=50, y=25)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=150, y=25)

        label_date = tk.Label(self, text='Дата заключения')
        label_date.place(x=50, y=50)
        self.entry_date = ttk.Entry(self)
        self.entry_date.place(x=150, y=50)

        label_strax = tk.Label(self, text='Страховая сумма')
        label_strax.place(x=50, y=75)
        self.entry_strax = ttk.Entry(self)
        self.entry_strax.place(x=150, y=75)

        label_type = tk.Label(self, text='Вид страхования')
        label_type.place(x=50, y=100)
        self.entry_type = ttk.Entry(self)
        self.entry_type.place(x=150, y=100)

        label_tarif = tk.Label(self, text='Тарифная ставка')
        label_tarif.place(x=50, y=125)
        self.entry_tarif = ttk.Entry(self)
        self.entry_tarif.place(x=150, y=125)

        label_filial = tk.Label(self, text='Филиал')
        label_filial.place(x=50, y=150)
        self.entry_filial = ttk.Entry(self)
        self.entry_filial.place(x=150, y=150)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=190)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=190)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                       self.entry_date.get(),
                                                                       self.entry_strax.get(),
                                                                       self.entry_type.get(),
                                                                       self.entry_tarif.get(),
                                                                       self.entry_filial.get()))

        self.grab_set()
        self.focus_set()

class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=190)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                          self.entry_date.get(),
                                                                          self.entry_strax.get(),
                                                                          self.entry_type.get(),
                                                                          self.entry_tarif.get(),
                                                                          self.entry_filial.get()))
        self.btn_ok.destroy()

class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск")
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

class DB:
    def __init__(self):

        with sq.connect('BD/dogovor.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                date INTEGER NOT NULL,
                strax INTEGER,
                type TEXT NOT NULL,
                tarif INTEGER,
                filial TEXT NOT NULL
                )""")

    def insert_data(self, user_id, date, strax, type, tarif, filial):
        self.cur.execute("""INSERT INTO users(user_id, date, strax, type, tarif, filial) VALUES (?, ?, ?, ?, ?, ?)""",
                             (user_id, date, strax, type, tarif, filial))
        self.con.commit()

if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("СТРАХОВАЯ КОМПАНИЯ")
    root.geometry("800x600+300+200")
    root.resizable(False, False)
    root.mainloop()