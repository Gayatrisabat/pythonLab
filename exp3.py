'''
General case represents that developer working on 
frontend cannot work backend development unless he/she is fullstack dev.

Write a method named verifier () that checks this condition.

The method should check that if frontend is True and backend is True,
the method returns Fullstack as string. If one of them is True, it should return
the respective desgination, and if none of them are true, it returns,
not a developer respetively.
'''

class Employee:
    def __init__ (
            self,
            designation : str = 'Developer',
            frontend : bool = False,
            backend : bool = False
    ):
        self.designation = designation
        self.frontend = frontend
        self.backend = backend

    def __repr__ (self):
        return '{}'.format (self.designation, self.frontend, self.backend)
    
    ### Write the your method over here.
    def verifier (self,frontend:bool = False,backend:bool = False):
        
        if self.frontend and self.backend:
            return 'Fullstack Developer'
        elif  self.frontend :
            return 'Frontend Developer'
        elif self.backend:
            return 'Backend Developer' 
        else:
            return 'Not a Developer'
    

if __name__ == '__main__':
    firstEmployee = Employee ()
    frontend = input("Are you a frontend developer? (yes =1 /no=0): ")
    backend = input("Are you a backend developer? (yes =1 /no=0): ")
 
    print (firstEmployee.verifier(frontend,backend))
    

    # Call the method here to display output.
