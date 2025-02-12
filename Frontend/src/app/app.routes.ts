import { Routes } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { ReunionesComponent } from './components/reuniones/reuniones.component';
import { BienvenidaComponent } from './components/bienvenida/bienvenida.component';
import { AuthGuardService } from './services/auth-guard.service';

export const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'dashboard', component: DashboardComponent, canActivate: [AuthGuardService] },
  { path: 'reuniones', component: ReunionesComponent, canActivate: [AuthGuardService] },
  { path: 'bienvenida', component: BienvenidaComponent, canActivate: [AuthGuardService] },
  { path: '**', redirectTo: 'login' }
];

