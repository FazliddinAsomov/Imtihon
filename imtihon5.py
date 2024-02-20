# 1-vazifa

# N soni kiritiladi.Dastlabki N ta Fibonachchi sonlarini chiqarish dasturini yield generatori yordamida yozing

#
# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
# N = int(input("N sonini kiriting: "))
# for num in fibonacci(N):
#     print(num)


# 2-vazifa

# https://tilshunos.com/ommonims/ adresidagi barcha sahifalarni ommonimlar noomli papkaga PDF formatida saqlang.Dastur multithreading yoki multiprocessing dastur bo'lishi kerak


# import pdfkit
# import threading
#
# path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
#
# config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
#
# base_url = 'https://tilshunos.com/ommonims/'
#
# def convert_to_pdf(pages):
#     pdfkit.from_url(base_url + str(pages),
#                     "ommonimlar/" + str(pages) + ".pdf",
#                     configuration=config)
#
#
# threads = []
# for i in range(1, 101):
#     thread = threading.Thread(target=convert_to_pdf, args=(i,))
#     threads.append(thread)
#     thread.start()
#
# for thread in threads:
#     thread.join()
#


# 3-vazifa

# Github
