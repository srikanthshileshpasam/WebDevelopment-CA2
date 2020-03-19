import pandas as pd
from django.shortcuts import render, get_object_or_404, redirect, reverse
from sklearn.externals import joblib
from .models import Document, MedicalInfo

def home_form(request):
    if request.user.is_authenticated:
        return render(request, "home_form.html")
    else:
        return redirect(reverse('login'))

def home_view(request):
    if request.user.is_authenticated:
        loaded_model = joblib.load("random_forest.pkl")
        age = int(request.POST['age'])
        sex = int(request.POST['sex'])
        cp = int(request.POST['cp'])
        trestbps = int(request.POST['trestbps'])
        chol = int(request.POST['chol'])
        fbs = int(request.POST['fbs'])
        restecg = int(request.POST['restecg'])
        thalach = int(request.POST['thalach'])
        exang = int(request.POST['exang'])
        oldpeak = float(request.POST['oldpeak'])
        slope = int(request.POST['slope'])
        ca = int(request.POST['ca'])
        thal = int(request.POST['thal'])
        MedicalInfo(user=request.user, age=age, sex=sex, cp=cp, trestbps=trestbps, chol=chol, fbs=fbs, restecg=restecg, thalach=thalach, exang=exang, oldpeak=oldpeak, slope=slope, ca=ca, thal=thal).save()
        lst = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        # lst = [44,1,2,130,233,0,1,179,1,0.4,2,0,2] 
        # lst = [52,1,0,125,212,0,1,168,0,1,2,2,2]
        df = pd.DataFrame([lst])
        df.columns =['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']
        result = loaded_model.predict(df)
        csv_file = Document.objects.get(description__icontains="heart")
        print(csv_file.document)
        df = pd.read_csv(csv_file.document)
        # Age histogram
        # Age vs chol scatter plot
        # Chol vs target line chart
        age = list(df['age'])
        age_zero = list(df.query('target==0')['age'])
        age_one = list(df.query('target==1')['age'])
        chol_zero = list(df.query('target==1')['chol'])
        chol_one = list(df.query('target==1')['chol'])
        chol = list(df['chol'])
        target = list(df['target'])
        target1 = target[0:100]
        chol1 = chol[0:100]
        return render(request, "home.html", {
            "age":age,
            "chol":chol,
            "target":target,
            "age_zero":age_zero,
            "age_one":age_one,
            "chol_zero":chol_zero,
            "chol_one":chol_one,
            "result":result[0],
            "target1":target1,
            "chol1":chol1
        })
    else:
        return redirect(reverse('login'))