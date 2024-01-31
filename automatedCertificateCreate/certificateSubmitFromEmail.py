from docx import Document
from docx.shared import Pt
from openpyxl import load_workbook
import win32com.client as win32

openOutlook = win32.Dispatch('outlook.application')

#Pegando o arquivo do Excel
studentsExcelArchive = 'DadosAlunosEmail.xlsx'

#Pegando a planilha dos alunos
studentsSheet = load_workbook(studentsExcelArchive)

#Selecionando a aba da planilha
sheetSelected = studentsSheet['Nomes']

#fazendo um for da segunda linha até o quantidade de itens da Coluna A
for lineName in range(2, len(sheetSelected["A"]) + 1) :

    #abrindo o arquivo word de certificado padrão
    wordDocument = Document('certified1.docx')
    styleDocument = wordDocument.styles["Normal"]

    #o %s converte o item da coluna para string/texto de linha por linha e transformando em valor
    studentName = sheetSelected['A%s' % lineName].value
    doneDay = sheetSelected['B%s' % lineName].value
    doneMonth = sheetSelected['C%s' % lineName].value
    doneYear = sheetSelected['D%s' % lineName].value
    studentCourse = sheetSelected['E%s' % lineName].value
    studentInstructor = sheetSelected['F%s' % lineName].value
    studentEmail = sheetSelected['G%s' % lineName].value

    for paragraph in wordDocument.paragraphs :
        if "@nome" in paragraph.text :
            paragraph.text = studentName
            font = styleDocument.font
            font.name = 'Agency FB'
            font.size = Pt(23)

        firstParagraph = 'Concluiu com sucesso o curso de'
        secondParagraph = 'com a carga horária de 20 horas, promovido pela escola de Cursos Online'
        studentsParagraph = f'{firstParagraph} {studentCourse} {secondParagraph} em {doneDay}/{doneMonth}/{doneYear}'

        if 'escola' in paragraph.text :
            paragraph.text = studentsParagraph
            font = styleDocument.font
            font.name = 'Agency FB'
            font.size = Pt(23)

        if 'Instrutor' in paragraph.text :
            paragraph.text = f'{studentInstructor} - Instrutor(a) do Curso'

    wordDocument.save(f'Certificado {studentName}.docx')

    outlookEmail = openOutlook.CreateItem(0)
    outlookEmail.To = studentEmail
    outlookEmail.Subject = f'{studentCourse} Certified'
    outlookEmail.HTMLBody = (f'<p>Boa tarde, {studentName},<p>'
                             f'<p>Segue em anexo o seu Certificado de {studentCourse}.<p>'
                             f'<p>Atenciosamente,'
                             f'<p>Vitor Vargem.<p>')
    
    outlookEmail.Attachments.Add(f'C:\\Users\\vitor.vargem\\PycharmProjects\\AutomationProjects\\automatingWordDocuments\\Certificado {studentName}.docx')

    outlookEmail.Send()
