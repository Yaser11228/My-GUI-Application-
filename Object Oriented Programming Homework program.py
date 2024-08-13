import tkinter as tk

def save_homework():
     title = entry_homework_title.get()
     description = entry_homework_description.get("1.0", "end-1c")
     with open("homework.txt", "a") as file:
         file.write(f"{title}\n{description}\n\n")
     entry_homework_title.delete(0, "end")
     entry_homework_description.delete("1.0", "end")
     show_homework()

def show_homework():
    global homework_window
    try:
        homework_window.destroy()
    except:
        pass
    homework_window = tk.Toplevel(root)
    homework_window.title("تکالیف خانگی")

    with open("homework.txt", "r") as file:
         content = file.read()
    label = tk.Label(homework_window, text=content)
    label.pack()

root = tk.Tk()
root.title("برنامه تکالیف خانگی")

button_show_homework = tk.Button(root, text="نمایش تکالیف خانگی", command=show_homework)
button_show_homework.pack()

button_save_homework = tk.Button(root, text="ذخیره تکالیف خانگی", command=save_homework)
button_save_homework.pack()

label_homework_title = tk.Label(root, text="عنوان تکلیف:")
label_homework_title.pack()

entry_homework_title = tk.Entry(root)
entry_homework_title.pack()

label_homework_description = tk.Label(root, text="توضیحات تکلیف:")
label_homework_description.pack()

entry_homework_description = tk.Text(root, height=5, width=50)
entry_homework_description.pack()

root.mainloop()



