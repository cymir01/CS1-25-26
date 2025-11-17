from core import agregar_tarea, listar_tareas
from rich.console import Console
from rich.table import Table

console = Console()
blue_console = Console(style="white on blue")
console.print("--- Gestor de Tareas ---")

while True:  
    cmd = console.input("[bold cyan]Acción (agregar, listar, salir): [/bold cyan]\n")
    if cmd == 'agregar': 
        desc = console.input("Descripción de la tarea: \n") 
        agregar_tarea(desc) 
    elif cmd == 'listar':
        tareas = listar_tareas() 
        if not tareas: 
            console.print("[yellow]No hay tareas.[/yellow]") 
        else:
            table = Table(title="Lista de Tareas") 
            table.add_column("ID", style="cyan") 
            table.add_column("Descripción", style="magenta") 
            table.add_column("Estado", style="green")  
            
            for id, tarea in tareas.items(): 
                table.add_row(str(id), tarea['desc'], tarea['estado'])  
            
            console.print(table)
    elif cmd == 'salir': 
        console.print("Adios") 
        break 
    else:
        console.print("Comando no reconocido\n")
