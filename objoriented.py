# """
# 1. class and object
# 2.  inheritance:

# 3. polymorphism
#     - method overriding
# 4.abstraction :pyhsically non-exixtancial things will be implemneted in the code.


# 1. class
#     it is concept , actually physical /blueprint ,the template,blueprint that cary the features
# 2. Object 
#     it is the physical representation of the class.
# ""
# class car:  #behavor and property
#             #inittialiser function
#     def __init__(self,model,color):
#         self.m=model
#         self.c=color
# c=car('2022','black')
# print(c.m)
# print(c.c)

class page:
    def __init__(self,pages_number,pages_content):
        self.page=pages_number
        self.content=pages_content
    def read(self):
        print(f"reading {self.content}  of page number:{self.page}")
    def print(self):
        print(f"printing {self.page}")
    def __repr__(self):
        return self.content
        
    @staticmethod
    def printing_out_of_the_content(content):
        print(f"printing {content}")
    

# p=page(12,'hello')
# p.read()
# p.printing_out_of_the_content('hello evry one:')
# class book:
#     def __init__(self,tittle,pages):
#         self.tittle=tittle
#         self.pages=pages
#     def number_of_pages(self):
#         return len(self.pages)
#     def add_pages(self,page):
#         self.pages.append(page)
#     def __str__(self) -> str:#it generally gives the information about the class
#         return(self.tittle)
#     def get_content(self,page_numeber):
#         for i in self.pages:
#             if i.page==page_numeber:
#                 return i.content
#         else:
#             print("not found:")


# pages=[]
# for i in range(1,6):
#     p=page(i,f"paragraph number:{i}")
#     pages.append(p)
# b=book("math",pages)
# print(f"the number of pages is:{b.number_of_pages()}")
# p=page('2',"this is new pages:")
# b.add_pages(p)
# print(f"the numebr of pages is {b.number_of_pages()}")
# print("all the book content are:")
# for i in pages:
#     i.read()
# print(b)
# print(b.pages)
# print(b.__dict__)
# print(b.get_content(4))

#Exception Handling:
# try:
#     n1=int(input("enter the number1:"))
#     n2=int(input("enter the number2:"))
# except ValueError:
#     print("cannnot convert to interger")
# except NameError:
#     print("variable not defined")
# else:
#     print(n1+n2)



        


        




