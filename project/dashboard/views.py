from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.core.exceptions import ValidationError
from django.views import generic, View
from django.views.generic.edit import FormView
from .models import Contrato
from .forms import LoadForm, UserForm, LoginForm
from .funciones import read_file
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


class LoginEmailView(LoginView):
    # Vista del formulario para el Login
    form_class = LoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('load') 

    def form_valid(self, form):
        user = form.get_user()
        if user:
            login(self.request, user)
            return HttpResponseRedirect(self.success_url)
        else:
            return self.form_invalid(form)
        
class RegistroView(FormView):
    # Vista para el registro del usuario con correo
    template_name = 'registro.html'
    form_class = UserForm
    success_url = reverse_lazy('load') 

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class LogoutView(View):
    #Vista para cerrar sesión
    def post(self, request):
        logout(request)
        return redirect('login')

class LoadView(LoginRequiredMixin, FormView):
    form_class = LoadForm
    template_name = "load.html"  
    success_url =  reverse_lazy('datos') 

    def form_valid(self, form):
        try:
            read_file(self.request.FILES['file'])
        except ValidationError as e:
            form.add_error(None, e.message)
            return self.form_invalid(form)
        return super().form_valid(form)
    
class ContratoView(LoginRequiredMixin,generic.ListView):
    model = Contrato
    template_name = 'datos.html'
    context_object_name = 'contratos'
    paginate_by = 20 

    # Diccionario de claves y nombres completos de columnas
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
        
        # Definir todas las columnas disponibles
        all_columns = self.column_names
        # Cambiamos el orden de las claves y nombres
        columns_names_reversed = {v: k for k, v in self.column_names.items()}

        # Obtener las columnas seleccionadas de la sesión o usar todas por defecto
        selected_columns = self.request.session.get('selected_columns', all_columns)
        # Obtener los nombres y claves de las columnas seleccionadas en un diccionario con ese orden.
        selected_columns_id = {key: columns_names_reversed[key] for key in selected_columns}
        # Obtener las claves seleccionadas
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
        # Procesar el formulario de selección de columnas
        selected_columns = request.POST.getlist('columns')
        
        # Guardar las selecciones en la sesión
        request.session['selected_columns'] = selected_columns
        
        # Redirigir a la misma página para evitar el reenvío del formulario
        return redirect(request.path_info)