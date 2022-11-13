from docxtpl import DocxTemplate

# experimented with creating a duplicate document and saving this
# this is a way to immediatly duplicate a word doc.

doc = DocxTemplate("Food Recall Alert (BASE DOCUMENT)-v0.0.2.docx")
context = { 'name' : 'Pack_size' }
doc.render(context)
doc.save("allergy_doc.docx")
