


from lec07_클래스_python import add
son = add(4, 5)
print("받았음", son)

from lec07_클래스_python import add
son = add(4, 5)
print("받았음", son)

import lec07_클래스_python
son = lec07_클래스_python.add(4, 5)
print("받았음", son)

import lec07_클래스_python as aa
son = aa.add(4,5)
print("받았음", son)

#...................................................................

from lec07_클래스_python import PhoneBook
pb = PhoneBook(55)
print(pb)

a = pb.addc( 5, 3)
print(a)

PhoneBook.loginc("홍긴동")

pb.login22('홍긴동')

pb.loginc33("홍긴동")

a=pb.loginc33("홍긴동")
print(f"{a}님 로그인")
