import os
import importlib.util
from src.topic import Topic  
from src.lesson import Lesson

TOPIC_NAMES = {
    "introduction": "Introducción a la programación",
    "variables": "Variables y tipos de datos",
    "conditional": "Condicionales",
    "loops": "Bucles",
    "functions": "Funciones",
    "input_output": "Entrada y salida",
    "vectors": "Vectores"
}

def load_theory():
    base_path = os.path.join(os.path.dirname(__file__), "theory")
    topics = {}

    for folder in os.listdir(base_path):
        topic_path = os.path.join(base_path, folder)
        if os.path.isdir(topic_path):
            lessons = []
            for file in sorted(os.listdir(topic_path)):
                if file.endswith(".py"):
                    filepath = os.path.join(topic_path, file)
                    spec = importlib.util.spec_from_file_location("lesson_module", filepath)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    lesson = module.lesson  
                    lessons.append(lesson)

            topic_name = TOPIC_NAMES.get(folder, folder.replace("_", " ").capitalize())
            topics[topic_name] = Topic(name=topic_name, lessons=lessons)

    return topics
