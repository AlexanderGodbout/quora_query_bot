jupyter nbconvert Business_Model.ipynb  --inplace --execute
jupyter nbconvert Business_Model.ipynb --no-input --to=html
scp Business_Model.html alegod4@www.queryquarry.tech:/home/alegod4/queryquarry.tech
