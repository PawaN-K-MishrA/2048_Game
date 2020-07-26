from tkinter import Frame, Label, CENTER
import logic
import constants as c

class Game2048(Frame):
	def __init__(self):
		Frame.__init__(self)
		self.grid()
		self.master.title('2048')
		self.master.bind("<Key>",self.key_down)
		self.commands={c.key_up:logic.move_up,c.key_down:logic.move_down,
						c.key_left:logic.move_left,c.key_right:logic.move_right}
		self.grid_cells=[]
		self.init_grid()
		self.init_matrix()
		self.update_grid_cells()
		self.mainloop()
	
	def init_grid(self):
		background=Frame(self,bg=c.bgcolor_game,width=c.size,height=c.size)
		background.grid()
		for i in range(c.grid_len):
			grid_row=[]
			for j in range(c.grid_len):
				cell=Frame(background,bg=c.bgcolor_emptycell,width=c.size/c.grid_len,height=c.size/c.grid_len)
				cell.grid(row=i,column=j,padx=c.grid_padding,pady=c.grid_padding)
				t=Label(master=cell,text='',bg=c.bgcolor_emptycell,justify=CENTER,font=c.font,width=5,height=2)
				t.grid()
				grid_row.append(t)
			self.grid_cells.append(grid_row)
	
	def init_matrix(self):
		self.matrix=logic.start_game()
		logic.add_new2(self.matrix)
		logic.add_new2(self.matrix)
		
	def update_grid_cells(self):
		for i in range(c.grid_len):
			for j in range(c.grid_len):
				new_number=self.matrix[i][j]
				if new_number==0:
					self.grid_cells[i][j].configure(text='',bg=c.bgcolor_emptycell)
				else:
					self.grid_cells[i][j].configure(text=str(new_number),bg=c.bgcolor_dict[new_number],fg=c.cellcolor_dict[new_number])
		self.update_idletasks()
	
	def key_down(self,event):
		key=repr(event.char)
		if key in self.commands:
			self.matrix,changed=self.commands[repr(event.char)](self.matrix)
			if changed:
				logic.add_new2(self.matrix)
				self.update_grid_cells()
				changed=False
				if logic.get_curr_state_of_game(self.matrix)=='WON':
					self.grid_cells[1][1].configure(text='YOU',bg=c.bgcolor_emptycell)
					self.grid_cells[1][2].configure(text='Win!',bg=c.bgcolor_emptycell)
				if logic.get_curr_state_of_game(self.matrix)=='LOST':
					self.grid_cells[1][1].configure(text='YOU',bg=c.bgcolor_emptycell)
					self.grid_cells[1][2].configure(text='LOST',bg=c.bgcolor_emptycell)
					
					
gamedrid=Game2048()
		
				