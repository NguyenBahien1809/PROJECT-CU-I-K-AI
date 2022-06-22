# load libraries
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np
#load the trained model to recognize rice disease
from keras.models import load_model
model = load_model('disease.h5')
#Classes Label
classes = { 
    0:'bacterial leaf bright',
    1:'brown spot',
    2:'Healthy',
    3:'Leaf smut',
}
#create Gui
top=tk.Tk()
top.geometry('800x500')
top.title('Recognition Rice Disease')
top.configure(background='#c5d5c5')
label=Label(top,background='#CDCDCD', font=('arial',15,'bold'))
sign_image = Label(top)
def classify(file_path):
    global label_packed    
    img = load_img(file_path,target_size=(64,64))
    img = img_to_array(img)
    img = img.reshape(1,64,64,3)
    img = img.astype('float32')
    img = img/255   
    kq = np.argmax(model.predict(img),axis=-1)
    
    if(kq==0):
        kq = "Bacterial Leaf Blight:cần phun thuốc trừ sâu, bón phân cân đối giữa các loại đạm NPK, không xạ dày "
    if(kq==1):
        kq = "Brown Spot:không nên xạ dày, cày bừa xáo đất kĩ trước khi xạ, bón nhiều phân chuồng và các loại phân hỗn hợp NPK "
    if(kq==2):
        kq = "Healthy: Cây lúa phát triển tốt, khoẻ mạnh"
    if(kq==3):
        kq = "Leaf Smut: Cần cân bằng các loại dinh dưỡng,dọn sạch các mảnh vụn cuối mùa sinh trưởng,sử dụng loại giống lúa khoẻ,kháng bệnh"
  
    label.configure(foreground='#da2616', text=kq) 
    
def show_classify_button(file_path):
    classify_b=Button(top,text="Recognize Rice Disease",
   command=lambda: classify(file_path),padx=10,pady=15)
    classify_b.configure(background='#364156', foreground='white',
font=('arial',13,'bold')) #recognize
    classify_b.place(relx=0.69,rely=0.46)
def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),
    (top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass
upload=Button(top,text="Upload an image",command=upload_image,
  padx=10,pady=15)
upload.configure(background='#364156', foreground='white',
    font=('arial',13,'bold')) #upload
upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Rice Disease Recognition ",pady=15, font=('arial',20,'bold'))
heading.configure(background='#364156',foreground='white')
heading.pack()
top.mainloop()