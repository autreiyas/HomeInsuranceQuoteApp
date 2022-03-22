from flask import Blueprint, jsonify, request, render_template, abort
from . import factors
import numpy

main = Blueprint('main', __name__)

# customer request data class
def FinalQuotedPremiumAmount(c):
    finalQuotedPremiumAmount = factors.basePremium * InterpolateCoverage(c["DwellingCoverage"]) * GetHomeAge(c["HomeAge"]) * factors.RoofType[c["RoofType"]] * factors.NumUnits[c["NumberOfUnits"]]

    return str(round(finalQuotedPremiumAmount if c["PartnerDiscount"].upper() != "Y" else finalQuotedPremiumAmount * .95))

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

# quote API route
@main.route('/quote', methods=["POST"])
def QuotePremium():
    c = request.get_json()
    if c is None :
        c = {
            "CustomerID": int(request.form["CustomerID"]),
            "DwellingCoverage": int(request.form["DwellingCoverage"]),
            "HomeAge": int(request.form["HomeAge"]),
            "RoofType": request.form["RoofType"],
            "NumberOfUnits": int(request.form["NumberOfUnits"]),
            "PartnerDiscount": request.form["PartnerDiscount"]
        }
        if not ValidateRequest(c):
            abort(400)
        return render_template('result.html', quote = FinalQuotedPremiumAmount(c))
    if not ValidateRequest(c):
        abort(400)
    return {"result":FinalQuotedPremiumAmount(c)}

#  web index
@main.route('/', methods=["GET"])
def index():
    return render_template('form.html')
