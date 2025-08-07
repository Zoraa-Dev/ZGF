try:
    from Temporary.ImportD.data import *
    from Manager.Styles import style_terminal
    from Temporary.ImportD.KEY import ZoraaDev
except (ImportError, ValueError) as e: exit(e)

class Main:
    def __init__(self) -> None:
        pass
        
    def ZGF(self):
        try:
            os.system('git pull'); ZoraaDev()
        except (Exception) as e:
            Console(width = 65, style = f"{style_terminal}").print(Panel(f"[grey50]{str(e).title()}", title = f"[white]• [red]Error Not Found [white]•"))
            exit()
            
Main().ZGF()
        
