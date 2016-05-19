Python Training Notes
---------------------------------
This document is a compilation of notes for Python Classroom training, that i attended recently.
The training was really good and give good kick-start to python scripting language.


General Notes
------------------------
 1. Python is an interpretted language. Just like JavaScript, a python script consists of commands that can be run by interpreter without need a compilation phase.
 2. Python removes all the extra overhead of learning the concepts before starting the actual code like "static", "void" "main". It is purely object-oriented language. Everything in Python is an object.
 3. There are two types of classes in Python:
    
    1. *Immutable Classes*
       
       Ones whose objects cannot be modified after instantiating. 
       `int, long, string, float, bool, tuple, complex, None` are immutable ones.
       
    2. *Mutable Classes*
    
        Ones whose objects can be modified aftestar instantiation. `list, dict, bytearray, set` are examples of mutable classes in Python.

 4. Every object in Python is referred by a reference. The reference is stored on Stack and the object is created on heap. Since the objects are immutable, hence objects are unique in data pool.
 
 5. For the given code statement:
        
        a= 10
       
    Python defines `a` in memory which refer to an object `10` in heap. `a` is of type `int` given at runtime. For C programmers, `a` is pointer to a constant value. 
    
 6. An array takes around 20 bytes in memory. When `a` is created, a block is reserved in heap, which stores the value=10, type=int, base=10, reference count=1, GC info.
 
 7. For the following statements:

        a = 10
        b = a
        c = 10
    10 is an object on heap which is referred by three variables on stack. The reference count of 10 is 3. Python performs the shallow copy, There is no deep copy in python.
    
 8. A python code is compiled at runtime into bytecode and then interpretted at runtime by the interpreter.
 9. Python can support following types of programming styles:
 
    1. Object Oriented Programming
    2. Procedural Programming
    3. Functional Programming

 10. There are different implementations of Python exists:
    1. CPython (95% of the market)
    2. Jython  (5%)
    3. iPython  ~1%
    4. Stackless Python (research project)
    5. PyPy  (research project)
 11. There are two versions of Python:
    1. Python 2.x
    2. Python 3.x
 12. Python works in two modes: Interpreter mode and Script Mode. You can write commands directly on interpreter.     Or just open IDLE create a new script file and run it from there.
 13. There are some global module functions available in Python for use with any object:
    1. `id(a)` - gives address of the variable.
    2. `type(a)` - gives the type of the variable.
    3. `min(x)` - gives the min of the structure.
    4. `max(x)` - gives the max of the structure.
    5. `sum(x)` - gives the sum of the structure.
    6. `len(a)` - length of a given structure.
    7. `dir(a)` - gives all the member functions and data members of the variable.
    8. `repr(a)` - gives the string representation of variable using " ".
    9. `str()` - casts into string.
    10. `int()` - cast into int.
    11. `long()` - cast into long.
    
 14. `int` and `float` are two data structures which are not iterable.
 15. The input-output operations in python are performed using input() and print statements.

         val = input('read a value from the console:')
         print('the value is ', val)
    
    The input is always read in String format. Cast into the right format before processing.
    The output can be written in multiple formats. Concatenate string form, C-style % form, {0}, {1} form and comma seperated form.
    
 16. During the study of basic data structures in Python, we will find a common format. All data structure kind of support similar APIs. So if we learn one, we can master mostly all, with some exceptions in their APIs.
 
 
 String
 ----------------
  1. Let us start the next set of discussion with data structures in Python language. By studying one or two data structures in depth, we can pickup the flavor of the style that python programming exhibits.
  
  2. A String object is just like an zero-indexed array of characters in any other language. A string can be represented as:
        
         a = 'sample data'
         b = "Hello World!"
         
         a[0] is 's'
         len(a) is length of any data structure, except int.
         
  3. Picking out a part of a string or any data structure in Python is called slicing. For this you can use bracekt notation instead of calling functions like in other languages.
  
          a[start:end:interval]
          a[0:4:]  # substring of length 3 is returned. (start to end-1)
          a[::]    # returns complete string
          a[::2]   # returns alternate character starting from 0
          a[1::2]  # returns alternate character string from 1
          a[-1]    # returns the last character of the string. -ve index starts from end of the string.
          a[::-1]  # reverse the string
          a[-1:]   # reverse the string
  4. Iteration in string is performed using `in` operator
  
           name = 'ashish'
           for ch in name:
            print(ch.upper())
  5. There are other useful methods in String class: `index(), rindex(), find(), count()., startswith(), endswith(), lower(), replace() upper(), isdigit(), isnumeric(), split(), strip()` etc. The string is immutable, that's why these methods create a new string object.
  6. `split()` divides the string based on the given delimiter into a list:
             
            name = 'ashish'
            n = name.split('h') 
            print(n)   # prints out ['as','is', '']
            
  7. String is a immutable iterable data structure, which can be sorted using global functions: `sorted()` and `reversed()`.
  

Data Structures
-------------------------
_Lists/Dict/Set/Tuple_

 1. A list can be defined as:
 
            a = []      // creates an empty list
            a = [i*i for i in range(5)] // creates a list of 5 elements.
 2. Mutable data structures are only deepcopied to perform sorting/reversed otherwise they will modify the original copy. 
 
            a = [1,5,2,3,52,6]
            temp= a[:] //copying the list, deep copy
            res = sorted(temp)
            res = reversed(temp)
3. Some standard APIs in every python data structure is: `append(), extend(), insert(i,x), remove(x), pop(),clear(), count(), sort(), reverse(), copy()`.
4. Every data structure in Python can exhibit following properties:
    1. Iterable
    2. Indexable
    3. Ennumerable
    4. Immutable/mutable
    5. Slicing-able

