import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../shared/services/auth.service';
import { FormsModule } from '@angular/forms';  // Importamos FormsModule
import { NotificationService } from '../../shared/services/notification.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [
    FormsModule,  // Aseguramos que FormsModule esté importado para usar ngModel
  ],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  
  usuario: string = '';
  password: string = '';

  constructor(
    private authService: AuthService,
    private router: Router,
    private notificationService: NotificationService  // Inyectar el servicio
  ) {}

  onSubmit() {
    console.log('Iniciando sesión con los siguientes datos:', this.usuario, this.password);
    this.authService.login(this.usuario, this.password).subscribe(
      (response) => {
        console.log('Respuesta de la API:', response);
        if (response && response.token) {
          const token = response.token;
          localStorage.setItem('token', token);  // Guardamos el token en localStorage
          console.log('Token guardado en localStorage:', token);
          const decodedToken = this.decodeToken(token);
          console.log('Token decodificado:', decodedToken);
          if (decodedToken.rol === 'administrador' || decodedToken.rol === 'moderador') {
            this.router.navigate(['/management/dashboard']);
            this.notificationService.showMessage('success','Bienvenido al Dashboard');
          } else {
            this.router.navigate(['/management/welcome']);
            this.notificationService.showMessage('success','Bienvenido');
          }
        } else {
          this.notificationService.showMessage('error','Respuesta sin token');
        }
      },
      (error) => { 
        console.error('Error al hacer la solicitud HTTP:', error);
        let errorMessage = 'Error desconocido';
        if (error.status === 401) {
          errorMessage = 'Credenciales incorrectas';
        } else if (error.error && error.error.message) {
          errorMessage = error.error.message;
        }
        this.notificationService.showMessage('error',errorMessage);
      }
      
    );
  }

  decodeToken(token: string) {
    try {
      return JSON.parse(atob(token.split('.')[1]));  // Decodificar el JWT
    } catch (e) {
      console.error('Error al decodificar el token:', e);
      return null;
    }
  }
}
