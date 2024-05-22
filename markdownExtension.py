from markdown.treeprocessors import Treeprocessor
from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension
import xml.etree.ElementTree as etree
from graph import NOTEGRAPH


# Custom InlineProcessor to handle [[dogorcats]] pattern
class CustomInlineProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        el = etree.Element("span")
        el.text = m.group(1)
        note = NOTEGRAPH.getNoteByTitle(el.text)
        if note:
            el.set("class", "text-indigo-400 hover:cursor-pointer")
            el.set("hx-vals", '{"noteID": "' + str(note.getId()) + '"}')
            el.set("hx-get", "/note")
            el.set("hx-trigger", "click")
            el.set("hx-swap", "innerHTML")
            el.set("hx-target", "#note-editor")
        else:
            el.set("class", "text-red-400 hover:cursor-pointer")
            el.set("hx-vals", '{"TITLE": "' + str(el.text) + '"}')
            el.set("hx-post", "/create-note")
            el.set("hx-trigger", "click")
            el.set("hx-swap", "beforebegin")
            el.set("hx-target", "#NEWNOTEBUTTON")

        return el, m.start(0), m.end(0)


class TailwindProcessor(Treeprocessor):
    def __init__(self, md) -> None:
        super().__init__(md)

    def run(self, root):
        for e in root:
            if e.tag == "h1":
                e.set("class", "text-4xl")
            if e.tag == "h2":
                e.set("class", "text-3xl")
            if e.tag == "h3":
                e.set("class", "text-2xl")
            if e.tag == "h4":
                e.set("class", "text-xl")
            if e.tag == "h5":
                e.set("class", "text-xl")
            if e.tag == "h6":
                e.set("class", "text-xl")
            if e.tag == "ul":
                e.set("class", "list-disc list-inside")
                e.append(etree.Element("br"))
            if e.tag == "ol":
                e.set("class", "list-decimal list-inside")
                e.append(etree.Element("br"))
        return root


# Extension that adds the custom pattern
class CustomExtension(Extension):
    def extendMarkdown(self, md):
        CUSTOM_PATTERN = r"\[\[(.*?)\]\]"  # Regex pattern to match [[dogorcats]]
        md.inlinePatterns.register(
            CustomInlineProcessor(CUSTOM_PATTERN, md), "custompattern", 1
        )
        md.treeprocessors.register(TailwindProcessor(md), "tailwind", 2)
