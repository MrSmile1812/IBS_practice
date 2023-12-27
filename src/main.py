import pandas as pd
from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import List
from database.base import tasks
from task_1.validator import validate_csv_data, validate_csv_file
from task_2.data_filter import find_in_different_registers


app = FastAPI()


# task_1
@app.post("/average_age_by_position")
def avg_age_by_posotion(file: UploadFile = File(...)) -> dict:
    """Функция по обработке csv файла и
    получению среднего возраста по каждой должности"""

    employee_data = pd.read_csv(
        file.file,
        encoding="utf-8",
        delimiter=","
    )

    if validate_csv_data(employee_data) and validate_csv_file(file.filename):
        employee_dict = employee_data.groupby(
            "Должность"
        )["Возраст"].mean().to_dict()

        return {"status": 200, "data": employee_dict}
    else:
        raise HTTPException(status_code=400, detail="Невалидный файл")


# task_2
@app.post("/find_in_different_registers", response_model=List[str])
async def get_unique_words(words: List[str]) -> list:
    result = find_in_different_registers(words)
    return result


# task_3
@app.get("/tasks")
def get_all() -> list:
    return tasks


@app.get("/tasks/{task_id}")
def get_one(task_id: int) -> list:
    res = [task for task in tasks if task.get("task_id") == task_id]
    if not res:
        raise HTTPException(status_code=404, detail="task not found")
    return res


@app.put("/tasks")
def add_task(task: str, status: bool = False) -> dict:
    tasks.append(
        {
            "task_id": len(tasks) + 1,
            "task": task,
            "status": status
        }
    )
    return {"status": 200, "data": tasks[-1]}


@app.post("/tasks/{task_id}")
def update(task_id: int, new_status: bool) -> dict:
    try:
        current_task = list(filter(
            lambda task: task.get("task_id") == task_id, tasks
        ))[0]
        current_task["status"] = new_status
        return {"status": 200, "data": current_task}
    except Exception:
        return {"status code": 404, "info": "task not found"}


@app.delete("/tasks/{task_id}")
def delete(task_id: int) -> dict:
    try:
        tasks.pop(task_id - 1)
        return {"status code": 200}
    except Exception:
        return {"status code": 404, "info": "task not found"}


# task_8
@app.get("/int_to_roman")
def int_to_roman(number: int) -> str:
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    res = ''
    while number:
        digit = number // num[i]
        number %= num[i]
        while digit:
            print(sym[i], end="")
            res += sym[i]
            digit -= 1
        i -= 1
    return res
