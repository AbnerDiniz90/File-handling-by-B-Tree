from customtkinter import *
from PIL import Image
from B_Tree import *


root = CTk()

root.geometry("800x600")

root.resizable(False, False)

root.iconbitmap("GUI_Images/big-data.ico")

root.title("Trabalho2")

set_appearance_mode("light")

B = B_Tree(3)

j = 0

qntd_elm = len(os.listdir("Banco_Imagens"))

#===========================================Erros==================================================

def erro_All_Inserted(number: int):

    for widget in frm_D.winfo_children():
        widget.destroy()

    lbl_error = CTkLabel(
    frm_D,
    text= f"Todas as {number} imagens já inseridas",
    text_color="black",
    font=("Arial", 12),
    anchor="nw",
    justify="left",
    wraplength=500,
    )
    lbl_error.pack(pady=10, expand=True)

def erro_Nothing_Found():

    for widget in frm_D.winfo_children():
        widget.destroy()

    lbl_error = CTkLabel(
    frm_D,
    text= "Nenhum elemento encontrado",
    text_color="black",
    font=("Arial", 12),
    anchor="nw",
    justify="left",
    wraplength=500,
    )
    lbl_error.pack(pady=10, expand=True)

#===========================================ExibirImprimir==================================================

def exibir_arvore():
    resultado = B.print_inOrder(B.root)

    for widget in frm_D.winfo_children():
        widget.destroy()

    lbl_resultado = CTkLabel(
        frm_D,
        text="\n".join(resultado) if resultado else "Nenhum elemento inserido",
        text_color="black",
        font=("Arial", 12),
        anchor="nw",
        justify="left",
        wraplength=500,
    )
    lbl_resultado.pack(pady=10, expand=True)

#===========================================ExibirBusca==================================================

def exibir_busca():

    actual = e.get()

    if actual == "":
        return erro_Nothing_Found()

    e.delete(0, END)

    resultado = B.search(actual)

    for img in resultado:
        i = Image.open(f"Banco_Imagens/{img}")
        i.show()

    for widget in frm_D.winfo_children():
        widget.destroy()

    lbl_busca = CTkLabel(
        frm_D,
        text="  ".join(resultado) if resultado else "Nenhum elemento encontrado",
        text_color="black",
        font=("Arial", 12),
        anchor="nw",
        justify="left",
        wraplength=500,
    )
    lbl_busca.pack(pady=10, expand=True)

#===========================================Inserir=========================================================

def insertion():
    option1 = checkbox_1.get()
    option2 = checkbox_2.get()
    image = load_imagem("Banco_Imagens")

    global j
    global qntd_elm

    if qntd_elm == 0:
        return

    if option1 == 1:
        if(j < len(image)):
            B.insert(image[j][0])
            j += 1
            qntd_elm -= 1

            lbl_12.configure(text=f"{j}")
            lbl_13.configure(text=f"{qntd_elm}")
        else:
            erro_All_Inserted(len(image))
            
    elif option2 == 1:
        for i in range(j, len(image)):
            B.insert(image[i][0])

        j = len(image)
        qntd_elm = 0

        lbl_12.configure(text=f"{j}")
        lbl_13.configure(text=f"{qntd_elm}")

#===========================================Deletar=========================================================

def delete():
    global j

    if e3.get() == "":
        return erro_Nothing_Found()
    
    category = B.search(f"{e3.get()}")

    e3.delete(0, END)

    for c in category:
        B.delete(B.root, c)
        j -= 1

    lbl_12.configure(text=f"{j}")

    exibir_arvore()
    
#===========================================CheckBoxInsertion=========================================================

def checkbox_toggle():
    if checkbox_1.get() == 1 and checkbox_2.get() == 1:
        checkbox_2.deselect()
        checkbox_1.deselect()
        

#===========================================Frames=========================================================

frm_A = CTkFrame(root, fg_color = "#1297A6", width = 230, height= 600)
frm_A.place(relx = 0.0, rely = 0.5, anchor = "w")

lbl = CTkLabel(
    root, text = "Recuperação de imagens usando Árvores-B", 
    text_color= "#1297A6",
    font=("Arial", 18, "bold"),
    wraplength=500)
    
lbl.place(relx = 0.32, rely = 0.08, anchor = "w")

icon = Image.open("GUI_Images/big-data.png")
lbl_icon = CTkLabel(frm_A, text = "", image = CTkImage(icon, size=(100, 100)))
lbl_icon.place(relx = 0.5, rely = 0.3, anchor = "center")

tittle = CTkLabel(
    frm_A, text = "AED II", 
    text_color= "white",
    font=("Arial", 18, "bold"),
    wraplength=250)
    
tittle.place(relx = 0.5, rely = 0.45, anchor = "center")


frm_B = CTkFrame(root, fg_color = "#1297A6", width = 230, height= 60)
frm_B.place(relx = 0.47, rely = 0.18, anchor = "center")

frm_C = CTkFrame(root, fg_color = "#1297A6", width = 230, height= 60)
frm_C.place(relx = 0.8, rely = 0.18, anchor = "center")

