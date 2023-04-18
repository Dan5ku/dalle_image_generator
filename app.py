#tested on python 3.9.0
from auth import auth_token
import tkinter as tk
from PIL import Image, ImageTk
import requests

# pip install openai
import openai

openai.api_key = auth_token

# create the app
app = tk.Tk()
app.geometry("532x632")
app.title("DALL E magic")

main_image = tk.Canvas(app, width=512, height=512)
main_image.place(x=10, y=110)

prompt_input = tk.Entry(
    app,
    font=("Arial", 16),
    width=38,
    bg="white",
    fg="black",
)
prompt_input.insert(0, "Enter prompt.")
prompt_input.place(x=10, y=10)


def apply_magic():
    global tk_img
    global img

    prompt = prompt_input.get()
    response = openai.Image.create(prompt=prompt, n=1, size="512x512")
    image_url = response["data"][0]["url"]
    img = Image.open(requests.get(image_url, stream=True).raw)
    tk_img = ImageTk.PhotoImage(img)
    main_image.create_image(0, 0, anchor=tk.NW, image=tk_img)
    print("Image created for prompt:", prompt)


def save_image():
    prompt = prompt_input.get().replace(" ", "_")
    img.save(f"img/{prompt}.png")


magic_button = tk.Button(
    app,
    font=("Arial", 20),
    bg="white",
    fg="black",
    text="Apply magic",
    command=apply_magic,
)
magic_button.place(x=100, y=60)

save_button = tk.Button(
    app,
    font=("Arial", 20),
    bg="white",
    fg="black",
    text="Save image",
    command=save_image,
)
save_button.place(x=266, y=60)

app.mainloop()
