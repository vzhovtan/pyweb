from flask import Flask, request

app = Flask(__name__)

contacts = [
    {"id": "1", "name": "Alice", "phone": "(123)444-55-66"},
    {"id": "2", "name": "Bob", "phone": "(234)555-66-77 "},
    {"id": "3", "name": "Emma", "phone": "(345)666-77-88"},
    {"id": "4", "name": "Danny", "phone": "(456)777-88-99"},
]

@app.route('/hello')
def helloRoute():
    return "<h1>Hello from the REST API server</h1>"


@app.get("/contacts")
def listContacts():
    return contacts


@app.get("/contacts/<id>")
def singleContacts(id):
    for c in contacts:
        if c["id"] == id:
            return c
    return "Contact not found"


@app.post("/contacts")
def createContact():
    next_id = int(contacts[len(contacts) - 1]["id"]) + 1
    new_contact = {
        "id": f'{next_id}',
        "name": request.json["name"],
        "phone": request.json["phone"],
    }
    contacts.append(new_contact)
    return new_contact


@app.put("/contacts/<id>")
def updateContact(id):
    for c in contacts:
        if c["id"] == id:
            c["name"] = request.json["name"] if "name" in request.json else c["name"]
            c["phone"] = request.json["phone"] if "phone" in request.json else c["phone"]
            return c

    return "Contact not found"


@app.delete("/contacts/<id>")
def delContact(id):
    for c in contacts:
        if c["id"] == id:
            contacts.remove(c)
            return c
    return "Contact not found"


if __name__ == "__main__":
    app.run(debug=True)