# def sum_of_cube(func,num1,num2):
#     return func(num1,num2)**3

# def sum(num1,num2):
#     return num1+num2

# s=sum_of_cube(sum,9,8)
# print(s)



# def calculator(oparator):
#     def add(a,b):
#         return a+b
#     def product(a,b):
#         return a*b
#     if oparator=='+':
#         return add
#     if oparator=='*':
#         return product

# s=calculator('*')
# print(s(2,2))


# def calculator(operator,a,b):
#     def sum():
#         return a+b
#     def product():
#         return a*b
#     if operator=='+':
#         return sum
#     if operator=='*':
#         return product

# a=calculator('*',2,2)
# print(a())
# sum=lambda x,y:print(x+y)
# difference=lambda x,y:print(x-y)
# product=lambda x,y:print(x*y)
# a=int(input("enter the first number:"))
# b=int(input("enter the second number:"))
# sum(a,b)
# product(a,b)
# difference(a,b)


#lambda Function

# total = lambda a, b:a+b
# print(total(10,12))

# map()
# filter()

# map(fun,iterables)
# a=[1,2,3,4,5]
# s=[]
# def incerment_by_one(n):
#     return n+1

# output=map(incerment_by_one,a)
# print(list(output))
# output1=map(lambda s:s*s,a)
# print(list(output1))
# name=['ram','shyam','sita','hari']
# output1=map(lambda a: a.capitalize(),name)
# print(list(output1))
# a=[1,2,3,4,5]
# out=list(filter(lambda n:n%2!=0,a))
# print(out)
    

# emails=['1@gmail.com','2@yahoo.com','3@gmail.com','4@outlook.com','5@gmail.com']
# out=list(filter(lambda a:a.endswith('@gmail.com'),emails))
# print(out)

# a=[1,2,3,'ram','apple',5,6,7]
# p=int()
# out=sum(filter(lambda s:isinstance(s,int),a))
# print(out)

#DECORATOR
# def outer(func):
#     def inner():
#         func()
#         print("hello inner")
#     return inner
# @outer
# def welcome():
#     print("welcome everyone:")

# welcome()

# class page:
#     def __init__(self,content,page_number):
#         self.content=content
#         self.page_number=page_number
#     def read(self):
#         print(f"'{self.content}' is contnet of page no{self.page_number}")
#     def print(self):
#         print(f"printing page no:{self.page_number} ")
# class book:
#     def __init__(self,title,pages):
#         self.pages=pages
#         self.title=title
#     def add_page(self,page):
#         self.pages.append()
#     def getcontent(self,page_no):
#         for i in self.pages:
#             if i.page_number==page_no:
#                 return i.content
#     def __str__(self):
#         return self.title
        
# pages=[]
# for i in range(1,6):
#     p=page(f'this is of page number:{i}',i)
#     pages.append(p)
# b=book("math",pages)
# a=b.getcontent(5)
# print(a)
# print(b)


        

        
        
        

    


