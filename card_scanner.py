from tkinter import *
import tkinter.messagebox as tmsg
import pandas
from PIL import Image, ImageTk
from tkinter import filedialog
import pytesseract	
import os.path

root = Tk()

root.geometry('800x500')	
root.maxsize(1000, 500)
root.minsize(600, 500)
root.title('Visiting card scanner')

def fileUploader():	
	global filename
	global start, last
	filename = filedialog.askopenfilename(
		initialdir='/Desktop', title = 'Select a card image',
	filetypes=(('jpeg files', '.jpg'), ('png files', '.png')))
	
	if filename == '':
		t.delete(1.0, END)
		t.insert(1.0, 'You have not provided any image to convertImage')
		tmsg.showwarning(
			title = 'Alert!', message = 'Please provide proper formatted image')
		return
	
	else:
		p_label_var.set('Image uploaded successfully')
		l.config(fg='#0CDD19')
	
	if filename.endswith('.JPG') or filename.endswith('.JPEG') or filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.PNG') or filename.endswith('.png'):
		filename_rev = filename[::-1]
		last = filename.index('.')
		start = len(filename) - filename_rev.index('/') - 1


def convertImage():	
	try:
		c_label_var.set('Output...')
		pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
		text = pytesseract.image_to_string(filename)
		t.delete(1.0, END)
		t.insert(1.0, text)
		root1 = Toplevel()
		root1.title('Uploaded image')
		img1 = ImageTk.PhotoImage(Image.open(filename))
		Label(root1, image=img1).pack()
		root1.mainloop()
	except:
		t.delete(1.0, END)
		t.insert(1.0, 'You have not provided any image to convertImage')
		tmsg.showwarning(
			title='Alert!', message='Please provide proper formatted image')
		return
	fileName = filename[start+1:last]+'.txt'
	fileName = os.path.join(r'Database', fileName)
	f = open(fileName, 'w')
	f.write(text)
	f.close()


mainMenu = Menu(root)
mainMenu.config(font = ('Times', 29))

menuObject1 = Menu(mainMenu, tearoff = 0)
menuObject1.add_command(label = 'Scan/Upload Visiting or Business cards and get all the text of cards',
			font = ('Times', 13))
root.config(menu = mainMenu)
mainMenu.add_cascade(label = 'Aim', menu = menuObject1)

menuObject2 = Menu(mainMenu, tearoff = 0)
menuObject2.add_command(label = '|| Computer Science and Engineering student ||',
			font = ('Times', 13))
menuObject2.add_command(label = '|| Coding Enthusiast ||', font = ('Times', 13))
root.config(menu = mainMenu)
mainMenu.add_cascade(label = 'About us', menu = menuObject2)

menuObject3 = Menu(mainMenu, tearoff=0)
menuObject3.add_command(label = 'E-mail: yashsharma2418@gmail.com',
			font = ('Times', 13))
menuObject3.add_separator()
menuObject3.add_command(label = 'Mobile: +91-8739811774', font=('Times', 13))
menuObject3.add_separator()

root.config(menu = mainMenu)
mainMenu.add_cascade(label = 'Contact us', menu = menuObject3)

Label(text = 'Visiting card scanner', bg = '#FAD2B8',
	fg = '#39322D', font = ('Times', 18)).pack(fill = 'x')
Label(text = 'Python GUI', bg = '#FAD2B8', fg ='#39322D', font=(
	'Times New Roman', 12, 'italic')).pack(fill='x')

frame = Frame()
frame.config(bg='white')
Label(frame, text='Browse photo to upload', width=20,
	font=('Times', 15), bg='white').pack(side='left')
Label(frame, text='format: png/jpeg', bg='white',
	width=30).pack(side='right', padx=5)
Button(frame, text='Upload card', bg='#F58D4B', font=('Times', 15),
	width=70, command=fileUploader).pack(side='right')
frame.pack(pady=10, fill='x')
p_label_var = StringVar()
p_label_var.set('Please upload an image to scan')
l = Label(textvariable=p_label_var, fg='red', bg='white')
l.pack()

Label(text='Developer: Yash Sharma', bg='#433E3B', fg='white',
	font=('Times', 10, ' italic')).pack(side='bottom', fill='x')
t = Text(root, height='9', font=('Times', 13))
t.pack(side='bottom', fill='x')
t.insert(1.0, 'Text of converted card will be shown here...', END)
c_label_var = StringVar()
c_label_var.set('Ready for conversion')
c_label = Label(textvariable=c_label_var)
c_label.pack(side='bottom', anchor='w')
Button(root, text='Scan and Convert', bg='#F58D4B', font=('Times', 15),
	width=70, command=convertImage).pack(pady='10', side='bottom')
root.mainloop()