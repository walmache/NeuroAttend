import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../services/auth.service';  // Importamos el servicio de autenticación

@Component({
  selector: 'app-login',
  standalone: true,
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  username: string = '';
  password: string = '';

  constructor(private authService: AuthService, private router: Router) {}

  onSubmit() {
    this.authService.login(this.username, this.password).subscribe(
      (response) => {
        const token = response.token;
        localStorage.setItem('token', token);  // Guardamos el token en localStorage

        // Aquí puedes decodificar el token y redirigir según el rol
        const decodedToken = this.decodeToken(token);
        if (decodedToken.role === 'admin' || decodedToken.role === 'moderator') {
          this.router.navigate(['/management/dashboard']);
        } else {
          this.router.navigate(['/management/welcome']);
        }
      },
      (error) => {
        console.error('Error al iniciar sesión', error);
      }
    );
  }

  decodeToken(token: string) {
    return JSON.parse(atob(token.split('.')[1]));  // Decodificar el JWT
  }
}
