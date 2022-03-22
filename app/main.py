# main project file. contains all functions and API/web routes for the application.
# utilizes Numpy to interpolate coverage values.

# ? notes: might switch to underscores instead of camelCase. Not 100% sure yet.

from flask import Blueprint, jsonify, request, render_template, abort
import numpy

from . import factors # import rate factors


# Flask blueprint for init
main = Blueprint("main", __name__)

# calculate and return the final quoted premium amount.
def GetFinalQuotedPremiumAmount(customer):
    finalQuotedPremiumAmount = factors.basePremium * InterpolateCoverage(customer["DwellingCoverage"]) * GetHomeAge(customer["HomeAge"]) * factors.RoofType[customer["RoofType"]] * factors.NumUnits[customer["NumberOfUnits"]]

    # check if partner discount is applied and return the final (rounded) quote in string format.
    return str(round(finalQuotedPremiumAmount if customer["PartnerDiscount"].upper() != "Y" else finalQuotedPremiumAmount * .95))

# leverages numpy to interpolate between dwelling coverage values.
def InterpolateCoverage(dwellingCoverage):
    coverage = numpy.interp(dwellingCoverage, list(factors.DwellingCoverage.keys()), list(factors.DwellingCoverage.values()))
    return coverage

# calculate HomeAge factor.  
def GetHomeAge(homeAge):
    for i in range(len(factors.HomeAge)):
        if i == len(factors.HomeAge) - 1:
            return factors.HomeAge[i][1]
        if homeAge > factors.HomeAge[i][0] and homeAge < factors.HomeAge[i + 1][0]:
            return factors.HomeAge[i][1]

# validate request data.
def ValidateRequest(request):
    if not str(request["CustomerID"]).isnumeric():
        return False
    if not str(request["DwellingCoverage"]).isnumeric():
        return False
    if not str(request["HomeAge"]).isnumeric():
        return False
    if not str(request["NumberOfUnits"]).isnumeric():
        return False
    if request["RoofType"] not in factors.RoofType:
        return False
    if request["PartnerDiscount"] not in ("Y", "N"):
        return False
    return True

# Quote API / web results
# Handles POST requests and returns the quoted monthly premium amount in JSON format or to the Flask template. 
@main.route("/quote", methods=["POST"])
def QuotePremium():
    customerRequest = request.get_json() # gets JSON data.

    # for our Flask app HTML template form handling.
    if customerRequest is None :
        customerRequest = {
            "CustomerID": int(request.form["CustomerID"]),
            "DwellingCoverage": int(request.form["DwellingCoverage"]),
            "HomeAge": int(request.form["HomeAge"]),
            "RoofType": request.form["RoofType"],
            "NumberOfUnits": int(request.form["NumberOfUnits"]),
            "PartnerDiscount": request.form["PartnerDiscount"]
        }
        # validate and return quoted amount to the HTML template.
        if not ValidateRequest(customerRequest):
            abort(400)
        return render_template("result.html", quote = GetFinalQuotedPremiumAmount(customerRequest))

    # validate and return quoted amount in JSON format.
    if not ValidateRequest(customerRequest):
        abort(400)
    return {
            "FinalQuotedPremiumAmount" : GetFinalQuotedPremiumAmount(customerRequest)
        } 

#  web index / customer input form
@main.route("/", methods=["GET"])
def Index():
    return render_template("form.html")
