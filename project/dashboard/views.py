from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.core.exceptions import ValidationError
from django.views import generic, View
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .utilits.read import read_file
from .forms import LoadForm, UserForm, LoginForm
from .models.auto import Auto
from .models.cliente import Cliente
from .models.contrato import Contrato


class LoginEmailView(LoginView):
   

    form_class = LoginForm
    template_name = 'login.html'
    
    def form_valid(self, form):
        user = form.get_user()
        if user:
            login(self.request, user)
            return redirect('load')
        else:
            return self.form_invalid(form)


class RegistroView(FormView):
   

    template_name = 'registro.html'
    form_class = UserForm
    success_url = reverse_lazy('load') 

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class LogoutView(View):
    
    def get(self, request):
        logout(request)
        return redirect('login')


class LoadView(LoginRequiredMixin, FormView):


    form_class = LoadForm
    template_name = 'load.html' 
    success_url =  reverse_lazy('datos') 

    def form_valid(self, form):
        try:
            read_file(self.request.FILES['file'])
        except ValidationError as e:
            form.add_error(None, e.message)
            return self.form_invalid(form)
        return super().form_valid(form)


class ContratoView(LoginRequiredMixin, generic.ListView):


    model = Contrato
    template_name = 'datos.html'
    context_object_name = 'contratos'
    paginate_by = 20 

    column_names = {
        'nombre': 'Nombres',
        'apellidos': 'Apellidos',
        'num_doc': 'Número de documento',
        'ini_cont': 'Inicio de contrato',
        'cuota': 'Cuota Semanal',
        'marca': 'Marca del auto',
        'modelo': 'Modelo del auto',
        'placa': 'Placa del auto',
    }

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs) 
        print(context.keys())

        all_columns = self.column_names
        columns_names_reversed = {v: k for k, v in self.column_names.items()}
        selected_columns = self.request.session.get('selected_columns', all_columns.values())
        selected_columns_id = {key: columns_names_reversed[key] for key in selected_columns}
        
        row_data = selected_columns_id.values()
        
        # Si no hay columnas seleccionadas, mostrar todas por defecto
        if not selected_columns:
            selected_columns = all_columns.values()
            row_data = all_columns.keys()
            
        
        # Pasar las columnas disponibles, seleccionadas y nombres completos al contexto
        context['available_columns'] = all_columns.values()
        context['selected_columns'] = selected_columns
        context['rows_data'] = row_data

        
        return context

    def post(self, request, *args, **kwargs):


        selected_columns = request.POST.getlist('columns')
        request.session['selected_columns'] = selected_columns  

        if('busqueda' in request.POST.getlist('key') ):
            palabra_buscada = request.POST['busqueda']    
            request.session['busqueda'] = palabra_buscada
            nombre_archivo = request.POST['name_report']    
            request.session['busqueda'] = palabra_buscada
            print(palabra_buscada, nombre_archivo)
        
        
        return redirect(request.path_info) #Redirigir a la misma página para evitar el envio del formulario

   