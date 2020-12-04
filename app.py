import os
from sanic import Sanic
from sanic.response import json as json_response
from sanic.exceptions import NotFound
from sanic_motor import BaseModel
from bson import ObjectId

app = Sanic(__name__)

settings = dict(
    MOTOR_URI=os.environ["MONGODB_URL"],
    LOGO=None,
)
app.config.update(settings)

BaseModel.init_app(app)


class Student(BaseModel):
    __coll__ = "students"


@app.route("/", methods=["POST"])
async def create_student(request):
    student = request.json
    student["_id"] = str(ObjectId())

    new_student = await Student.insert_one(student)
    created_student = await Student.find_one(
        {"_id": new_student.inserted_id}, as_raw=True
    )

    return json_response(created_student)


@app.route("/", methods=["GET"])
async def list_students(request):
    students = await Student.find(as_raw=True)
    return json_response(students.objects)


@app.route("/<id>", methods=["GET"])
async def show_student(request, id):
    if (student := await Student.find_one({"_id": id}, as_raw=True)) is not None:
        return json_response(student)

    raise NotFound(f"Student {id} not found")


@app.route("/<id>", methods=["PUT"])
async def update_student(request, id):
    student = request.json
    update_result = await Student.update_one({"_id": id}, {"$set": student})

    if update_result.modified_count == 1:
        if (
            updated_student := await Student.find_one({"_id": id}, as_raw=True)
        ) is not None:
            return json_response(updated_student)

    if (
        existing_student := await Student.find_one({"_id": id}, as_raw=True)
    ) is not None:
        return json_response(existing_student)

    raise NotFound(f"Student {id} not found")


@app.route("/<id>", methods=["DELETE"])
async def delete_student(request, id):
    delete_result = await Student.delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return json_response({}, status=204)

    raise NotFound(f"Student {id} not found")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
