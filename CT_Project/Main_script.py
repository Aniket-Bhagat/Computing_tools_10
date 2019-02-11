#!/usr/bin/env python
from Tkinter import *
import tkFileDialog,ttk,sys,os
from nucleotide import *			# User defind module
from protein import * 			# User defind module

def restart_program():
	python = sys.executable					# gives path of executable binary for python interpreter
	os.execl(python, python, * sys.argv)	# execute a new program, replacing the current process


root = Tk()
root.title('SNV Detection Tool')
root.geometry('1200x720')
mainframe = ttk.Frame(root, padding="10 10 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))


#------------------------------------------Heading-------------------------------------------#
label1 = Label(mainframe, text ="SNV Detection Tool",foreground="red",font="Times 25 bold")
label1.grid(row=0, columnspan=7, pady=10)

#--------------------------------------------------------------------------------------------#

def browseQuery():
	filename = tkFileDialog.askopenfilename(title = "Select Query sequence file",
		filetypes = (("fasta files","*.fasta"),("all files","*.*")))
	#Using try in case user types in unknown file or closes without choosing a file.
	try:
		with open(filename,'r') as f:
			content = f.read()
			e1.delete('1.0', END)
			e1.insert('1.0', content)
	except:
		pass

label2 = Label(mainframe,text=" Input Nucleotide Query Sequence (fasta format) :", font="Times 20",anchor=W)
label2.grid(row=1,columnspan=3, sticky="w")

e1 = Text(mainframe,height=5,width=80)
e1.insert(END, '')
e1.grid(row=2,columnspan=3,sticky="w",padx=3,pady=3)

browsebutton = Button(mainframe, text="Browse", command=browseQuery)
browsebutton.grid(row=3,columnspan=3,sticky="w",padx=3,pady=3)

#--------------------------------------------------------------------------------------------#

empty = Label(mainframe,text="",anchor=W)
empty.grid(row=4, sticky='s')

def browseRef():
	filename = tkFileDialog.askopenfilename(title = "Select Refrence sequence file",filetypes = (("fasta files","*.fasta"),("all files","*.*")))
	#Using try in case user types in unknown file or closes without choosing a file.
	try:
		with open(filename,'r') as f:
			content = f.read()
			e2.delete('1.0', END)
			e2.insert('1.0', content)
	except:
		pass

label3 = Label(mainframe,text=" Input Nucleotide Refrence Sequence (fasta format) :", font="Times 20",anchor=W)
label3.grid(row=5,columnspan=3, sticky="w")

e2 = Text(mainframe,height=5,width=80)
e2.insert(END, '')
e2.grid(row=6,columnspan=3,sticky="w",padx=3,pady=3)

browsebutton = Button(mainframe, text="Browse", command=browseRef)
browsebutton.grid(row=7,columnspan=3,sticky="w",padx=3,pady=3)

#--------------------------------------------------------------------------------------------#

Label(mainframe,text="",anchor=W).grid(row=8, sticky='s')

def LoadEmboss():
	with open('alpha.faa','w') as q:
		q.write(e1.get('0.1',END))
		q.close()
	with open('beta.faa','w') as r:
		r.write(e2.get('0.1',END))
		r.close()

	mutation.configure(text = DoEmboss(var.get()))
	SeqStats(e1,R1,R2,R3,R4,R5,R6,R7,R8)


Emboss = Button(mainframe, text="EMBOSS", command=LoadEmboss)
Emboss.grid(row=9,columnspan=3,sticky="w")

var = IntVar()
Checkbutton(mainframe, text="save EMBOSS alignment file as 'alignment.txt'", variable=var).grid(row=9,column=1,columnspan=2, sticky=W)

#---------------------------------------------------------------------------------------------#

Label(mainframe, text = 'Results :', font="Times 20").grid(row=10,columnspan=3, sticky = 'w')

Label(mainframe,text="Sequence Length : ").grid(row=11,column=0,sticky="w",pady=3)
R1=Text(mainframe,height=1.3,width=40,borderwidth=0); R1.grid(row=11,column=1,sticky="w")

Label(mainframe,text="Guanine (G) : ").grid(row=12,column=0,sticky="w",pady=3)
R2=Text(mainframe,height=1.3,width=40,borderwidth=0); R2.grid(row=12,column=1)

Label(mainframe,text="Cytosine (C) : ").grid(row=13,column=0,sticky="w",pady=3)
R3=Text(mainframe,height=1.3,width=40,borderwidth=0); R3.grid(row=13,column=1)

Label(mainframe,text="Thaimine (T): ").grid(row=14,column=0,sticky="w",pady=3)
R4=Text(mainframe,height=1.3,width=40,borderwidth=0); R4.grid(row=14,column=1)

Label(mainframe,text="Adenine (A) : ").grid(row=15,column=0,sticky="w",pady=3)
R5=Text(mainframe,height=1.3,width=40,borderwidth=0); R5.grid(row=15,column=1)

Label(mainframe,text="GC-content(%) : ").grid(row=16,column=0,sticky="w",pady=3)
R6=Text(mainframe,height=1.3,width=40,borderwidth=0); R6.grid(row=16,column=1)

Label(mainframe,text="Start codons : ").grid(row=17,column=0,sticky="w",pady=3)
R7=Text(mainframe,height=1.3,width=40,borderwidth=0); R7.grid(row=17,column=1)

Label(mainframe,text="Start codons : ").grid(row=18,column=0,sticky="w",pady=3)
R8=Text(mainframe,height=1.3,width=40,borderwidth=0); R8.grid(row=18,column=1)

mutation=Label(mainframe, text = 'mutation', font="Times 20")
mutation.grid(row=19,columnspan=3, sticky = 'w')


#--------------------------------------Empty-column---------------------------------------#
Label(mainframe,text="			",anchor=S).grid(row=11,column=2,columnspan=2,sticky='s')

#--------------------------------------Protein-Sequence---------------------------------------#

label4 = Label(mainframe,text=" Translated Protein Sequence (Query) :", font="Times 20",anchor=W)
label4.grid(row=1,column=4,columnspan=3, sticky="w")
e3 = Text(mainframe,height=5,borderwidth=0,width=80)
e3.insert(INSERT, '')
e3.grid(row=2,column=4,columnspan=3,sticky="w",padx=3,pady=3)

label5 = Label(mainframe,text=" Translated Protein Sequence (Refrence) :", font="Times 20",anchor=W)
label5.grid(row=5,column=4,columnspan=3, sticky="w")
e4 = Text(mainframe,height=5,borderwidth=0,width=80)
e4.insert(INSERT, '')
e4.grid(row=6,column=4,columnspan=3,sticky="w",padx=3,pady=3)


#---------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------#
def ShowProtein():
	query_N = e1.get('0.1',END)
	ref_N = e2.get('0.1',END)
	
	query_P = GetProtein(query_N)
	ref_P = GetProtein(ref_N)
	e3.insert('1.0', query_P)
	e4.insert('1.0', ref_P)

	result=CompareProtein(query_P,ref_P)
	if result!='':
		result2.configure(text = result+' : Nonsynonymous Mutation')
		pos = map(lambda x : int(x.split()[-1]),result.split('\n'))
		for i in range(len(pos)):
				e3.tag_add("base", "1."+str(pos[i]-1), "1."+str(pos[i])) ; e3.tag_config("base", background = "red", foreground = "white")
				e4.tag_add("base", "1."+str(pos[i]-1), "1."+str(pos[i])) ; e4.tag_config("base", background = "red", foreground = "white")
	else:
		result2.configure(text = 'No change in Protein sequence : Synonymous Mutation')

	# e3.configure(state="disabled");	e4.configure(state="disabled")

ProtAnalysis = Button(mainframe, text="Analysis", command=ShowProtein)
ProtAnalysis.grid(row=7,column=4,columnspan=3,sticky="w")

result2 = Label(mainframe, text = 'Result2', font="Times 20")
result2.grid(row=8,column=4,columnspan=3, sticky = 'w')

#---------------------------------------------------------------------------------------------------------------#
def runBlast():
	blast(e4,P1,P2,P3)

Blast = Button(mainframe, text="BLAST", command=runBlast)
Blast.grid(row=10,column=4,columnspan=3,sticky="w")


Label(mainframe,text="Sequence Length :").grid(row=11,column=4,sticky="w",pady=3)
P1=Text(mainframe,height=1.3,width=40,borderwidth=0); P1.grid(row=11,column=5,sticky="w")

Label(mainframe,text="Sequence Details :").grid(row=12,column=4,sticky="w",pady=3)
P2=Text(mainframe,height=1.3,width=40,borderwidth=0); P2.grid(row=12,column=5,sticky="w")

Label(mainframe,text="Accession Number :").grid(row=13,column=4,sticky="w",pady=3)
P3=Text(mainframe,height=1.3,width=40,borderwidth=0); P3.grid(row=13,column=5,sticky="w")



#---------------------------------------restart-the-whole-program-----------------------------------------------#
Button(mainframe, text="Reset", command=restart_program).grid(row=20,columnspan=7,sticky=E)

root.mainloop()