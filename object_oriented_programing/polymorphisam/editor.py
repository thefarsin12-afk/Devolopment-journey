#overriding another method

class Editor:

    def open (self):
     print("editor open method")

class Vscode:

   def open(self):
      print("open method is code .")

vs_instant = Vscode()
vs_instant.open()           