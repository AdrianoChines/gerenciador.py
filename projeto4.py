# -*- coding: utf-8 -*-
"""
Created on Wed Oct 5 21:05:41 2016
@author: adrianoaguiar156@hotmail.com

"""
import pymysql
from tkinter import *
from tkinter import messagebox

class Banco:
     def __init__(self):
         self.conexao=pymysql.connect(host="localhost",user="root",passwd="chines22",db="projeto4")
         self.criarTabela()

     def criarTabela(self):
         c = self.conexao.cursor()
         c.execute("""CREATE TABLE if not exists clientes(
         id INT NOT NULL AUTO_INCREMENT,
         nome VARCHAR(45) NOT NULL,
         celular VARCHAR(12) NOT NULL,
         telefone VARCHAR(12) NOT NULL,
         veiculo VARCHAR(45) NOT NULL,
         placa VARCHAR(45) NOT NULL,
         servico VARCHAR(45) NOT NULL,
         PRIMARY KEY (id))""")
         self.conexao.commit()
         self.conexao.close

class Cliente:
     def __init__(self, id, nome, celular, telefone, veiculo, placa, servico):
         self.id = id
         self.nome = nome
         self.celular = celular
         self.telefone = telefone
         self.veiculo = veiculo
         self.placa = placa
         self.servico = servico
         
     def inserirCliente(self):
         banco = Banco()
         c = banco.conexao.cursor()
         c.execute("insert into clientes (nome, celular, telefone, veiculo, placa, servico) values ('" + self.nome + "', '" + self.celular + "', '" + self.telefone + "', '" + self.veiculo + "', '" + self.placa + "', '" + self.servico + "')")
         banco.conexao.commit()
         c.close()
         
     def atualizarCliente(self):
         banco = Banco()
         c = banco.conexao.cursor()
         self.id = str(self.id)
         c.execute("update clientes set nome = '" + self.nome + "',celular = '" + self.celular + "', telefone = '" + self.telefone + "', veiculo = '" + self.veiculo + "', placa = '" + self.placa + "', servico = '" + self.servico + "' where id = " + self.id + " ")
         banco.conexao.commit()
         c.close()
         
     def selecionarCliente(self, id):
         banco = Banco()
         c = banco.conexao.cursor()
         id = str(id)
         c.execute("select * from clientes where id = " + id + " ")
         for linha in c:
             self.id = linha[0]
             self.nome = linha[1]
             self.celular = linha[2]
             self.telefone = linha[3]
             self.veiculo = linha[4]
             self.placa = linha[5]
             self.servico = linha[6]
             c.close()
             
     def deletarCliente(self):
         banco = Banco()
         c = banco.conexao.cursor()
         self.id = str(self.id)
         c.execute("delete from clientes where id = " + self.id + " ")
         banco.conexao.commit()
         c.close()

