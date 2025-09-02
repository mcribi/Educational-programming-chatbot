from .exercises_introduction import exercises_introduction
from .exercises_variables import exercises_variables
from .exercises_conditional import exercises_conditional
from .exercises_loops import exercises_loops
from .exercises_functions import exercises_functions
from .exercises_structures import exercises_structures
from .exercises_vectors import exercises_vectors
from .exercises_matrix import exercises_matrix
from .exercises_class import exercises_class


exercises_by_topic = {
    "Introducción a la programación": exercises_introduction,
    "Variables y tipos de datos": exercises_variables,
    "Condicionales": exercises_conditional, 
    "Bucles": exercises_loops, 
    "Funciones": exercises_functions,
    "Registros": exercises_structures,
    "Vectores": exercises_vectors, 
    "Matrices": exercises_matrix, 
    "Clases": exercises_class
}