frm_D = CTkScrollableFrame(root, fg_color = "#F2F2F2", width = 520, height= 150, label_anchor="s")
frm_D.place(relx = 0.635, rely = 0.785, anchor = "center", relheight=0.245)

#===========================================Infos=========================================================

node = Image.open("GUI_Images/structured-data.png")

node_icon = CTkLabel(frm_B, text = "", image = CTkImage(node, size=(50, 50)))

node_icon.place(relx = 0.05, rely = 0.12)

lbl_11 = CTkLabel(
    frm_B, 
    text = "Nós:", 
    text_color= "White",
    font=("Arial", 15, "bold"))

lbl_12 = CTkLabel(
    frm_B, 
    text = f"{j}", 
    text_color= "White",
    font=("Arial", 15, "bold"))

picture = Image.open("GUI_Images/image.png")

picture_icon = CTkLabel(frm_C, text = "", image = CTkImage(picture, size=(40, 40)))

picture_icon.place(relx = 0.05, rely = 0.15)

lbl_1 = CTkLabel(
    frm_C, 
    text = "Imagens:", 
    text_color= "White",
    font=("Arial", 15, "bold"))

lbl_13 = CTkLabel(
    frm_C, 
    text = f"{qntd_elm}", 
    text_color= "White",
    font=("Arial", 15, "bold"))

lbl_11.place(relx = 0.3, rely = 0.1)

lbl_12.place(relx = 0.5, rely = 0.1)

lbl_1.place(relx = 0.3, rely = 0.1)

lbl_13.place(relx = 0.6, rely = 0.1)

#===========================================Inserção=========================================================

lbl_2 = CTkLabel(
    root, text = "Inserir", 
    text_color= "#1297A6",
    font=("Arial", 15))
    
lbl_2.place(relx = 0.35, rely = 0.27, anchor = "center")

cmb_box = CTkComboBox(master = root, border_width=0, values=["Inserção1", "Inserção2"])

checkbox_1 = CTkCheckBox(root, text="Inseção Tipo 1", onvalue=True, offvalue=False, command = checkbox_toggle)
checkbox_1.place(relx = 0.4, rely = 0.33, anchor = "center")

checkbox_2 = CTkCheckBox(root, text="Inserção Tipo 2", onvalue=True, offvalue=False, command = checkbox_toggle)
checkbox_2.place(relx = 0.65, rely = 0.33, anchor = "center")


cmb_btn = CTkButton(master = root, width = 100, text = "Inserir", fg_color = "#1297A6", hover_color = "#558080", anchor = "center", command=insertion)

cmb_btn.place(relx = 0.88, rely = 0.33, anchor = "center")

#===========================================Deletar=========================================================

lbl_3 = CTkLabel(
    root, text = "Deletar", 
    text_color= "#1297A6",
    font=("Arial", 15))
    
lbl_3.place(relx = 0.354, rely = 0.41, anchor = "center")

e3 = CTkEntry(root, width= 360, height= 30, border_width=0, placeholder_text="Deletar categoria")
e3.place(relx = 0.557, rely = 0.47, anchor = "center")

cmb_btn2 = CTkButton(master = root, width = 100, text = "Deletar", fg_color = "#1297A6", hover_color = "#558080", anchor = "center", command=delete)

cmb_btn2.place(relx = 0.88, rely = 0.47, anchor = "center")

#===========================================Pesquisar=========================================================

lbl_3 = CTkLabel(
    root, text = "Pesquisar", 
    text_color= "#1297A6",
    font=("Arial", 15))

lbl_3.place(relx = 0.365, rely = 0.55, anchor = "center")

btn = CTkButton(root, text = "Buscar", width = 100, fg_color = "#1297A6", hover_color = "#558080", anchor = "center", command=exibir_busca)

btn.place(relx = 0.88, rely = 0.61, anchor = "center")

e = CTkEntry(root, width= 360, height= 30, border_width=0, placeholder_text="Pesquisar imagem")
e.place(relx = 0.557, rely = 0.61, anchor = "center")

#===========================================Imprimir=========================================================

btn = CTkButton(root, 
                text = "Imprimir", 
                width = 100, 
                fg_color = "#1297A6", 
                hover_color = "#558080", 
                anchor = "center",
                command = exibir_arvore)

btn.place(relx = 0.645, rely = 0.95, anchor = "center")

#===========================================Nome/RA=========================================================

lbl_4 = CTkLabel(
    frm_A, text = "Abner A. P. Diniz", 
    text_color= "white",
    font=("Arial", 12, "bold"))

lbl_4.place(relx = 0.5, rely = 0.9, anchor = "center")

lbl_5 = CTkLabel(
    frm_A, text = "168476", 
    text_color= "white",
    font=("Arial", 12, "bold"))

lbl_5.place(relx = 0.5, rely = 0.935, anchor = "center")

#===========================================Dados=========================================================

def main():
    B = B_Tree(3)

main()

root.mainloop()