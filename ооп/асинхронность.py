"""
import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(9)  # Имитация асинхронной задачи (например, ввод-вывод)
    print("Task 1 completed")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 completed")

async def main():
    # Создаем список асинхронных задач
    tasks = [task1(), task2()]

    # Запускаем задачи и ждем их завершения
    await asyncio.gather(*tasks)

# Запуск асинхронной программы
asyncio.run(main())
"""



async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 completed")
    return "Result from Task 1"

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 completed")
    return "Result from Task 2"

async def main():
    tasks = [task1(), task2()]
    results = await asyncio.gather(*tasks)
    print("All tasks completed")
    print("Results:", results)

# Запуск асинхронной программы
"""asyncio.run(main())"""



# Чтобы начать работать с asyncio, вам нужно импортировать модуль и создать цикл событий (event loop). Это основной объект, который управляет асинхронными операциями. Вот простой пример:
import asyncio
async def main():
    print("Hello, asyncio!")
 
# asyncio.run(main())

# Здесь мы определили асинхронную функцию main() и вызвали ее с помощью asyncio.run(). Это основной способ запуска асинхронного кода в Python.

# Асинхронные операции

# Asyncio предоставляет множество асинхронных операций, таких как сопрограммы, задачи, ожидание (awaitables) и многое другое. Вот пример асинхронного ожидания с использованием оператора await:

import asyncio
 
async def foo():
    print("Start foo")
    await asyncio.sleep(1)
    print("End foo")
 
async def main():
    await foo()
 
# asyncio.run(main())

# В этом примере функция foo() выполняет асинхронную операцию asyncio.sleep(), которая заставляет сопрограмму ждать указанное количество секунд. Затем мы используем оператор await для вызова foo() в функции main().

# Работа с несколькими задачами

# Asyncio позволяет выполнять несколько задач одновременно, используя функцию asyncio.gather(). Вот пример с несколькими асинхронными функциями:

async def foo():
    print("Start foo")
    await asyncio.sleep(1)
    print("End foo")
 
async def bar():
    print("Start bar")
    await asyncio.sleep(2)
    print("End bar")
 
"""async def main():
    await asyncio.gather(foo(), bar())
 
asyncio.run(main())"""

# Здесь функции foo() и bar() выполняются параллельно, и программа завершается после выполнения обеих функций.


import asyncio
import time

async def brewCoffe():
    print("Start brewCoffe")
    await asyncio.sleep(3)
    print("End brewCoffe")
    return 'Coffe ready'

async def toastBagel():
    print("Start toastBagel")
    await asyncio.sleep(2)
    print("End toastBagel")
    return 'Bagel ready'

async def main():
    start_time = time.time()

    # batch = asyncio.gather(brewCoffe(), toastBagel())
    # result_coffee, result_bagel = await batch
    
    coffe_task = asyncio.create_task(brewCoffe())
    toast_task = asyncio.create_task(toastBagel())
    result_coffee = await coffe_task
    result_bagel = await toast_task

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Result of BrewCoffee: {result_coffee}")
    print(f"Result of toastBagel: {result_bagel}")
    print(f"Total exution time: {elapsed_time:.2f} seconds")

if __name__=="__main__":
       asyncio.run(main())