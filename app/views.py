from app import app
from flask import redirect, render_template, request


# every route needs a forward slash at the beginning.
@app.route("/")
# writing a function called index
def index():
    # return "allergy warning"
    # I now return render_template and inside will be the specific html file I want to render from.
    # provide it a path now it is in a public folder.
    return render_template("public/index.html")

# asking the route of about to return a h1 HTML tag with styling.
@app.route("/about")
    # writing a function called about
def about():
        return "<h1 style='color: red'>Food Recall Allergy</h1>"

# creating a new route named jinja2

@app.route("/jinja2")
def jinja2():

    # Crisp Company Limited, Salted Crisps - Use by dates: 18 December 2024 and 1 February 2025
    # Al's Fancy Hummus, Light Hummus - Use by dates: 18 November 2021, 1 February 2022, 9 February 2022
    # Babyco Turbo Baby Formula - Best before date: 18 March 2023

    # use_by_dates = {
    #     "Crisp Company Limited, Salted Crisps": {18/12/2024, 1/2/2025}

    # }


    types_contamination_recall = ['lead', 'peanut', ' egg']
    # passing in a Python Object
    name_of_product = "Babyco Turbo Baby Formula"
    # pass this object in a key value pair
    # the form template will have full access to the object.
    return render_template("public/jinja2.html", name_of_product=name_of_product, types_contamination_recall=types_contamination_recall)


# Dictionary created to store particular data needed

allergy_alert = {
    "Crisp Company Limited, Salted Crisp": {
        "allergy": "egg",
        "use_by_date": {
            "date 1": "18/12/2024",
            "date 2": "01/02/2025",
        },
        "pack_size": {
            "size 1": "30g",
            "size 2": "50g",
        },
        "batch_codes": {
            "code 1": "321B",
            "code 2": "122C",
        },
    },
    "Al's Fancy Hummus, Light Hummus": {
        "allergy": "peanut",
        "use_by_date": {
            "date 1": "18/11/2021",
            "date 2": "01/02/2022",
            "date 3": "09/02/2022",
        },
        "pack_size": {
            "size 1": "100g",
            "size 2": "150g",
            "size 3": "200g",
        },
        "batch_codes": {
            "code 1": "321B",
            "code 2": "122C",
            "code 3": "426C",
        },
    },
    "Babyco Turbo Baby Formula": {
        "allergy": "lead",
        "use_by_date": {
            "date 1": "18/03/2023",
        },
        "pack_size": {
            "size 1": "500g",
        },
        "batch_codes": {
            "code 1": "1234-A",
        },
    },
}

@app.route("/doc_template/<business_name>")
def document_info(business_name):

        business_product = None


        if business_name in allergy_alert:
# print(allergy_alert[business_name])
         business_product = allergy_alert[business_name]
        return render_template("public/doc_template.html", business_name=business_name, business_product=business_product)

@app.route("/insert-data", methods=["GET", "POST"])
def insert_data(self, business_product):

    # now a bit of validation to say that we only want the code thats in the if statement.
    # and run when the method is post.

    if request.method == 'POST':

        # to access the form data I will want to request it.
        # this will show it as a dictionary object of data
        # store it in a variable called req
        req = request.form

        print(req)

        business_name = req.get("business_name")
        food_allergy = req.get("food_allergy")
        use_by_date = req.get("use_by_date")
        pack_size = req.get("pack_size")
        batch_codes = req.get("batch_codes")

        print(business_name, food_allergy, use_by_date, pack_size, batch_codes)
        # business_name = allergy_alert[business_name]
        # nonlocal business_product
        print(self.business_product)
        if not business_name in allergy_alert:
          print("Product name not found")
        return redirect(request.url)
    else:
        self.business_product = allergy_alert[business_name]

    if not food_allergy in allergy_alert:
        print("This is not a correct allergy")
    return redirect(request.url)
    return render_template("public/form_data.html")


#     else:
#     business_product = allergy_alert["business_name"]
#     return redirect(url_for("/doc_template"))

# if not pack_size in allergy_alert:
#         print("This is not a correct allergy")
#     return redirect(request.url)
#     else:
#     business_product = allergy_alert["business_name"]
#     return redirect(url_for("/doc_template"))

# if not food_allergy in allergy_alert:
#         print("This is not a correct allergy")
#     return redirect(request.url)

# if not food_allergy in allergy_alert:
#         print("This is not a correct allergy")
#     return redirect(request.url)

