from tkinter import Tk, Label, Button, Entry, filedialog, Canvas, PhotoImage
from PIL import Image, ImageTk
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic.face_counter import detect_faces

class AppUI:
    def __init__(self, master):
        self.master = master
        master.title("Face Recognition App")

        self.label = Label(master, text="Enter image path:")
        self.label.pack()

        self.entry = Entry(master, width=50)
        self.entry.pack()

        self.browse_button = Button(master, text="Browse", command=self.browse_image)
        self.browse_button.pack()

        self.load_button = Button(master, text="Load Image", command=self.load_image)
        self.load_button.pack()

        self.canvas = Canvas(master, width=400, height=400)
        self.canvas.pack()

        self.result_label = Label(master, text="")
        self.result_label.pack()

    def browse_image(self):
        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image",
                                              filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png")))
        self.entry.delete(0, 'end')
        self.entry.insert(0, filename)

    def load_image(self):
        image_path = self.entry.get()
        print(f"Loading image from: {image_path}")
        if os.path.isfile(image_path):
            # Nhận diện khuôn mặt và lưu ảnh kết quả
            output_path = "C:/Project/Project1/asset/output_images/detected_faces.jpg"
            num_faces = detect_faces(image_path, output_path)
            self.display_image(output_path)
            self.result_label.config(text=f"Đã nhận diện {num_faces} khuôn mặt.")
        else:
            self.result_label.config(text="Invalid image path.")

    def display_image(self, image_path):
        img = Image.open(image_path)
        try:
            resample = Image.Resampling.LANCZOS
        except AttributeError:
            resample = Image.LANCZOS
        # Resize giữ nguyên tỷ lệ, vừa với khung 400x400
        img.thumbnail((400, 400), resample)
        self.photo = ImageTk.PhotoImage(img)
        self.canvas.delete("all")  # Xóa ảnh cũ nếu có
        # Tính toán để ảnh nằm giữa khung
        x = (400 - img.width) // 2
        y = (400 - img.height) // 2
        self.canvas.create_image(x, y, anchor='nw', image=self.photo)

if __name__ == "__main__":
    root = Tk()
    app = AppUI(root)
    root.mainloop()