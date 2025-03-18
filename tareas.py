from collections import deque

# Definir el grafo de tareas como un diccionario, donde cada tarea tiene una lista de subtareas
# que dependen de ella.
task_dependencies = {
    'Tareas de la casa': ['Tarea de limpieza', 'Tarea de cocina', 'Tarea de limpieza de cocina'],
    'Tarea de limpieza': ['Tarea de limpieza de cocina','Pasar el aspirador' ],
    'Tarea de cocina': ['Hacer la comida', 'Poner la mesa', 'Lavar los platos'],
    'Tarea de limpieza de cocina': ['Poner el lavavajillas'],
    'Pasar el aspirador': [],
    'Hacer la comida': [],
    'Poner la mesa': [],
    'Lavar los platos': [],
    'Poner el lavavajillas': []

}

def find_task_completion_order(task_dependencies, start_task):
    """
    Función para encontrar el orden de completitud de tareas usando BFS.
    """
    # Cola para realizar el recorrido BFS
    task_queue = deque([start_task])
    # Conjunto para llevar un registro de las tareas visitadas
    visited_tasks = set()
    # Lista para almacenar el orden de completitud de las tareas
    task_completion_order = []

    while task_queue:
        # Extraer la tarea en el frente de la cola
        current_task = task_queue.popleft()
        # Si la tarea no ha sido visitada, la procesamos
        if current_task not in visited_tasks:
            # Marcar la tarea como visitada
            visited_tasks.add(current_task)
            # Añadir la tarea al orden de completitud
            task_completion_order.append(current_task)
            # Añadir las subtareas a la cola
            for dependent_task in task_dependencies[current_task]:
                if dependent_task not in visited_tasks:
                    task_queue.append(dependent_task)

    return task_completion_order

# Buscar el orden de completitud comenzando desde la Tarea A
start_task = 'Tareas de la casa'
completion_order = find_task_completion_order(task_dependencies, start_task)
print("Orden de completitud de las tareas:", completion_order)
