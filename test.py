try:
    a = "hola"
    b = 5
    print(a/b)
except TypeError:
    print("type error")
except SyntaxError:
    print("syntax error")
except NameError:
    print("name error")
except Exception as e:
    print(e)

  
        
