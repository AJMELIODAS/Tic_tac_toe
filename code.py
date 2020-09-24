from tkinter import *
from tkinter import messagebox

board=Tk()
board.geometry('700x750')
board.title('Tic Tac Toe')
board.configure(bg='pink')
#board.iconbitmap('C:/Users/new/Downloads/tic-tac-toe_39453.ico')

global x
x=0
ps='' #player symbol



def new_game():
	global x
	warning.config(text='')
	x=0
	if p1['state']==p2['state']=='disabled':
		p1.config(state=NORMAL)
		p2.config(state=NORMAL)
	p1.delete(0,END)
	p2.delete(0,END)
	for j in [a,b,c,d,e,f,g,h,i]:
		if j['state']=='disabled':
			j.config(state=NORMAL)
			j.config(text='')

def rematch():
	global x
	x=0
	for j in [a,b,c,d,e,f,g,h,i]:
		if j['state']=='disabled':
			j.config(state=NORMAL)
			j.config(text='')


#Names frame
names=LabelFrame(board,padx=10,pady=10,bg='orange',bd=0)
names.pack(padx=10,pady=5)


#board frame
game=LabelFrame(board,padx=10,pady=10,bg='light green',bd=0)
game.pack(padx=10,pady=5)

#Buttons Frame
buttons=LabelFrame(board,padx=10,pady=10,bg='light blue',bd=0)
buttons.pack()

# entry check
def play():
	player1=p1.get()
	player2=p2.get()
	if player1=='' or player2=='':
		warning.config(text='Please enter player names!')
	else:
		p1.config(state=DISABLED)
		p2.config(state=DISABLED)
		warning.config(text=F'Player1: {player1.upper()}  and  Player2: {player2.upper()}')


def win(ps):
	if a['text']==b['text']==c['text']=='X'  or d['text']==e['text']==f['text']=='X' or g['text']==h['text']==i['text']=='X' or a['text']==e['text']==i['text']=='X' or c['text']==e['text']==g['text']=='X' or a['text']==d['text']==g['text']=='X' or b['text']==e['text']==h['text']=='X' or c['text']==f['text']==i['text']=='X':
		for j in [a,b,c,d,e,f,g,h,i]:
			if j['state']=='normal':
				j.config(state=DISABLED)
		messagebox.showinfo('Congratulations'.upper(),'THE WINNER IS '+str(ps).upper())
	elif a['text']==b['text']==c['text']=='O'  or d['text']==e['text']==f['text']=='O' or g['text']==h['text']==i['text']=='O' or a['text']==e['text']==i['text']=='O' or c['text']==e['text']==g['text']=='O' or a['text']==d['text']==g['text']=='O' or b['text']==e['text']==h['text']=='O' or c['text']==f['text']==i['text']=='O':
		for j in [a,b,c,d,e,f,g,h,i]:
			if j['state']=='normal':
				j.config(state=DISABLED)
		messagebox.showinfo('Congratulations'.upper(),'THE WINNER IS '+str(ps).upper())
	elif a['text']!='' and b['text']!='' and c['text']!='' and d['text']!='' and e['text']!='' and f['text']!='' and g['text']!='' and h['text']!='' and i['text']!='':
		messagebox.showwarning('Well PLayed'.upper(),'THE MATCH IS DRAW')

