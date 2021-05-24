
import pyttsx3
import PyPDF2

pdf_book = open('THE FALLING OF THE LEAVES.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_book)
num_pages_counter = pdf_reader.numPages

play = pyttsx3.init()
print('Playing Audio Book from pdf')

for num in range(0, num_pages_counter):
	page = pdf_reader.getPage(num)
	data = page.extractText()

	play.say(data)
	play.runAndWait()

print('Book is Finished, Thank you!')

## contributed by Amresh Ranjan.