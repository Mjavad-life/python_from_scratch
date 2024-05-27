# in barnameh 2 adad ra migirad va anha ra taghsim mikonad
# agar be jaye adad , harf vared shavad elam khata mikonad

aval = input(" adade aval ra benevisid :")
dovom = input(" adade dovom ra benevisid :")

try :
    adadeaval = int(aval)
    adadedovom = int(dovom)
    taghsim = adadeaval / adadedovom
    print (taghsim)
except ValueError :
    pass