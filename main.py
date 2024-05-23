import re
from random import choice
from typing import Annotated
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import markdown
from markdownExtension import CustomExtension
from graph import NOTEGRAPH
from fastapi.staticfiles import StaticFiles


app = FastAPI()
templates = Jinja2Templates("templates")
app.mount("/assets", StaticFiles(directory="assets"), name="asset")


def set_connected_nodes(markdown_text, src_note):
    CUSTOM_PATTERN = r"\[\[(.*?)\]\]"
    matches = re.findall(CUSTOM_PATTERN, markdown_text)
    match_counts = {}

    for match in matches:
        match_counts[match] = (
            1 if not match in match_counts else match_counts[match] + 1
        )

    for note in match_counts:
        dest_note = NOTEGRAPH.getNoteByTitle(note)
        if dest_note:
            NOTEGRAPH.addConnection(src_note, dest_note, match_counts[note])


@app.on_event("startup")
async def startup_event():
    notes = NOTEGRAPH.getVertices()
    for entry in notes:
        set_connected_nodes(entry.note_value, entry)


@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    # This will return the original template
    return templates.TemplateResponse(
        "index.html", {"request": request, "notes": NOTEGRAPH.getVertices()}
    )


@app.post("/process-markdown", response_class=HTMLResponse)
async def render(
    request: Request,
    markdownText: Annotated[str, Form()],
    noteID: Annotated[str, Form()],
):
    NOTE = NOTEGRAPH.getNoteByID(noteID)
    if NOTE:
        NOTE.note_value = markdownText
        set_connected_nodes(markdownText, NOTE)

    return templates.TemplateResponse(
        "snippets/processed.html",
        {
            "request": request,
            "RENDERED": markdown.markdown(markdownText, extensions=[CustomExtension()]),
            "VERTICES": NOTEGRAPH.getConnected(NOTE),
        },
    )


@app.get("/note/", response_class=HTMLResponse)
async def getNote(request: Request, noteID: str):
    note = NOTEGRAPH.getNoteByID(noteID)
    if note:
        return templates.TemplateResponse(
            "snippets/textarea.html",
            {
                "request": request,
                "MARKDOWN": note.getValue(),
                "ID": note.getId(),
                "RENDERED": markdown.markdown(
                    note.getValue(), extensions=[CustomExtension()]
                ),
                "VERTICES": NOTEGRAPH.getConnected(note),
            },
        )


@app.get("/viz/", response_class=HTMLResponse)
async def getViz(request: Request):
    url = NOTEGRAPH.generate_visualisations()
    return templates.TemplateResponse(
        "snippets/graph.html", {"request": request, "imgpath": url}
    )


@app.post("/create-note/", response_class=HTMLResponse)
async def create_a_note(request: Request, TITLE: Annotated[str, Form()]):
    word_list = [
        "apple",
        "book",
        "desk",
        "pen",
        "cat",
        "dog",
        "tree",
        "house",
        "car",
        "phone",
        "computer",
        "laptop",
        "keyboard",
        "mouse",
        "chair",
        "table",
        "door",
        "window",
        "wall",
        "floor",
    ]  # 20*20*20 = 8000 unique

    while True:
        name = f"{choice(word_list)}-{choice(word_list)}-{choice(word_list)}"
        if TITLE != "RANDOM":
            name = TITLE
        note = NOTEGRAPH.getNoteByTitle(name)
        if not note:
            NOTEGRAPH.addNote(name)
            return templates.TemplateResponse(
                "snippets/notelink.html",
                {"request": request, "note": NOTEGRAPH.getNoteByTitle(name)},
            )