class Aplicacao:
     def __init__(self, master=None):
         self.cont1 = Frame(master, pady =10)
         self.cont1.pack()
         self.cont2 = Frame(master, padx =20, pady=5)
         self.cont2.pack()
         self.cont3 = Frame(master, padx =20, pady=5)
         self.cont3.pack()
         self.cont4 = Frame(master, padx =20, pady=5)
         self.cont4.pack()
         self.cont5 = Frame(master, padx =20, pady=5)
         self.cont5.pack()
         self.cont6 = Frame(master, padx =20, pady=10)
         self.cont6.pack()
         self.cont7 = Frame(master, padx =20, pady =7)
         self.cont7.pack()
         self.cont8 = Frame(master, pady =10)
         self.cont8.pack()
        
         self.titulo = Label(self.cont1, text="Gerenciador")
         self.titulo.pack ()
        
         self.lblid = Label(self.cont4, text="ID:")
         self.lblid.pack(side=LEFT)
         self.txtid = Entry(self.cont4)
         self.txtid.pack(side=LEFT)
         
         self.lblnome = Label(self.cont5, text="Nome:")
         self.lblnome.pack(side=LEFT)
         self.txtnome = Entry(self.cont5)
         self.txtnome.pack(side=LEFT)
        
         self.lblcelular= Label(self.cont5, text="Celular:")
         self.lblcelular.pack(side=LEFT)
         self.txtcelular = Entry(self.cont5)
         self.txtcelular.pack(side=LEFT)
         
         self.lbltelefone = Label(self.cont5, text="Telefone:")
         self.lbltelefone.pack(side=LEFT)
         self.txttelefone = Entry(self.cont5)
         self.txttelefone.pack(side=LEFT)
         
         self.lblveiculo = Label(self.cont6, text = "Veículo:")
         self.lblveiculo.pack(side=LEFT)
         self.txtveiculo = Entry(self.cont6)
         self.txtveiculo.pack(side=LEFT)
         
         self.lblplaca = Label(self.cont6, text = "Placa:")
         self.lblplaca.pack(side=LEFT)
         self.txtplaca = Entry(self.cont6)
         self.txtplaca.pack()
         
         self.lblservico = Label(self.cont7, text = "Serviços:")
         self.lblservico.pack()
         self.txtservico = Text(self.cont8)
         self.txtservico.pack()
         
         self.btnBuscar = Button(self.cont3, text="Buscar", background = "grey")
         self.btnBuscar["command"] = self.buscarCliente
         self.btnBuscar.pack()
        
        
         self.bntIns = Button(self.cont2, text="Cadastrar", background = "light green")
         self.bntIns["command"] = self.inserirCliente
         self.bntIns.pack (side=LEFT)
        
         self.bntAlt = Button(self.cont2, text="Alterar", background = "grey")
         self.bntAlt["command"] = self.alterarCliente
         self.bntAlt.pack (side=LEFT)
        
         self.bntEx = Button(self.cont2, text="Excluir", background = "red")
         self.bntEx["command"] = self.excluirCliente
         self.bntEx.pack(side=LEFT)

     def inserirCliente(self):
         id = self.txtid.get()
         nome = self.txtnome.get()
         celular = self.txtcelular.get()
         telefone = self.txttelefone.get()
         veiculo = self.txtveiculo.get()
         placa = self.txtplaca.get()
         servico = self.txtservico.get(0.0, END)
         user = Cliente(id, nome, celular, telefone, veiculo, placa, servico)
        
         user.inserirCliente()
         
         messagebox.showinfo(title='Aviso!', message='Cliente "%s" Cadastrado Com Sucesso!' %(nome))
         
     def alterarCliente(self):
         id = self.txtid.get()
         nome = self.txtnome.get()
         celular = self.txtcelular.get()
         telefone = self.txttelefone.get()
         veiculo = self.txtveiculo.get()
         placa = self.txtplaca.get()
         servico = self.txtservico.get(0.0, END)
         user = Cliente(id, nome, celular, telefone, veiculo, placa, servico)
         var = messagebox.askokcancel(title='Atenção!', message='Alterar Dados De "%s".' %(nome))

         if (var == True):
             user.atualizarCliente()
             messagebox.showinfo(title = 'Aviso!', message = 'Informações Do Cliente "%s" Atualizados.' %(nome))
         else:
             return
             
     def excluirCliente(self):
         id = self.txtid.get()
         nome = self.txtnome.get()
         celular = self.txtcelular.get()
         telefone = self.txttelefone.get()
         veiculo = self.txtveiculo.get()
         placa = self.txtplaca.get()
         servico = self.txtservico.get(0.0, END)
         user = Cliente(id, nome, celular, telefone, veiculo, placa, servico)
         var = messagebox.askokcancel(title = 'Atenção!', message = 'Excluir Todas Informações De "%s".' %(nome))
         
         if (var == True):
             user.deletarCliente()
             messagebox.showinfo(title = 'Aviso!', message = 'Cliente "%s" Excluído Com Sucesso!' %(nome))
             self.txtid.delete(0, END)
             self.txtnome.delete(0, END)
             self.txtcelular.delete(0, END)
             self.txttelefone.delete(0, END)
             self.txtveiculo.delete(0, END)
             self.txtplaca.delete(0, END)
             self.txtservico.delete(0.0, END)
         else:
             return

     def buscarCliente(self):
         id = self.txtid.get()
         nome = self.txtnome.get()
         celular = self.txtcelular.get()
         telefone = self.txttelefone.get()
         veiculo = self.txtveiculo.get()
         placa = self.txtplaca.get()
         servico = self.txtservico.get(0.0, END)
         user = Cliente(id, nome, celular, telefone, veiculo, placa, servico)
         
         if (id != ""):
             
             user.selecionarCliente(id)
         
             self.txtnome.delete(0, END)
             self.txtnome.insert(INSERT, user.nome)
        
             self.txtcelular.delete(0, END)
             self.txtcelular.insert(INSERT, user.celular)
        
             self.txttelefone.delete(0, END)
             self.txttelefone.insert(INSERT, user.telefone)
         
             self.txtveiculo.delete(0, END)
             self.txtveiculo.insert(INSERT, user.veiculo)
         
             self.txtplaca.delete(0, END)
             self.txtplaca.insert(INSERT, user.placa)
         
             self.txtservico.delete(0.0, END)
             self.txtservico.insert(INSERT, user.servico)
             
         else:
             messagebox.showinfo(title = 'Aviso!', message = 'Nenhum "ID" Inserido. \n Tente Novamente.')
             return
         
raiz = Tk()
Aplicacao(raiz)
raiz.geometry('800x600')
raiz.mainloop()
