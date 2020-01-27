
from django.test import TestCase

# Create your tests here.


#https://www.geeksforgeeks.org/textfield-django-models/
#https://realpython.com/django-redirects/#passing-parameters-with-redirects
#https://www.w3schools.com/css/css_table.asp

#pip3 install django-crispy-forms

#Zerar senha do admin
#python manage.py shell
#from django.contrib.auth.models import User
#User.objects.filter(is_superuser=True)

#usr = User.objects.get(username='nome-do-administrador')
#usr.set_password('nova-senha')
#usr.save()



'''Upload documents on Github
git clone <nome>
<entra na pasta criada>
git add .
git commit -m "texto"
git push
git pull
'''

'''git checkout -b nome cria uma branch
git checkout nome entra na branch
git branch - verifica as branchs
git checkout master - entra na master
git merge origin "nome" 
git push origin master - subir commit
git branch -D "nome"- deletar branch
'''



#Heroku
#https://github.com/Gpzim98/django-heroku

#git add .gitignore
#colocar no gitignore
'''.idea
.pyc
.DS_Store
*.sqlite3'''

'''
Publishing the app
git add .
git commit -m "Configuring the app"
git push heroku master --force
'''


#------

'''

def newTask(request):


    if request.method == 'POST':
        form = ResidencDimensForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.total_va = (task.potencia_va * task.quant)
            task.corrente_a = (task.total_va / task.tensa_va)

            #queda = task.sessao_condutor
            #test = main.read_sql_queda(queda)

            #task.queda_tensao_ckt = ((((test['queda_tesao'] * task.corrente_a) * task.comprimento) / 1000) / task.total_va)

            task.save()

            return redirect('/')

    else:
        form = ResidencDimensForm()
        return render(request, 'cable/add-task.html', {'form': form})


'''

#urls ID
#https://stackoverflow.com/questions/15608295/passing-an-id-in-django-url



#===============================================
'''

@login_required
def newTask(request):

    if request.method == 'POST':
        form = ResidencDimensForm(request.POST)
        #conductor = TabelaCondutor.objects.all()
        #print('----------->', conductor[0])

        task = form.save(commit=False)
        task.sessao_condutor = '10'

        if form.is_valid():

            task = form.save(commit=False)
            task.total_va = (task.potencia_va * task.quant)
            #--------------------------------------------------

            print(task.sessao_condutor)

            t_va = float(task.total_va)

            task.corrente_a = (float(task.total_va) / t_va)
            #--------------------------------------------------
            queda = task.sessao_condutor
            test = main.read_sql_queda(queda)
            queda_tensao = test['queda_tesao'][0]

            calc = ((((float(queda_tensao) * float(task.corrente_a)) * float(task.comprimento)) / (1000) / t_va))

            task.queda_tensao_ckt = calc * 100
            
            if (float(task.queda_tensao_perm) / 100)< task.queda_tensao_ckt:
                task.queda_tensao_test = 'OK'
            else:
                task.queda_tensao_test = 'NÃO'
            #--------------------------------------------------

            corr = task.sessao_condutor
            test = main.read_sql_corr(corr)
            corrente = test['capacidade_conducao'][0]

            if corrente > float(task.corrente_a):
                task.capacidade_corrente = 'OK'
            else:
                task.capacidade_corrente = 'NÀO'
            #--------------------------------------------------
            dj = task.corrente_nominal
            test = main.read_sql_dj(dj)
            djj = int(test['dj'][0])

            if djj > (float(task.corrente_a) * 1.1):
                task.verifica_dj = 'OK'
            else:
                task.verifica_dj = 'NÀO'

            #--------------------------------------------------
            id_x = task.projeto
            test = main.read_sql_filter_id(id_x)
            id_project = int(test['id'][0])
            #--------------------------------------------------

            cable = main.table_tens(float(task.total_va), task.tensa_va)

            print('\n\n')
            print(cable)
            print('\n\n')

            task.sessao_condutor = cable

            print(task.sessao_condutor)

            task.save()

            link = '/tasklist'

            url = '{}/{}'.format(link, id_project)
            return redirect(url)

    else:
        form = ResidencDimensForm()
        return render(request, 'cable/add-task.html', {'form': form})


'''