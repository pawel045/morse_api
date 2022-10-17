from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import morse

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'))
templates = Jinja2Templates(directory="templates")


alphabet = morse.Alphabet()


@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# GET a random character
@app.get("/random")
async def random():
    char = alphabet.get_rand_char()
    return {
        'length': len(char[0]),
        char[0]: char[1]
    }


# GET a translated text
@app.get("/translate/{text}")
async def translate(text: str = Form(...)):
    translated_text = alphabet.translate(text)

    if 'X' in translated_text:
        return {
            'length': len(text),
            text: translated_text,
            'X': 'some characters not recognized',
        }
    else:
        return {
            'length': len(text),
            text: translated_text,
        }
    