# position of piece
def pos(num):
	global x,ps
	if p1.get()!='' and p2.get()!='' and warning['text']==F'Player1: {str(p1.get()).upper()}  and  Player2: {str(p2.get()).upper()}':
		if num==1:
			if x%2==0:
				a.config(text='X',state=DISABLED)
				x+=1
			else:
				a.config(text='O',state=DISABLED)
				x+=1
			if a['text']=='X':
				ps=p1.get()
			elif a['text']=='O':
				ps=p2.get()

			win(ps)
		if num==2:
			if x%2==0:
				b.config(text='X',state=DISABLED)
				x+=1
			else:
				b.config(text='O',state=DISABLED)
				x+=1
			if b['text']=='X':
				ps=p1.get()
			elif b['text']=='O':
				ps=p2.get()
			win(ps)
		if num==3:
			if x%2==0:
				c.config(text='X',state=DISABLED)
				x+=1
			else:
				c.config(text='O',state=DISABLED)
				x+=1
			if c['text']=='X':
				ps=p1.get()
			elif c['text']=='O':
				ps=p2.get()				
			win(ps)
		if num==4:
			if x%2==0:
				d.config(text='X',state=DISABLED)
				x+=1
			else:
				d.config(text='O',state=DISABLED)
				x+=1
			if d['text']=='X':
				ps=p1.get()
			elif d['text']=='O':
				ps=p2.get()				
			win(ps)
		if num==5:
			if x%2==0:
				e.config(text='X',state=DISABLED)
				x+=1
			else:
				e.config(text='O',state=DISABLED)
				x+=1
			if e['text']=='X':
				ps=p1.get()
			elif e['text']=='O':
				ps=p2.get()							
			win(ps)
		if num==6:
			if x%2==0:
				f.config(text='X',state=DISABLED)
				x+=1
			else:
				f.config(text='O',state=DISABLED)
				x+=1
			if f['text']=='X':
				ps=p1.get()
			elif f['text']=='O':
				ps=p2.get()				
			win(ps)
		if num==7:
			if x%2==0:
				g.config(text='X',state=DISABLED)
				x+=1
			else:
				g.config(text='O',state=DISABLED)
				x+=1
			if g['text']=='X':
				ps=p1.get()
			elif g['text']=='O':
				ps=p2.get()				
			win(ps)
		if num==8:
			if x%2==0:
				h.config(text='X',state=DISABLED)
				x+=1
			else:
				h.config(text='O',state=DISABLED)
				x+=1
			if h['text']=='X':
				ps=p1.get()
			elif h['text']=='O':
				ps=p2.get()				
			win(ps)

		if num==9:
			if x%2==0:
				i.config(text='X',state=DISABLED)
				x+=1
			else:
				i.config(text='O',state=DISABLED)
				x+=1
			if i['text']=='X':
				ps=p1.get()
			elif i['text']=='O':
				ps=p2.get()				
			win(ps)																	
	else:
		warning.config(text='Please enter player names!')


# names of the players
Label(names,text='Enter Player 1 Name:',fg='green',font=('sans-serif',20),bg='orange').pack(pady=10)
p1=Entry(names,bd=0,bg='yellow',font=('sans-serif',20))
p1.pack()
Label(names,text='Enter Player 2 Name:',fg='green',font=('sans-serif',20),bg='orange').pack(pady=10)
p2=Entry(names,bd=0,bg='yellow',font=('sans-serif',20))
p2.pack()
Button(names,text='Start',fg='white',bg='green',bd=0,font=('sans-serif',20),command=play).pack(pady=10)


# warning message
warning=Label(names,text='',fg='red',font=('sans-serif',15),bg='orange')
warning.pack(pady=10)

color='white'
#game board
a=Button(game,text='',font=('sans-serif',20),width=6,height=3,bd=0,bg=color,command=lambda:pos(1))
a.grid(pady=5,padx=5,row=0,column=0)
b=Button(game,text='',font=('sans-serif',20),width=6,height=3,bd=0,bg=color,command=lambda:pos(2))
b.grid(pady=5,row=0,padx=5,column=1)
c=Button(game,text='',font=('sans-serif',20),width=6,height=3,bd=0,bg=color,command=lambda:pos(3))
c.grid(pady=5,row=0,padx=5,column=2)
d=Button(game,text='',font=('sans-serif',20),width=6,height=3,bd=0,bg=color,command=lambda:pos(4))
d.grid(pady=5,row=1,padx=5,column=0)
e=Button(game,text='',font=('sans-serif',20),width=6,height=3,bd=0,bg=color,command=lambda:pos(5))
e.grid(pady=5,row=1,padx=5,column=1)
f=Button(game,text='',font=('sans-serif',20),width=6,height=3,bd=0,bg=color,command=lambda:pos(6))
f.grid(pady=5,row=1,padx=5,column=2)
g=Button(game,text='',font=('sans-serif',20),width=6,height=3,bd=0,bg=color,command=lambda:pos(7))
g.grid(pady=5,row=2,padx=5,column=0)
h=Button(game,text='',font=('sans-serif',20),width=6,height=3,bd=0,bg=color,command=lambda:pos(8))
h.grid(pady=5,row=2,padx=5,column=1)
i=Button(game,text='',font=('sans-serif',20),width=6,height=3,bd=0,bg=color,command=lambda:pos(9))
i.grid(pady=5,row=2,padx=5,column=2)

new_game=Button(buttons,text='NEW GAME',bg='green',fg='white',command=new_game,bd=0,font=('sans-serif',20))
new_game.grid(row=0,column=0,padx=10)

rematch=Button(buttons,text='REMATCH',bg='green',fg='white',command=rematch,bd=0,font=('sans-serif',20))
rematch.grid(row=0,column=2,padx=10)

board.mainloop()
