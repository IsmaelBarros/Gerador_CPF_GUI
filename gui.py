import tkinter as tk

root = tk.Tk()

main_title = tk.Label(
    root,
    text='Gerador/Validador de CPF',
    bg='#fff',
    font=('Helvica', 12, 'bold')
)
main_title.grid(row=0, column=0, columnspan=3, pady=(0, 20))

validate_label = tk.Label(root, text='Validar:', bg='#fff')
validate_label.grid(row=1, column=0)

root.title('Gerador/Validador de CPF')
root.config(background='#fff', padx=20, pady=20)
root.mainloop()
