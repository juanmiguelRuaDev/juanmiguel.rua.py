'''
Created on 10/04/2012

@author: jmrua
'''
import sys
import colorize

def importSpecificLibrary():
    try:
        import termios, TERMIOS
        print 'Su sistema es unix'
    except ImportError:
        try:
            import msvcrt
            print 'su sistema es Windows'
        except ImportError:
            try:
                from EasyDialogs import  AskPassword
                print 'su sistema es macOs'
            except ImportError:
               getpass = "No hay plataforma compatible"
            else:
                getpass = 'Se ha importado AskPassword'
        else: 
            getpass = "Se ha importado msvcrt"
    else:
        getpass = 'Se ha importado termios'
    
    return getpass


                
            
        



if __name__ == "__main__":
    print 'Hello World'
    
    '''Ejemplo de try/catch '''
    print importSpecificLibrary()
    
    '''Ejemplo de llamado a una classe ubicada en otro package'''
    import root.classes.FistClass as fs
    
    f = fs.First()   
    
    print 'la clase obtenida es '+ str(f)
    
    print "La variable privada es igual a : %s " % f.getVariable()
    
    f.setVariable(8)    
    print  'ahora la variable privada es igual a:  '+f.getVariable()
    
    
    
    