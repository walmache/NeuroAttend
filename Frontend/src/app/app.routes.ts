import { Routes } from '@angular/router';
import { LoginComponent } from './auth/login/login.component';
import { RegisterComponent } from './auth/register/register.component';
import { DashboardComponent } from './management/dashboard/dashboard.component';
import { WelcomeComponent } from './management/welcome/welcome.component';

export const routes: Routes = [
  { path: '', redirectTo: '/auth/login', pathMatch: 'full' },
  { path: 'auth/login', component: LoginComponent },
  { path: 'auth/register', component: RegisterComponent },
  { path: 'management/dashboard', component: DashboardComponent },
  { path: 'management/welcome', component: WelcomeComponent },
  // Ruta para manejar rutas no encontradas (404)
  { path: '**', redirectTo: '/auth/login' },  // Redirige a login en caso de ruta no encontrada

];
