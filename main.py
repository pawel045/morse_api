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
@app.get("/encrypt")
async def decrypt(text: str):
    encrypted_text = alphabet.encrypt(text)

    if 'X' in encrypted_text:
        return {
            'length': len(text),
            'original text': text,
            'encrypted text': encrypted_text,
            'X': 'some characters unrecognized',
        }
    else:
        return {
            'length': len(text),
            'original text': text,
            'translated text': encrypted_text,
        }


@app.get("/decrypt")
async def encrypt(text: str):
    decrypted_text = alphabet.decrypt(text)

    if not decrypted_text:
        return {
            'error': 'Encrypted message is not a morse code text'
        }

    elif '_' in decrypted_text:
        return {
            'length': len(text),
            'original text': text,
            'encrypted text': decrypted_text,
            '_': 'some characters unrecognized',
        }

    else:
        return {
            'length': len(text),
            'original text': text,
            'translated text': decrypted_text,
        }
    
    if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
