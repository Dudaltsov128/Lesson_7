import datetime

from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docxtpl import DocxTemplate, InlineImage

# source = []

with open('source.txt') as s:
    source = s.read()
    source = source.split('\n')
    print(type(source),source)

def get_context(producer, model, fuel, price): # возвращает словарь аргуменов
    return {
        'producer': producer,
        'model': model,
        'fuel' : fuel,
        'price' : price
    }

def from_template(producer, model, fuel, price, template):
    template = DocxTemplate(template)
    context = get_context(producer, model, fuel, price)  # gets the context used to render the document

    template.render(context)

    template.save(producer + '_' + str(datetime.datetime.now().date()) + '_offer.docx')


def generate_report(producer, model, fuel, price):
    template = 'template.docx'
    from_template(producer, model, fuel, price, template)


# def toFixed(numObj, digits=0):
#     return f"{numObj:.{digits}f}"

generate_report(source[0],source[1],source[2],source[3])