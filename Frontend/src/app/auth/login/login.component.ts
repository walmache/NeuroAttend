import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';  // Asegúrate de que el servicio esté bien importado
import { FormsModule } from '@angular/forms';  // Importamos FormsModule

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
  
  username: string = '';
  password: string = '';

  constructor(private authService: AuthService, private router: Router) {}

  onSubmit() {
    // Log para verificar que los datos se están enviando
    console.log('Iniciando sesión con los siguientes datos:', this.username, this.password);

    // Llamamos al servicio para hacer login
    this.authService.login(this.username, this.password).subscribe(
      (response) => {
        // Log para verificar la respuesta de la API
        console.log('Respuesta de la API:', response);

        if (response && response.token) {
          const token = response.token;
          localStorage.setItem('token', token);  // Guardamos el token en localStorage
          console.log('Token guardado en localStorage:', token);

          // Decodificamos el token (suponiendo que contiene el rol)
          const decodedToken = this.decodeToken(token);
          console.log('Token decodificado:', decodedToken);

          // Redirigir según el rol del usuario
          if (decodedToken.role === 'admin' || decodedToken.role === 'moderator') {
            this.router.navigate(['/management/dashboard']);
            console.log('Redirigiendo a Dashboard...');
          } else {
            this.router.navigate(['/management/welcome']);
            console.log('Redirigiendo a la pantalla de bienvenida...');
          }
        } else {
          console.error('Respuesta sin token:', response);
        }
      },
      (error) => {
        // Log para verificar el error
        console.error('Error al iniciar sesión:', error);
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
